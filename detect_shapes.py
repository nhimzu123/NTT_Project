import cv2 as cv


image = cv.imread('shapes.png')
image = cv.imshow('window', image)
cv.waitKey(0)
cv.destroyAllWindows()