# pip install pandas
# pip install numpy
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(4),name="values")
s = np.abs(s) * 10
s.index = ["Freshman","Sophomore","Junior","Senior"]
print(s)
print(s["Senior"])
print(s.describe())