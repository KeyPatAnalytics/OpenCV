import cv2 as cv
import numpy as np

img = cv.imread("Photos/pic9.jpg")
cv.imshow("Original",img)

# BLURRING OR SMOOTHING TEND TO REMOVE NOISE 
# OF LIGHTENING OR SENSORS FROM A PICTURE

# DIFFERENT TYPE OF SMOOTHING

# 1. AVERAGE
average = cv.blur(img, (3,3))
cv.imshow("Average",average)

# 2. Gaussian blurring
#  It adds weights to pixels around the central one
gauss = cv.GaussianBlur(img,(3,3),sigmaX=0)
cv.imshow('Gaussian Blur',gauss)

# 3. Median Blur
# In many projects, it is the preferred smoothing method
median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)

# THe most effective method
# Bi lateral method
bilateral = cv.bilateralFilter(img,5,10,25)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)
