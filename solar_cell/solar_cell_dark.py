import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from curve_fitting import curve_fitting, objective
import math

q = 1.602176634e-19
T = 298

def get_boltzmann(a, b):
    return -(q*b)/(a*T*2.54) 

df = pd.read_excel("scd.xlsx")

print(df["I2"])

x = df["V2"][2:]
y = df["I2"][2:]

print(y)
y = [math.log(i) for i in y]

plt.plot(x,y)
plt.show()
"""
x = df["V1"]
y = df["I1"]

y = y[5:10]
x = x[5:10]


y = [math.log(i) for i in y]
y1, a, b = curve_fitting(x, y)


plt.plot(x,y, 'o')
plt.plot(x, y1)
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.errorbar(x,y,xerr=0.01, yerr=0.01, fmt='o')
plt.title("Steffan Boltzmann Law with k as {}".format(get_boltzmann(a, b)))
plt.show()

"""