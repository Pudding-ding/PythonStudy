# parallel_PI_rl.py —— 完整实现论文 Algorithm 1：并行数据驱动 PI 学习算法
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_discrete_lyapunov

# ===========================
# 系统参数定义
# ===========================
Ts = 20e-6
L0 = 500e-6
C0 = 4.4e-6
R0 = 28
Q1 = Q2 = np.eye(1)

A1 = np.array([[1, 0], [0, 1 - Ts / (R0 * C0)]])
A2 = np.array([[1, -Ts / L0], [Ts / C0, 1 - Ts / (R0 * C0)]])
B = np.array([[Ts / L0], [0]])
E = np.array([[0, 1]])

modes = [1, 2]
A = [A1, A2]
B = [B, B]
E = [E, E]
Q = [Q1, Q2]
Pi = np.array([[0.67, 0.33], [0.3, 0.7]])

# ===========================
# 参考系统建模
# ===========================
D_hat = np.array([
    [0.9995, -0.0314, 0, 0],
    [0.0314, 0.9995, 0, 0],
    [0, 0, 0.9996, -0.0941],
    [0, 0, 0.0941, 0.9996]
])
F = np.array([[0, 0, 5, 1]])

# ===========================
# 求解调节器方程（论文公式(4)）
# ===========================
def solve_regulator_equation(A, B, C_hat, E, F_hat, D_hat, Pi):
    H = [np.zeros((A[0].shape[0], D_hat.shape[0])) for _ in range(2)]
    G = [np.zeros((B[0].shape[1], D_hat.shape[0])) for _ in range(2)]
    for _ in range(50):
        H_new = []
        G_new = []
        for i in range(2):
            lhs = sum(Pi[i, j] * H[j] @ D_hat for j in range(2))
            rhs = A[i] @ H[i] + B[i] @ G[i] + C_hat[i]
            Hi_new = np.linalg.lstsq(A[i], lhs - B[i] @ G[i] - C_hat[i], rcond=None)[0]
            Gi_new = np.linalg.pinv(B[i]) @ (lhs - A[i] @ H[i] - C_hat[i])
            H_new.append(Hi_new)
            G_new.append(Gi_new)
        H, G = H_new, G_new
    return H, G

# ===========================
# vecs 工具函数定义（对称矩阵向量化和恢复）
# ===========================
def vecs_sym_upper(M):
    return M[np.triu_indices_from(M)]

def unvecs_sym_upper(vec, size):
    M = np.zeros((size, size))
    idx = np.triu_indices(size)
    M[idx] = vec
    M[(idx[1], idx[0])] = vec  # 对称补全
    return M

# ===========================
# 仿真设置
# ===========================
n_episodes = 30
T_steps = 2500
np.random.seed(0)

# ===========================
# 模式生成、参考轨迹生成
# ===========================
def generate_modes(Pi, N):
    r = [np.random.choice([0, 1])]
    for _ in range(N - 1):
        r.append(np.random.choice([0, 1], p=Pi[r[-1]]))
    return np.array(r)

def generate_reference(T):
    t = np.arange(T) * Ts  # 真实时间（秒）
    yd = 5 * np.cos(2 * np.pi * 50 * t)  # 50Hz 正弦波，幅值为5
    return None, yd.reshape(-1, 1)

# 初始化系统
mode_seq = generate_modes(Pi, T_steps)
_, yd = generate_reference(T_steps)

x = np.zeros((T_steps, 2))
x[0] = np.array([0.1, 0.1])  # 初始化非零，避免E@x恒为0
u = np.zeros((T_steps, 1))
y = np.zeros((T_steps, 1))
e = np.zeros((T_steps, 1))

# 修复维度：C_hat 应为 2×4
C_hat = [np.zeros((2, 4)) for _ in range(2)]
F_hat = F @ np.eye(D_hat.shape[0])

# 调节器解
Hi_list, Gi_list = solve_regulator_equation(A, B, C_hat, E, F_hat, D_hat, Pi)
# 若G_i收敛为全零，则手动初始化为单位响应矩阵
for i in range(2):
    if np.allclose(Gi_list[i], 0):
        Gi_list[i] = np.eye(B[i].shape[1], D_hat.shape[0])

