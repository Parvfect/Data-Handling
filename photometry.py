
import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
import astropy as astro

tpf = lk.search_targetpixelfile('KIC 6922244', author="Kepler", cadence="long", quarter=4).download()
#tpf.plot(title="Pixel plot of Kepler-8")
# Convert target pixel file to Lightcurve using aperture mask
lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
klc = lk.search_lightcurve("Kepler-8", author="Kepler", cadence="long", quarter=4).download()
#Plotting lightcurve
 
"""
ax = klc.plot(column='pdcsap_flux', label='PDCSAP Flux', normalize=True)
klc.plot(column='sap_flux', label='SAP Flux', normalize=True, ax=ax);
plt.title("Comparing Flux Lightcurves of Kepler-8(KIC 6922244)")
plt.show()


klc.plot(column='pdcsap_flux', label='PDCSAP Flux', normalize=True)
plt.title("PDSCAP Lightcurve of Kepler-8(KIC 6922244)")
plt.show()
"""

klc.remove_nans().flatten(window_length=401).fold(period=3.523).bin(time_bin_size=0.01).plot(title = "KIC 6922244")
plt.title("Folded Lightcurve of Kepler-8(KIC 6922244)")
plt.show()


# Converting to periodogram
pg = lc.to_periodogram(method = 'bls', minimum_period=2.0)

import astropy.units as u
print(pg.period_at_max_power)
