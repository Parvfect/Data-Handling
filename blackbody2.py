
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def read_double_column_data(file_name):
    # Read text file
    a = []
    b = []

    f = open(file_name, "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.

    for i in lines:
        
        j = i.split(' ')
        if j == '':
            continue
        a.append(float(j[0]))
        b.append(float(j[1]))
        
    return a, b

def plot(x,y, title, xlabel, ylabel, xerr, yerr):

    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.errorbar(x, y, xerr = xerr, yerr = yerr,  barsabove = True, ecolor = "Red")
    plt.show()


deg1, ir1 = read_double_column_data("t1.txt")
deg2, ir2 = read_double_column_data("t2.txt")
deg3, ir3 = read_double_column_data("t3.txt")
deg4, ir4 = read_double_column_data("t4.txt")

plt.plot(deg1, ir1)
plt.plot(deg2, ir2)
plt.plot(deg3, ir3)
plt.plot(deg4, ir4)
plt.title("Superposition Plot")
plt.xlabel("Angle  +/- 1")
plt.ylabel("Irradiance W/m^2 +/- 0.5")
plt.show()