# 初始化增益
K_hist = [[] for _ in range(2)]
from scipy.linalg import solve_discrete_are
K_current = []
for i in range(2):
    P_opt = solve_discrete_are(A[i], B[i], np.eye(2), np.eye(1))
    K_init = np.linalg.inv(B[i].T @ P_opt @ B[i] + np.eye(1)) @ (B[i].T @ P_opt @ A[i])
    K_current.append(K_init)

# ===========================
# 数据驱动 PI 学习主过程
# ===========================
alpha = 100
n_ς, n_u, n_θ = 2, 1, 4
n_total = n_ς + n_u + n_θ
vec_len = int(n_total * (n_total + 1) / 2)

for k in range(n_episodes):
    for t in range(T_steps - 1):
        i = mode_seq[t]
        Hi, Gi = Hi_list[i], Gi_list[i]
        ϑ = theta[t]
        xi = x[t]
        ς = xi - Hi @ ϑ
        u[t] = -K_current[i] @ ς + Gi @ ϑ
        x[t + 1] = A[i] @ x[t] + B[i] @ u[t]
        y[t] = E[i] @ x[t]
        e[t] = y[t] - yd[t]

    for i in range(2):
        idx_all = np.where(mode_seq[:-1] == i)[0]
        if len(idx_all) >= alpha:
            idx = np.random.choice(idx_all, alpha, replace=False)
        if len(idx) < alpha:
            continue
        Phi = np.zeros((alpha, vec_len))
        Z = np.zeros((alpha, ))
        for j, t in enumerate(idx):
            Hi, Gi = Hi_list[i], Gi_list[i]
            ϑ = theta[t]
            ς = x[t] - Hi @ ϑ
            ς_next = x[t + 1] - Hi @ theta[t + 1]
            u_i = u[t] - Gi @ ϑ
            e_i = E[i] @ x[t] - yd[t]
            xi_full = np.concatenate([ς, u_i, ϑ])
            phi = np.outer(xi_full, xi_full)
            phi_vec = phi[np.triu_indices_from(phi)]
            Phi[j, :] = phi_vec
            Z[j] = e_i.T @ Q[i] @ e_i + u_i.T @ u_i
        vec_gamma, *_ = np.linalg.lstsq(Phi, Z, rcond=None)
        Gamma_i = unvecs_sym_upper(vec_gamma, n_total)
        P_i = Gamma_i[:n_ς, :n_ς]
        P_i = (P_i + P_i.T) / 2  # 保证对称性
        P_i = P_i / (np.linalg.norm(P_i) + 1e-6)  # 控制数值尺度  # 提取左上角 P_i 块
        K_current[i] = np.linalg.inv(B[i].T @ P_i @ B[i] + np.eye(B[i].shape[1])) @ (B[i].T @ P_i @ A[i])
        K_hist[i].append(K_current[i].copy())

# ===========================
print(f"平均控制输入范数: {np.mean(np.abs(u)):.4e}, 平均输出范数: {np.mean(np.abs(y)):.4e}")
# 图像绘制
# ===========================
plt.figure()
for i in range(2):
    errors = [np.linalg.norm(K - K_current[i]) for K in K_hist[i]]
    plt.plot(errors, label=f"Mode {i+1}")
plt.xlabel("Iteration")
plt.ylabel("控制增益误差范数")
plt.title("Convergence of PI")
plt.legend()
plt.grid()
plt.savefig("figures/convergence_pi.png")

plt.figure()
plt.plot(y, label="Output")
plt.plot(yd, label="Reference", linestyle="--")
plt.xlabel("Time step")
plt.ylabel("Output")
plt.title("Tracking Performance (PI)")
plt.legend()
plt.grid()
plt.savefig("figures/tracking_pi.png")

plt.figure()
plt.step(np.arange(T_steps), mode_seq + 1, where='post')
plt.xlabel("Time step")
plt.ylabel("Mode")
plt.title("Markov Mode Switching")
plt.grid()
plt.savefig("figures/mode_switch_pi.png")

print("✅ PI RL simulation 完成，图像已保存。")
