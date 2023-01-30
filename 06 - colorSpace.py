# HOW TO SWITCH BETWEEN COLOR SCPACES IN OPENCV (BGR, GrayScale, ...)
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/pic5.jpg')
cv.imshow("BGR image",img)

# From BGR to GrayScale
# Gray scale image provide the distribution of pixel intensity over the image
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Scale", gray)

# # BGR to HSV (Hue Saturation Value)
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# # BGR to L*a*b
# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("LAB",lab)


# OPEN CV WORKS WITH BGR COLR SPACE 
# BUT MATPLOTLIB WORKS WITH RGB SPACE
# IMPORTANT TO KNOW WHEN WORKING WITH DIFERENT LIBRARIES

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()


# We can convert from hsv, lab, grayscale to bgr

cv.waitKey(0)

