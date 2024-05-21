import pandas as pd

df =pd.read_csv("data.csv")

df["dm"] = df["distance"] * df["mass"]
print(df.head(1))


big = df[df["mass"] > 20 ]
print(big)