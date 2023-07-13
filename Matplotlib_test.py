from matplotlib import pyplot as plt
import random

# 设置图片大小
# 通过实例化figure并传递参数，能够在后台自动使用该figure实例
fig = plt.figure(figsize=(20, 9), dpi=80)

x = range(120)
# y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
y = [random.randint(20, 35) for i in range(120)]

plt.plot(x, y)

# 设置轴刻度（输入一个代表轴的数据的列表）
# plt.xticks(range(0, 25))
plt.yticks(range(min(y), max(y) + 1))

# 设置轴刻度为字符串
xtick_labels = ["10:{}".format(i) for i in range(60)]
xtick_labels += ["11:{}".format(i) for i in range(60)]
plt.xticks(list(x)[::10], xtick_labels[::10], rotation=-90)

# 保存图片
# plt.savefig("./t1.png")

plt.show()
