import pandas as pd

df = pd.read_csv("books.csv")

print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())
##Rating analiz
print("\nRating Distribution:")
print(df["Rating"].value_counts())
## ən bahalı kitab
print("\nMost Expensive Book:")
print(df.loc[df["Price"].idxmax()])
##Ən ucuz kitab
print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()])
##Average
print("\nAverage Price:")
print(df["Price"].mean())
##Media
print("\nMedian Price:")
print(df["Price"].median())


print("\nPrice Standard Deviation:")
print(df["Price"].std())
print(df["Rating"].value_counts())

print(df.groupby("Rating")["Price"].mean())

print(df.groupby("Page")["Price"].mean().head())