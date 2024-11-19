# 代码生成对比动画
import matplotlib.animation as animation

fig, ax = plt.subplots()
lines = []
params = [
    (0.1, 0, "Kp=0.1, Ki=0"),
    (0.6, 0, "Kp=0.6, Ki=0"),
    (0.45, 30, "Kp=0.45, Ki=30"),
    (0.45, 43.5, "OPTIMAL")
]

def animate(i):
    ax.clear()
    Kp, Ki, label = params[i]
    pid = PIDController(Kp, Ki)
    voltage = simulate(pid)  # 伪代码：仿真函数
    ax.plot(voltage, label=label)
    ax.axhline(30.5, ls='--', c='r')
    ax.axhline(29.5, ls='--', c='r')
    ax.legend()

ani = animation.FuncAnimation(fig, animate, frames=4, interval=2000)