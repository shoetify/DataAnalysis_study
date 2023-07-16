from matplotlib import pyplot as plt
import random

# 设置组距
DISTANCE = 6  # 组距

a = [random.randint(80, 160) for i in range(1000)]

# 设置x轴刻度
plt.xticks(range(min(a), max(a) + DISTANCE, DISTANCE))

# 绘图
plt.hist(a, range(min(a), max(a) + DISTANCE, DISTANCE))

plt.grid()

plt.show()
