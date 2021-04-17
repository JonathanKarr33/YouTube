# pip install pandas
# pip install numpy
import pandas as pd
import numpy as np

df = pd.read_csv("Jonathan Karr Running Data.csv")
print(df)
print(type(df))
print("")
print(df["Distance (mi)"])
print("")
print(df[2:5])
print("")
print(df.iloc[0:4,1:4])
print("")
print(df.loc[df.index[1:5],["Date","Distance (mi)"]])
print("")
df = df.set_index("Date")
print(df)
print("")
print(df[["Day of Week","Distance (mi)"]])
print("")
print(df.sum(numeric_only=True))