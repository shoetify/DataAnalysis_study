import pandas as pd
from matplotlib import pyplot as plt

file_path = "IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df.head(1))
# print(df.info())

# 画runtime的分布情况 ： 使用直方图

runtime_data = df["Runtime (Minutes)"]

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

print(max_runtime, min_runtime)

# 计算组数
DISTANCE = 5

num_bin = (max_runtime - min_runtime) // DISTANCE

# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(runtime_data, num_bin)

plt.xticks(range(min_runtime, max_runtime + DISTANCE, DISTANCE))

plt.show()


