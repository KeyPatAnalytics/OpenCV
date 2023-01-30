import cv2 as cv
import numpy as np


img = cv.imread('Photos/pic1.jpg')
cv.imshow('Original',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# How to computer gradients an edge detection
#  THERE TWO METHODS
# 1. Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian gradients',lap)



# 2. SOBEL
# It computes the gradients in directions X, Y
SobelX = cv.Sobel(gray,cv.CV_64F,1,0)
SobelY = cv.Sobel(gray,cv.CV_64F,0,1)

# cv.imshow('SobelX',SobelX)
# cv.imshow('SobelY',SobelY)

combined_Sovel = cv.bitwise_or(SobelX,SobelY)
cv.imshow('Combined Sobel',combined_Sovel)

# CANNY ADGE DETECTION
# Canny uses Sobel method for gradient computation
canny = cv.Canny(gray, 150, 185)
cv.imshow('Canny',canny)


cv.waitKey(0)

