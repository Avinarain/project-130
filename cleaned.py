import pandas as pd
import csv

df=pd.read_csv("stars.csv")

del df["star_name"]
del df["distance"]
del df["mass"]
del df["radius"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

df.to_csv("cleaned_dataset.csv")

print(df.columns)
print(list(df))