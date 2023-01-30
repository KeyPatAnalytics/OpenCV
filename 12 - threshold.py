import cv2 as cv


img = cv.imread('Photos/pic7.jpg')
cv.imshow('Original',img)


# Gray image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Thresholding is used to binarize an image

# 1. Simple thresholding
threshold, thresh = cv.threshold(gray,175,255,cv.THRESH_BINARY)
# pixel > 175 ===> pixel = 255
# pixel < 175 ===> pixel = 0
cv.imshow('Simple threshold',thresh)

# Inverse thresholding
ithreshold, ithresh = cv.threshold(gray,175,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse threshold',ithresh)


# 2. Adaptive threshold
# we can indicate the opptimal threshold value
# Or let the computer find the optimal an use it

# adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,15,-5)
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,15,-5)

cv.imshow('Adaptive Threshold',adaptive_thresh)


cv.waitKey(0)
