import pandas as pd

file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# 获取电影平均评分

print(df["Rating"].mean())

# 获取导演的人数
print(len(df["Director"].unique()))

# 获取演员的人数
temp_actors_list = df["Actors"].str.split("，").tolist()
actor_list = [i for j in temp_actors_list for i in j]
actor_count = len(set(actor_list))

print(actor_count)