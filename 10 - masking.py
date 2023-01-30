import cv2 as cv
import numpy as np

# Masking is important when for example we want to focus 
#  on a particular part of the image
# For example the faces of people

img = cv.imread('Photos/pic7.jpg')
cv.imshow('Original',img)

# We create a blank
blank = np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('Blank Image',blank)

# mask (Let's take the example of a circle)
mask1 = cv.circle(blank.copy(),(img.shape[1]//4,img.shape[0]//4 + 70),100,255,-1)
mask2 = cv.rectangle(blank.copy(),(img.shape[1]//4-85,img.shape[0]//4 - 15),
(img.shape[1]//4+85,img.shape[0]//4 + 155),255,-1)

mask3 = cv.bitwise_or(mask1,mask2)
# cv.imshow('Mask',mask3)

# Masked image
masked = cv.bitwise_and(img,img,mask=mask2)
cv.imshow("Masked image",masked)
#  The mask has to be with same shape as the image




cv.waitKey(0)
