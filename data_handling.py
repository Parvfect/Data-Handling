import numpy as np
import matplotlib.pyplot as plt
import math

t = []
x = []
y = []
input_file = "db1"
theta = []
l = 198
T = 0.04
v = []
E = []

def read_data(input_file):

    file = open(input_file, "r")
    # Skipping two lines
    file.readline()
    file.readline()

    for f in file:
        
        temp_arr = f.split(',')

        if(temp_arr[0] == "" or temp_arr[1] == "" or temp_arr[2] == "" ):
            break
        
        t.append(float(temp_arr[0]))
        x.append(float(temp_arr[1]))
        y.append(float(temp_arr[2]))

    """
    for i in range(len(x)-1):
        v.append((x[i+1] - x[i])/T)
    """
   
read_data(input_file)

try:
    for i in y:
        theta.append(math.acos(i/l))


    for i in range(len(x)-1):
        v.append((theta[i+1] - theta[i])/T)
    
    v = [i/8 for i in v]
    
    for i in range(len(x)-1):
        E.append(v[i] +y[i])
    
    E = [abs(i) for i in E]

except:
    print(i/l)

def plot():
    plt.plot(t,y)
    plt.show()
    """
    plt.plot(t[:-1],v)
    plt.show()

    plt.plot(theta[:-1], v)
    plt.show()

    plt.plot(t[:-1],v)
    plt.plot(t[:-1], theta[:-1])
    plt.show()

    plt.plot(t[:-1], E)
    plt.show()
    """
plot()