
import numpy as np
import matplotlib.pyplot as plt

# Modelling the single slit diffraction pattern and the double slit interference pattern as sinc functions


t = np.linspace(-4, 4, 41)

f = np.sinc(t)
g = 6 * f

plt.plot(t, f)
plt.plot(t, g)
plt.show()


