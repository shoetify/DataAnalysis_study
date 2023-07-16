from matplotlib import pyplot as plt

# 定义条形宽度
BAR_WIDTH = 0.2

x_axis = ['Xingqiu3: Final War', "Dunkerk", "Spider Man: Hero Return", "War Wall: 2"]
y_16 = [15746, 312, 4497,319]
y_15 = [12357, 156, 2045, 168]
y_14 = [2358, 399, 2358, 362]

x_14 = list(range(len(x_axis)))
x_15 = [i+BAR_WIDTH for i in x_14]
x_16 = [i+BAR_WIDTH for i in x_15]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.bar(x_14, y_14, width=0.2, label="14")
plt.bar(x_15, y_15, width=0.2, label="15")
plt.bar(x_16, y_16, width=0.2, label="16")

# 绘制图例
plt.legend()

# 设置x轴刻度
plt.xticks(x_15, x_axis)

plt.show()
