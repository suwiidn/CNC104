#suwijuk 6809658138


import requests
import pandas as pd

df = pd.DataFrame(requests.get("https://jsonplaceholder.typicode.com/posts").json())

print(df.head())
print("\nColumns:")
print(df.columns)
print("\nNumber of rows:")
print(len(df))

df["title_length"] = df["title"].str.len()

posts_per_user = df.groupby("userId")["id"].count().sort_values(ascending=False)
print("\nPosts per user:")
print(posts_per_user.to_string())