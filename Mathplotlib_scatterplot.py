from matplotlib import pyplot as plt

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 18, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]

x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.scatter(x_3, y_3, label="Mar")
plt.scatter(x_10, y_10, label="Oct")

# 调整x轴刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3/{}".format(i) for i in x_3]
_xtick_labels += ["10/{}".format(i - 50) for i in x_10]
plt.xticks(_x, _xtick_labels, rotation=45)

# 添加描述信息
plt.xlabel("time")
plt.ylabel("temperature")
plt.title("Title")

# 显示图例
plt.legend(loc="upper left")

# 展示
plt.show()
