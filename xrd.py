import numpy as np
import math

sample_a = [29.9, 42.8, 53.1, 62.1, 70.5, 78.4, 86.1, 93.7, 101.5, 109.4, 117.7, 126.7, 137]

sample_b = [44.5, 51.9, 76.5, 93, 98.5, 122.1, 145, 156.1]

sample_c = [28.5, 47.3, 56.2, 69.2, 76.5, 88.1, 95.1, 106.8, 114.2]

sample_a = np.array(sample_a)
sample_b = np.array(sample_b)
sample_c = np.array(sample_c)

sample_a = sample_a/2
sample_b = sample_b/2
sample_c = sample_c/2

# Converting to radians
sample_a = [math.radians(i) for i in sample_a]
sample_b = [math.radians(i) for i in sample_b]
sample_c = [math.radians(i) for i in sample_c]

# Taking Sin
a_sin = np.sin(sample_a)
b_sin = np.sin(sample_b)
c_sin = np.sin(sample_c)



# Normalising the squares
a_div = [i**2/a_sin[0]**2 for i in a_sin]
b_div = [i**2/b_sin[0]**2 for i in b_sin]
c_div = [i**2/c_sin[0]**2 for i in c_sin]

# Multiplying to obtain Ni (smallest  possible integer value)
a_div = 2*a_div # Since we get a 7
b_div = 3*b_div
c_div = 3*c_div

# Finding the {m1, m2, m3} 


# Finding lattice constant

def get_lattice_constant(wavelength, angle, m1, m2, m3):
    """ Takes angle in radians """
    return (wavelength / (2 * math.sin((angle)))) * math.sqrt(m1^2 + m2^2 + m3^2)
