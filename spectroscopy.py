
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

data = fits.open('data.fits')

min_temp = 6000
max_temp = 7500
ksel = np.logical_and(data[1].data['INPUT_TEFF'] > min_temp, data[1].data['INPUT_TEFF'] < max_temp)
kstars = data[1].data[ksel]

def plot_temperature():
    plt.hist(kstars["INPUT_TEFF"],bins=100)
    plt.title("Teff")
    plt.show()

goodspec = fits.open('spectrum_data.fits')[1].data

def plot_spectrum(n):

    visits = goodspec['MANGAID']==kstars[n]['MANGAID']
    temp = kstars[n]['INPUT_TEFF']
    wl = goodspec[visits]['WAVE'][0]
    flux = goodspec[visits]['FLUX'][0]
    plt.plot(wl,flux)
    plt.axvline(3950, color='g', label = "Ionized Calcium", linewidth = 0.4)
    plt.axvline(4850, color='b', label = "Hydrogen Beta", linewidth = 0.4)
    plt.axvline(4340, color= 'red', label = "Hydrogen Gamma", linewidth = 0.4)
    plt.ylabel("flux (1e-17 erg/s/cm$^2$/Angstrom")
    plt.xlabel("wavelength (Angstroms)")
    plt.title("Spectrum for F class {} at {:.0f}K".format(kstars[n]['MANGAID'] , temp))
    plt.legend()
    plt.show()

plot_spectrum(23)
