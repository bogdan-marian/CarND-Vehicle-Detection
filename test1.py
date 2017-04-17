import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import time
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from skimage.feature import hog


cars = []
notcars = []

#load not_cars
images = glob.glob('./training_data/non-vehicles/non-vehicles/*/*.png')
for image in images:
    notcars.append(image)
print (len(notcars))
#lead cars
images = images = glob.glob('./training_data/vehicles/vehicles/*/*.png')
for image in images:
    cars.append(image)
print (len(cars))
