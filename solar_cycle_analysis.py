# Reading an excel file using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
import math

# Give the location of the file
loc = "solar.xlsx"
 
df = pd.read_excel(loc)
year = np.arange(1951,2021)
uncertainty_arr = []


def yearlyAverage(column_name):
    
    prev_year = 1951
    sum_vals = 0
    num_vals = 0
    maximum = 0 
    minimum = 100000
    yearly_average = []
    
    for i in range(len(df['Date'])):
        
        if df['Date'][i].year == prev_year:

            if df[column_name][i] > maximum:
                maximum = df[column_name][i]
            if df[column_name][i] < minimum:
                minimum = df[column_name][i]

            sum_vals += df[column_name][i]
            num_vals +=1
        
        else:
            yearly_average.append(sum_vals/num_vals)
            uncertainty_arr.append(((maximum - minimum) /(2 * math.sqrt(num_vals))))
            num_vals = 0
            sum_vals = 0
            maximum = 0
            minimum = 100000
            prev_year = prev_year + 1
        
            
    
    yearly_average.append(sum_vals/num_vals)

    return yearly_average


def fourier_transform(arr, name):
    arr = arr - np.mean(arr)
    N = len(arr)

    yf = rfft(arr)
    xf = rfftfreq(N, 1)

    plt.plot(xf, np.abs(yf), label = '{}'.format(name))

    return yf, xf



def find_solar_cycle(arr):
    # Find the solar cycle
    
    yf, xf = fourier_transform(arr, "")
    sorted_yf = np.sort(yf)
    index = np.where(yf == sorted_yf[-2])
    solar_cycle = 1.0/xf[index]
    print(xf[np.argmax(yf)])
    print("Solar Cycle: {}".format(solar_cycle))
        
    return solar_cycle
    

def sunspot(filename):
    
    error = []
    # Read text file
    with open(filename) as f:
        content = f.readlines()

    sunspot = []
    year = []
    for line in content:
        words = line.split()
        year.append(int(words[0][:-2]))
        sunspot.append(float(words[1]))
        error.append(float(words[1]))

    lowerLimit = year.index(1951)
    error = error[lowerLimit:]
    avg_error = np.std(error)/math.sqrt(len(error))
    total_uncertainty = avg_error #+ (np.max(error) - np.min(error))/(math.sqrt(len(error)))
    relative_uncertainty = total_uncertainty/np.mean(sunspot)
    print("Sunspot Uncertainty: {}".format(relative_uncertainty))

    return sunspot[lowerLimit:-1]

def plot_ft():
    
    fourier_transform(f10, "f10.7")
    fourier_transform(sunspot("sunspot.txt"), "Sunspot")
    
    plt.legend()
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.title("Fourier Transform of Normalised Flux and Sunspots per Year")
    plt.show()

def plot_flux_spectrum():
        
    #plt.plot(year, f30, label = 'f30')
    #plt.plot(year, f15, label = 'f15')
    sunspots = sunspot("sunspot.txt")
    plt.plot(year, sunspots, label = 'Sunspot')
    plt.plot(year, f10, label = 'f10.7')
    #plt.plot(year, f8, label = 'f8')
    #plt.plot(year, f3, label = 'f3.2')
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Flux +/- 3.7 / Sunspots +/- 8.5")
    plt.title("Comparing Solar Flux and Sunspots per Year")
    plt.show()


def predict_next_solar_maxima(arr):
    # Predict the next solar maximum
    
    # We need to find the first peak in the last 10 years, so we extract the last ten years 
    # of solar flux and find the maximum value in it, indicating the last solar maximum
    arr = arr[(len(arr) - 9):]

    # Using this, we can find the year of the last solar maximum
    index = 2010 + np.argmax(arr) 
    print("Last Solar Maximum - {}".format(index))
    
    # To find the next Solar Maximum, we add the length of the solar cycle to the last solar maximum
    print("Next Solar Maximum - {}".format(index + 10))


f30 = yearlyAverage('f30')
f15 = yearlyAverage('f15')
f10 = yearlyAverage('f10.7')
f8 = yearlyAverage('f8')
f3 = yearlyAverage('f3.2')
error = np.std(uncertainty_arr)/np.sqrt(len(uncertainty_arr))
error += np.std(f30)/np.sqrt(len(f30))
print("Uncertainty in Solar Cycle: {}".format(error))


#print("Uncertainty: {}".format(error))
# need to work out solar cycle
# need to predict next solar maxima
#plot_ft()

#sunspot = sunspot("sunspot.txt")
plot_flux_spectrum()

# / Sunspots +/- 8.5
