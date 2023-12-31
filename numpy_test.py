import numpy as np
import pandas as pd

# 创建数组
t1 = np.array([3, 4, 5])
t2 = np.array(range(10))
t3 = np.arange(3, 10, 2)

print(t1)
print(t2)
print(t3)

# 数组类型
print(type(t1), type(t2), type(t3))

# 数组中的数据类型
print(t1.dtype, t2.dtype, t3.dtype)

# Numpy 指定数据类型
t4 = np.array(range(4), dtype="float32")
print(t4)
print(t4.dtype)

# Numpy 修改数组数据类型
t5 = t4.astype("int32")
print(t5)
print(t5.dtype)

# Numpy 保留小数位数
t6 = np.array([3.145, 56.6343, 12.2314, 12.111])
t7 = np.round(t6, 2)
print(t7)

# Numpy 数组的形状（维数）
t8 = np.array([[2, 3, 4], [5, 6, 7]])
print(t8)
print(t8.shape)
print(t8.reshape(6, ))

# 矩阵的转置
t9 = np.arange(24).reshape((4, 6))
print(t9)
print(t9.transpose())


df = pd.DataFrame()
df.sort_values()