import cv2 as cv
import numpy as np

img = cv.imread('Photos/pic11.jpg')
cv.imshow("KeyPat",img)

# Convert to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GrayKeyPat",gray)

# # BLUR THE GRAY IMAGE
blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("Blur Image",blur)


# # Find the edges
canny  = cv.Canny(blur,125,175)
# cv.imshow("Canny edges",canny)

blank = np.zeros(img.shape)


ret, thresh  = cv.threshold(gray,125,255,cv.THRESH_BINARY) # We are binarizing the image
cv.imshow("Thresh",thresh)

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) are found!')


cv.drawContours(blank,contours,-1, (255,0,255),thickness = 1)
cv.imshow("Drawn contours",blank)

# WE CAN FIND THE CONTOURS USING WHETHER CANNY OR THRESHOLD METHOD
# BUT IT ALWAYS BETTER TO USE FIRST CANNY METHOD


cv.waitKey(0)
