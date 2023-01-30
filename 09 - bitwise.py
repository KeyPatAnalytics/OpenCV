import cv2 as cv
import numpy as np

#  BITWISE ARE USED A LOT WHEN WORKING WITH MASKS
blank = np.zeros((400,400),dtype='uint8')

# We must use copies of our blank image
# Otherwise all our modifications will be saved on the blank image
rectangle = cv.rectangle(blank.copy(),(20,20),(380,380),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Restangle',rectangle)
cv.imshow('Circle',circle)


# Bite AND --> Intersection area
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("Bite wise AND", bitwise_and)

# Bitewise OR --> the UNION area
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitewise OR",bitwise_or)

# bitewise xor --> non-intersectional areas
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitewise XOR",bitwise_xor)

# bitwise NOT
# It does not return anything, but invert color index
rectangle_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not', rectangle_not)

# Bitwise operations are important in a concept called masking


cv.waitKey(0)