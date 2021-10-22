import numpy as np
import matplotlib.pyplot as plt
import math

t = {
300 ,5.64
400 ,8.06
500, 10.74
600, 13.54
700, 16.46
800, 19.47
900, 22.58
1000, 25.70
1100, 28.85
1200, 32.02
1300, 35.24
1400, 38.52
1500, 41.85
1600, 45.22
1700, 48.63
1800, 52.08
1900, 55.57
2000, 59.10
2100 ,62.65
2200 66.25
2300 69.90
2400 73.55
2500 77.25
2600 81.0
2700 84.7
2800 88.5
2900 92.3
3000 96.2
3100 100.0
3200 103.8
3300 107.8
3400 111.7
3500 115.7
3655 121.8


T = [[]]
X = [[]]
Y = [[]]
Theta = [[]]
V = [[]]
E = [[]]
ptr = 0

input_files = ['phy1','phy2','phy3','phy4']

l = 198
delt = 0.04

v_x = []
v_y = []

def read_data(input_file):

    global ptr
    t = []
    x = []
    y = []
    v = []
    en = []
    theta = []

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
    DP
    for i in range(len(x)-1):
        v_x.append((x[i+1] - x[i])/T)
    

    for i in range(len(y)-1):
        v_y.append((y[i+1] - y[i])/T)
    """

    
    for i in x:
        val = math.asin(i/l) * (180/3.14)
        #Normalising if val>18:
         #   theta.append(17)
        #else:
        theta.append(math.asin(i/l) * (180/3.14))


    for i in range(len(x)-1):
        v.append((theta[i+1] - theta[i])/delt)
    
    v = [i/5 for i in v]
    
    for i in range(len(x)-1):
        en.append(v[i] +y[i])
    
    en = [abs(i) for i in en]

    T.append(t)
    X.append(x)
    Y.append(y)
    Theta.append(theta)
    V.append(v)
    E.append(en)
    ptr+=1

def plot():

    plt.plot(T[4] , Theta[4] )
    plt.plot(T[3] , Theta[3] )
    plt.plot(T[2] , Theta[2] )
    plt.plot(T[1] , Theta[1] )
    plt.ylabel("Theta in degrees")
    plt.xlabel("Time in seconds")
    plt.show()

    plt.plot(Theta[4][:-1], V[4] )
    plt.plot(Theta[3][:-1], V[3] )
    plt.plot(Theta[2][:-1], V[2] )
    plt.plot(Theta[1][:-1], V[1] )
    plt.xlabel("Theta in degrees")
    plt.ylabel("Theta velocity")
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