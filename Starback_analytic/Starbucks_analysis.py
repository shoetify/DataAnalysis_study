import pandas as pd
import numpy as np

file_path = "starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)

grouped = df.groupby(by="Country")
# 获得DataFrameGroupBy 对象

# 可以进行遍历
# for i, j in grouped:
#     print(i, type(i))
#     print("-" * 100)
#     print(j, type(j))
#     print("*" * 100)

# 可以调用聚合方法
# print(grouped["Brand"].count())

# 统计中国每个省店铺的数量
china_data = df[df["Country"] == "CN"]

grouped = china_data.groupby(by="State/Province").count()["Brand"]

print(grouped)