
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os

Rows = []

def get_all_images(path):

    for filename in os.listdir(path):
        img = cv2.imread(path + "\\" + filename[:-4] + '.JPG')  
        # Convert the image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img[1200:3300, 1800:3450]
        
        #plot_intensity_avg(img, filename[:-4], save_image=True)
        #plt.imshow(img)
        #plt.show()
        # I reckon make a dataframe to handle that kind of data, its genuinely super dimensional
        Rows.append(img.mean(axis=1))
        
        
            

def show_image(img):
    cv2.imshow("Converted Image",img)
    # waiting for key event
    cv2.waitKey(0)
    # destroying all windows
    cv2.destroyAllWindows()

def plot_intensity_avg(img, filename, save_image=False):    
    # Average column and rows left to right
    cols = img.mean(axis=0)
    # Bottom to top
    rows = img.mean(axis=1)

    # Plot histogram
    f, ax = plt.subplots(2, 1)
    ax[0].plot(cols)
    ax[1].plot(rows)
    if save_image:
        plt.savefig("10deg_results\{}.png".format(filename))
    else:
        plt.show()
    plt.close()

def clean_image(img, min_val=0.5):
    
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] < min_val:
                img[i][j] = 0

    return img

def resize_image(img, scale_percent):

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


if __name__ == "__main__":

    # Read the image
    #img = cv2.imread("data5.jpg", -1)
    # Convert the image to grayscale
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #plot_intensity_avg(img)

    path = r"C:\Users\Parv\Documents\University\Lab\quantum eraser\finalrun10deg\finalrun10deg\DATA_12522"
    get_all_images(path)


# Now we store all them and find the mutual information between them
