import numpy as np
import matplotlib.pyplot as plt

# 参数设置
dt = 0.01  # 时间步长
T = 10  # 总时间
steps = int(T / dt)  # 总步数

# 过程噪声和观测噪声
Q = np.diag([0.01, 0.01, 0.001, 0.001])  # 过程噪声协方差
R = np.diag([0.1, 0.1])  # 观测噪声协方差

# 状态转移矩阵
F = np.array([
    [1, 0, dt, 0],
    [0, 1, 0, dt],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# 观测矩阵
H = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])

# 初始状态和协方差
x_true = np.array([0, 0, 1, 1])  # 真实状态 [角度, 速度, 角度, 速度]
x_est_ekf = np.array([0, 0, 0, 0])  # EKF估计状态
x_est_ukf = np.array([0, 0, 0, 0])  # UKF估计状态
P_ekf = np.eye(4)  # EKF协方差矩阵
P_ukf = np.eye(4)  # UKF协方差矩阵

# UKF参数
alpha = 1e-3
beta = 2
kappa = 0
n = 4  # 状态维度
lambda_ = alpha**2 * (n + kappa) - n

# 存储结果
true_states = []
ekf_states = []
ukf_states = []

# EKF 更新函数
def ekf_update(x_est, P, z):
    # 预测步骤
    x_pred = F @ x_est
    P_pred = F @ P @ F.T + Q

    # 更新步骤
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
    x_est = x_pred + K @ (z - H @ x_pred)
    P = (np.eye(4) - K @ H) @ P_pred

    return x_est, P

# UKF 更新函数
def ukf_update(x_est, P, z):
    # 生成Sigma点
    sigma_points = np.zeros((2 * n + 1, n))
    W = np.zeros(2 * n + 1)
    sigma_points[0] = x_est
    W[0] = lambda_ / (n + lambda_)
    U = np.linalg.cholesky((n + lambda_) * P)
    for i in range(n):
        sigma_points[i + 1] = x_est + U[:, i]
        sigma_points[n + i + 1] = x_est - U[:, i]
        W[i + 1] = 1 / (2 * (n + lambda_))
        W[n + i + 1] = 1 / (2 * (n + lambda_))

    # 预测步骤
    sigma_points_pred = np.array([F @ point for point in sigma_points])
    x_pred = np.sum(W[:, None] * sigma_points_pred, axis=0)
    P_pred = np.sum(W[:, None, None] * (sigma_points_pred - x_pred)[:, :, None] @ (sigma_points_pred - x_pred)[:, None, :], axis=0) + Q

    # 更新步骤
    z_points = np.array([H @ point for point in sigma_points_pred])
    z_pred = np.sum(W[:, None] * z_points, axis=0)
    P_zz = np.sum(W[:, None, None] * (z_points - z_pred)[:, :, None] @ (z_points - z_pred)[:, None, :], axis=0) + R
    P_xz = np.sum(W[:, None, None] * (sigma_points_pred - x_pred)[:, :, None] @ (z_points - z_pred)[:, None, :], axis=0)
    K = P_xz @ np.linalg.inv(P_zz)
    x_est = x_pred + K @ (z - z_pred)
    P = P_pred - K @ P_zz @ K.T

    return x_est, P

# 仿真循环
for t in range(steps):
    # 真实状态更新
    x_true = F @ x_true + np.random.multivariate_normal([0, 0, 0, 0], Q)
    z = H @ x_true + np.random.multivariate_normal([0, 0], R)

    # EKF 更新
    x_est_ekf, P_ekf = ekf_update(x_est_ekf, P_ekf, z)

    # UKF 更新
    x_est_ukf, P_ukf = ukf_update(x_est_ukf, P_ukf, z)

    # 保存结果
    true_states.append(x_true)
    ekf_states.append(x_est_ekf)
    ukf_states.append(x_est_ukf)

# 转换为数组
true_states = np.array(true_states)
ekf_states = np.array(ekf_states)
ukf_states = np.array(ukf_states)

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(true_states[:, 0], true_states[:, 1], label="True Trajectory", color="black")
plt.plot(ekf_states[:, 0], ekf_states[:, 1], label="EKF Estimate", linestyle="--")
plt.plot(ukf_states[:, 0], ukf_states[:, 1], label="UKF Estimate", linestyle="-.")
plt.xlabel("Rotor Angle")
plt.ylabel("Rotor Speed")
plt.title("Dynamic State Estimation: EKF vs UKF")
plt.legend()
plt.grid()
plt.show()