import cv2 as cv
from PIL import Image


# load image 
image = cv.imread('images/shapes.jpg')

# image = cv.GaussianBlur(image, ksize=(7, 7), sigmaX=1)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply thesholding
_, threshold_img = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)

# using findContours() function
contours, _ = cv.findContours(threshold_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


# List for storing names of shapes

for contour in contours[1:]:
    # here we are ignoring the first contour because 
    # findcontour function detects whole image as shape, so start with 1
    
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv.approxPolyDP(contour,
                             0.01 * cv.arcLength(contour, True), True)

    # using drawContours() function
    cv.drawContours(image, [contour], 0, (252, 219, 3), 4)

    # finding center point of shape 
    M = cv.moments(contour)  # cv.moments() function calculates all the centroid, area of object, shape, etc.

    center_point = None

    if M['m00'] != 00:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        center_point = (x, y)
    
    # putting shape name at center of each shape
    if len(approx) == 3:
        cv.putText(image, 'Triangle', center_point, cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)
    elif len(approx) == 4:
        cv.putText(image, 'Rectangle', center_point, cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv.putText(image, 'Pentagon', center_point, cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)
    elif len(approx) == 6:
        cv.putText(image, 'Hexagon', center_point, cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)
    elif len(approx) == 8:
        cv.putText(image, 'Octagon', center_point, cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)
    else:
        cv.putText(image, 'Circle', center_point, cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)

# image_data = Image.fromarray(image)
# image_data.save("images/detected_shapes.jpg")

cv.imshow('Detected shapes', image)
cv.waitKey(0)
cv.destroyAllWindows()