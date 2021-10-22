import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as stats


f = []
v = []
input_file = ""
input_files = ["RLC150ohm","RLC410ohm","RLC22ohm","RLC47ohm"]

markers=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_']

def read_data(input_file):
    
    file = open(input_file, "r")
    # Skipping one line
    file.readline()

    temp_f = []
    temp_v = []

    for i in file:
        
        temp_arr = i.split(' ')

        temp_f.append(float(temp_arr[0]))
        temp_v.append(float(temp_arr[1]))

    f.append(temp_f)
    v.append(temp_v) 

def calculate_resonance():
    
    max_volt = []
    max_freq = []
    for i,j in zip(v,f):
        max_volt.append(max(i))
        index = i.index(max(i))
        max_freq.append(j[index])

    res_volt = stats.mean(max_volt)
    res_freq = stats.mean(max_freq)
    print(res_volt)
    print(res_freq)
    print("Standard Deviation = ", stats.stdev(max_volt))
    print("Standard Deviation = ", stats.stdev(max_freq))

    return res_volt, res_freq

def better_plot():

    fr = []
    vr = []
    for i,j in zip(f,v):
        vt = [c for c in j if c>5.1]
        indexes = [j.index(c) for c in vt]
        frt = [i[c] for c in indexes]
        fr.append(frt)
        vr.append(vt)

    for i,j in zip(fr[3:],vr[3:]):
        plt.scatter(i,j)
    plt.grid()
    plt.title("Superposition Plot")
    plt.show()


def plot():
    
    res_volt, res_freq = calculate_resonance()
    for i,j in zip(f,v):
        plt.plot(i,j)

    plt.plot(res_freq, res_volt, marker=markers[2])
    plt.annotate('Average resonance point = {}Hz'.format(res_freq), xy=(res_freq, res_volt),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )
    plt.grid()
    plt.title("Superposition Plot")
    plt.show()




for i in input_files:
    input_file = i
    read_data(input_file)


plot()
better_plot()