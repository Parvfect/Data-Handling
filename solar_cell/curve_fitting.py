import numpy as np
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt



x = list(range(1,100))
y = [math.exp(i) for i in x]


def objective(x, a, b):
    return a*x + b

def curve_fitting(x, y):
    popt, pcov = curve_fit(objective, x, y, bounds=((-np.inf, -np.inf, 0, 0), (np.inf, np.inf, 1, 1)))
    print(popt)
    a, b = popt
    y1 = [objective(i, a, b) for i in x]
    return y1, a, b

"""
t = curve_fitting(x, y)
y1 = [objective(i, t[0], t[1]) for i in x]
plt.plot(x, y, 'o')
plt.plot(x, y1)
plt.show()
"""