
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2


def show_image(img):
    cv2.imshow("Converted Image",img)
    # waiting for key event
    cv2.waitKey(0)
    # destroying all windows
    cv2.destroyAllWindows()

def plot_histogram(img):
    # configure and draw the histogram figure
    histogram, bin_edges = np.histogram(img, bins=256, range=(0, 1))
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixel count")
    
    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.show()


def plot_hist(img):
    plt.hist(img.ravel(),256,[0,256]); plt.show()

img = cv2.imread("data3.jpg", -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

print('Original Dimensions : ',img.shape)
 
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

"""
img = NormalizeData(resized) 
plt.plot(img)
plt.show()
"""

# Get all the rows of the image in a 1d array
x = []
st = []
for i in range(0,img.shape[0],75):
    st.append(img[i][::75])


plt.title("Single Slit Pattern obtained on adding a Polariser")
plt.plot(st)
plt.show()
