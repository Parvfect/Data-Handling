
import matplotlib.pyplot as plt
import numpy as np
import math

sr = []
t = []
r = []
P = []
R = []
T = []

def read_specific_resistance_data(file_name):
    # Read text file

    f = open(file_name, "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.

    for i in lines:
        j = i.split(' ')
        t.append(float(j[0]))
        sr.append(float(j[1][:-1]))


def read_numbers_from_file(filename):
    """ Reads all the numbers in a file seperated by \n and returns the array"""
   
    arr = []
    f = open(filename, "r")
    lines = f.readlines()
    for i in lines:
        if i!= ' ' and i!= '':
            arr.append(float(i[:-1]))

    return arr

def plot(x,y, title, xlabel, ylabel, xerr, yerr, inter = False, intercept = 0):
    """ Plot y against x"""
    
    line2d = plt.plot(x, y)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.errorbar(x,y, xerr=0.1, yerr=0, barsabove = True, ecolor = "Red")
    plt.show()

def resistance_values():

    k = 1.2

    for i in sr:
        r.append(k*float(i))
    
    s = [x/100 for x in t]
    plot(s , r, "", "Temperature (100 kelvin)", "Resistance(ohm)",  0.19, 0.0),

def calculate_power(R, I):
    return I*I*R

def get_point(x):
    """ Getting a point that is not within the data"""
    m,b = np.polyfit(r, [x/100 for x in t], 1)
    return (m*x + b)

def plot_power_temperature(power, temperature):
    """ Plots log of power against temperature"""
    power = [math.log(i) for i in power]
    temperature = [math.log(i) for i in temperature]
    plt.plot(temperature, power)
    m,b = np.polyfit(power, temperature, 1)
    plt.title("Stefan Boltzmann's Law - {}".format(m*100))
    plt.xlabel("log - Temperature (K)")
    plt.ylabel("log - Power (W)")
    plt.errorbar(temperature, power, xerr=0.005, yerr=0.005, barsabove = True, ecolor = "Red")
    plt.show()

read_specific_resistance_data("sr.txt")
#plot(t, sr, "", "Temperature", "Specific Resistance", True, 0)
resistance_values()

P = read_numbers_from_file("power.txt")
R = read_numbers_from_file("resistance.txt")

print(len(t))
print(len(R))

for i in R:
    T.append(get_point(i))

print(T)

plot_power_temperature(P, T)