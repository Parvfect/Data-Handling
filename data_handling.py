import numpy as np
import matplotlib.pyplot as plt
import math


f = []
v = []

input_files = ["RLC150ohm","RLC410ohm","RLC22ohm","RLC47ohm"]


def read_data(input_file):
    
    file = open(input_file, "r")
    # Skipping one line
    file.readline()

    for i in file:
        
        temp_arr = i.split(' ')

        f.append(float(temp_arr[0]))
        v.append(float(temp_arr[1]))
     
def plot():

    plt.plot(f,v)
    plt.grid()
    plt.title("{}".format(input_file))
    plt.show()




input_file = input("Enter input file")
read_data(input_file)
plot()