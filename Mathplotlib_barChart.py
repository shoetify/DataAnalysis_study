from typing import List

from matplotlib import pyplot as plt

x_axis = ['Zhanlang2', 'Speed8', 'Kongfu Yoga', "Karabi Haidu"]
y_axis = [56.01, 26.94, 17.53, 15.45]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.xticks(rotation=90)

# 绘图 （纵向条形图）
#plt.bar(x_axis, y_axis, width=0.3, color="orange")

# 绘图 （横向条形图）
plt.barh(x_axis, y_axis, height=0.3, color="orange")

# 网格
plt.grid(alpha=0.4)

# 展示
plt.show()
