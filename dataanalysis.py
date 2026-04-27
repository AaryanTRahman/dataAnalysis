import pandas as pd

df = pd.read_csv("dataset_2.csv")

print(df.shape)
print(df.dtypes)
print(df.describe())
