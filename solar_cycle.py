# Reading an excel file using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Give the location of the file
loc = "solar.xlsx"
 

df = pd.read_excel(loc)

year = np.arange(1951,2021)

def yearlyAverage(column_name):
    
    prev_year = 1951
    sum_vals = 0
    num_vals = 0
    yearly_average = []
    
    for i in range(len(df['Date'])):
        if df['Date'][i].year == prev_year:
            sum_vals += df[column_name][i]
            num_vals +=1
        else:
            yearly_average.append(sum_vals/num_vals)
            num_vals = 0
            sum_vals = 0
            prev_year = prev_year + 1
    
    yearly_average.append(sum_vals/num_vals)

    return yearly_average




f30 = yearlyAverage('f30')
f15 = yearlyAverage('f15')
f10 = yearlyAverage('f10.7')
f8 = yearlyAverage('f8')
f3 = yearlyAverage('f3.2')



plt.plot(year, f30, label = 'f30')
plt.plot(year, f15, label = 'f15')
plt.plot(year, f10, label = 'f10.7')
plt.plot(year, f8, label = 'f8')
plt.plot(year, f3, label = 'f3.2')
plt.title("Flux vs year")
plt.show()
