from matplotlib import pyplot as plt
import random
import matplotlib

# 设置线条属性
matplotlib.rc('lines', linewidth=4, color='green')

# 设置图片大小
# 通过实例化figure并传递参数，能够在后台自动使用该figure实例
fig = plt.figure(figsize=(20, 9), dpi=80)

x = range(120)
# y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
y_1 = [random.randint(20, 35) for i in range(120)]
y_2 = [random.randint(20, 35) for i in range(120)]


# 添加图例
plt.legend()

# 设置轴刻度（输入一个代表轴的数据的列表）
# plt.xticks(range(0, 25))
plt.yticks(range(min(y_1), max(y_1) + 1))

# 设置轴刻度为字符串
xtick_labels = ["10:{}".format(i) for i in range(60)]
xtick_labels += ["11:{}".format(i) for i in range(60)]
plt.xticks(list(x)[::10], xtick_labels[::10], rotation=-90)

# 添加描述信息
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Time-Temperature in 10am-12am")

# 绘制网格
plt.grid(alpha=0.4)
# 设置透明度

# 保存图片
# plt.savefig("./t1.png")

plt.show()
