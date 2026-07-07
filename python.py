import pandas as pd

df = pd.read_csv("data/supply_chain_enriched.csv")

print(df.columns)
print(df.head())
print(df["OrderStatus"].value_counts())
print(df["DeliveryStatus"].value_counts())
print(df["ProductCategory"].value_counts())