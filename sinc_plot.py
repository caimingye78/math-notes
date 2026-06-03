import numpy as np
import matplotlib.pyplot as plt

# 定义 x 范围，避免 x=0 处的除零问题
x = np.linspace(-20, 20, 1000)

# 使用 np.sinc 注意：np.sinc(x) = sin(pi*x)/(pi*x)
# 所以我们手动计算 sin(x)/x
y = np.where(x != 0, np.sin(x) / x, 1.0)  # x=0 时极限值为 1

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=r'$y = \frac{\sin(x)}{x}$')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title(r'$y = \frac{\sin(x)}{x}$', fontsize=16)
plt.legend(fontsize=12)
plt.ylim(-0.4, 1.2)
plt.tight_layout()
plt.savefig('/projects/sandbox/sinc_plot.png', dpi=150)
plt.close()

print("图像已保存为 sinc_plot.png")
