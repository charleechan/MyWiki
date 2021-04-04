import seaborn  # 酷炫点的主题,可以去掉
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_tight_layout(True)
plt.style.use('seaborn-pastel')

# 询问图形在屏幕上的大小和DPI（每英寸点数）
# 注意当把图形保存为文件时，需要为此单独再提供一个DPI
print('fig size: {0} DPI, size in inches {1}'.format(fig.get_dpi(),
                                                     fig.get_size_inches()))

# 绘制一个保持不变（不会被重新绘制）的散点图以及初始直线
x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))
line, = ax.plot(x, x - 5, 'r-', linewidth=2)


def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    # 更新直线和轴（用一个新X轴标签）
    # 以元组形式返回这一帧需要重新绘制的物体
    line.set_ydata(x - 5 + i)
    ax.set_xlabel(label)
    return line, ax


if __name__ == '__main__':
    # 会为每一帧调用Update函数
    # 这里FunAnimation设置一个10帧动画，每帧间隔200ms
    anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=200)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('line.gif', dpi=80, writer='imagemagick')
    else:
        plt.show()