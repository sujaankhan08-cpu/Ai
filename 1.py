import pandas as pd

data = pd.read_csv("amazon_sales_dataset.csv")

print(data.head())

print(data.tail())

print(data.info())

print(data.describe())