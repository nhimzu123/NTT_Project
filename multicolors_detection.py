import cv2 as cv
import numpy as np
from numpy.lib.twodim_base import mask_indices


####################################
# Step 1: Load image
####################################
img = cv.imread('images/shape.jpg')


####################################
# Step 2: Convert BGR to HSV
####################################
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)


####################################
# Step 3: Define the range of each color and create the corresponding mask.
####################################

# Set range for red color and define mask
red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], dtype=np.uint8)

red_mask = cv.inRange(hsv_img, red_lower, red_upper)

# Set range for green color and define mask
green_lower = np.array([25, 52, 72], dtype=np.uint8)
green_upper = np.array([102, 255, 255], dtype=np.uint8)

green_mask = cv.inRange(hsv_img, green_lower, red_upper)

# Set range for blue color and define mask
blue_lower = np.array([94, 80, 2], dtype=np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)

blue_mask = cv.inRange(hsv_img, blue_lower, blue_upper)


##########################################
# Step 4
# Morphological Transform, Dilation
# for each color and bitwisr_and operator
# between imageFrame and mask determines
# to detect only that particular color
##########################################
# Define kernel for Dilation
kernel = np.ones((5, 5), dtype=np.uint8)


# For red color
red_mask = cv.dilate(red_mask, kernel)
result_red = cv.bitwise_and(img, img, mask=red_mask)

# For green color
green_mask = cv.dilate(green_mask, kernel)
result_green = cv.bitwise_and(img, img, mask=green_mask)

# For blue color
blue_mask = cv.dilate(blue_mask, kernel)
result_blue = cv.bitwise_and(img, img, mask=blue_mask)


#######################################
# Find contours
#######################################
contours, _ = cv.findContours()