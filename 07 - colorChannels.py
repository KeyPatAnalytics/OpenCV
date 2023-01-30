# SPLIT AMD MERGE COLOR CHANNELS IN OPEN CV
# BGR = Blue, Green, Red === 3 channels
import cv2 as cv
import numpy as np

img = cv.imread('Photos/pic9.jpg')
cv.imshow('Original Picture',img)


# WE CREATE A BLANK(BLACK) CHANNEL
# VERY IMPORT TO ADD DATA TYPE TO UNSIGNED INT8
blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

print("Blank: ", blank.shape)
print("Blue: ",b.shape)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank, blank,r])

cv.imshow('Blue Picture',blue)
cv.imshow('Green Picture',green)
cv.imshow('Red Picture',red)


cv.waitKey(0)
