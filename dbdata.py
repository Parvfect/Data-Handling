import numpy as np
import matplotlib.pyplot as plt
import math

T = [[]]
X = [[]]
Y = [[]]
E = [[]]
ptr = 0

input_files = ['db1','db2','db3','db4']

l = 198
delt = 0.04

V_x = []
V_y = []

def read_data(input_file):

    global ptr
    t = []
    x = []
    y = []
    v_x = []
    v_y = []
    en = []

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

    
    for i in range(len(x)-1):
        v_x.append((x[i+1] - x[i])/delt)
    

    for i in range(len(y)-1):
        v_y.append((y[i+1] - y[i])/delt)
    
   

    for i in range(len(x)-1):
        en.append(v_x[i] +v_y[i])
    
    en = [abs(i) for i in en]

    T.append(t)
    X.append(x)
    Y.append(y)
    V_x.append(v_x)
    V_y.append(v_y)
    E.append(en)
    ptr+=1

def plot():

    plt.plot(T[4][200:800] ,  X[4][200:800] )
    plt.plot(T[3][200:800] ,  X[3][200:800] )
    plt.plot(T[2][200:800] ,  X[2][200:800] )
    plt.plot(T[1][200:800] ,  X[1][200:800] )
    plt.ylabel(" X in mm")
    plt.xlabel("Time in seconds")
    plt.show()

    plt.plot( X[4][:-1],  V_x[3] )
    plt.plot( X[3][:-1],  V_x[2] )
    plt.plot( X[2][:-1],  V_x[1] )
    plt.plot( X[1][:-1],  V_x[0] )
    plt.xlabel(" X in mm")
    plt.ylabel(" X velocity")
    plt.show()


def plot_vanilla(t,x,v,y):
    
    plt.plot(t,x)
    plt.xlabel("Time (s)")
    plt.ylabel("x (mm)")
    plt.show()
    
    plt.plot(t,y)
    plt.xlabel("Time (s)")
    plt.ylabel("y(mm)")
    plt.show()
    
    plt.plot(x[:-1], v_x)
    plt.xlabel("x(mm)")
    plt.ylabel("Velocity")
    plt.show()
    
    
    plt.plot(y[:-1], v_y)
    plt.xlabel("y(mm)")
    plt.ylabel("Velocity")
    plt.show()
    
    o = []
    p =[]
    for i in range(len(x)):
        o.append(8* (x[i] + y[i]))
     
    for i in range(len(v_x)):
        p.append((v_x[i] + v_y[i]))
     
    plt.plot(t[:-1],o[:-1])
    plt.plot(t[:-1],p)
    plt.xlabel("Time (s)")
    plt.ylabel("Potential and Kinetic energies (Not to scale)")
    plt.legend()
    plt.show()

for i in input_files:
    read_data(i)

plot()