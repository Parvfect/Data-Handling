import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from curve_fitting import curve_fitting, objective
import math

df = pd.read_excel("solarcell.xlsx")

print(df["I1"])

x = df["V1"]
y = df["I1"]

y = y[1:]
x = x[1:]
#y1, a, b = curve_fitting(x, y)
y = [math.log(i) for i in y]

print(x)
print(y)
"""
plt.plot(x,y, 'o')
plt.plot(x, y1)
plt.show()
"""