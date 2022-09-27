
import math

from scipy.stats import sem

def get_theta(x,y):
    """ Returns angle in radians """
    return math.atan(math.radians(y)/math.radians(x))

def get_p(x,y):
    p1 = (0.5/(1.39e9))*math.sqrt(x**2 + y**2)
    return math.atan(math.radians(2*p1/0.5)) - p1

def get_B(B0, p, P, theta):
    t = math.sin(math.radians(B0))*math.cos(math.radians(p))
    u = math.cos(math.radians(B0)) * math.sin(math.radians(p)) * math.cos(math.radians(P - theta))
    return math.asin(t + u)

def get_L(p, theta, B, Lo):
    t = math.sin(math.radians(p)) * math.sin(math.radians(p -theta))
    u = math.cos(math.radians(B))
    return math.asin(t/u) + Lo

def convert_coordinates(X,Y, B0, L0, P):
    """ Converts coordinates to stonyhurst """
    
    theta = []
    B = []
    L = []

    for x,y in zip(X,Y):
        p = get_p(x,y)
        theta_ = get_theta(x,y)
        B.append(get_B(B0, p, P, theta_))
        L.append(get_L(p, theta_, B0, L0))
        theta.append(theta_)

    return theta, B, L
        
def get_rotation(L, total_time):
    """ Returns rotation rate """
    return L/total_time

# Read from text file
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def read_from_file():

    t,x,y = [], [], []
    file_ = read_file('singleSunspot.txt')

    for i in file_:
        arr = i.split()
        t.append(float(arr[0]))
        x.append(float(arr[1]))
        y.append(float(arr[2]))

    return t,x,y


t,x,y = read_from_file()
# Split into four days with time 4, 9 and 14 boundaries
t1 = [i for i in t if i < 4]
x1 = x[:len(t1)]
y1 = y[:len(t1)]

t2 = [i for i in t if i >= 4 and i < 9]
x2 = x[len(t1):len(t1)+len(t2)]
y2 = y[len(t1):len(t1)+len(t2)]

t3 = [i for i in t if i >= 9 and i < 14]
x3 = x[len(t1)+len(t2):len(t1)+len(t2)+len(t3)]
y3 = y[len(t1)+len(t2):len(t1)+len(t2)+len(t3)]

t4 = [i for i in t if i >= 14]
x4 = x[len(t1)+len(t2)+len(t3):len(t1)+len(t2)+len(t3)+len(t4)]
y4 = y[len(t1)+len(t2)+len(t3):len(t1)+len(t2)+len(t3)+len(t4)]


# Get stonyhurst for each day 
B1 = 0.64
l1 = 85.66 
P1 = -11.05


B2 = 0.76
l2 = 72.42
P2 = -10.63

B3 = 0.88
l3 = 59.18
P3 = -10.2

B4 = 1
l4 = 45.95
P4 = -9.78

theta1, B1, L1 = convert_coordinates(x1, y1, B1, l1, P1)
theta2, B2, L2 = convert_coordinates(x2, y2, B2, l2, P2)
theta3, B3, L3 = convert_coordinates(x3, y3, B3, l3, P3)
theta4, B4, L4 = convert_coordinates(x4, y4, B4, l4, P4)

L = [L1, L2, L3, L4]
B = [B1, B2, B3, B4]

print(sem(L))

# w = L/T
# T = 2pi/w
