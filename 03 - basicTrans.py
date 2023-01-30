import cv2 as cv
import numpy as np

img = cv.imread('Photos/pic5.jpg')

cv.imshow("Picture",img)


# Translation
def translation(img,x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# -x / x ==> Left / right
# -y / y ==> Up / down

# translated = translation(img, 100, 100)
# cv.imshow("Translated",translated)


# ROTATION
def rotate(img, angle, rotPoint=None, scale=1.0):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,scale)

    dimensions = (width, height)

    return cv.warpAffine(img,rotMat,dimensions)


# rotated = rotate(img,180)
# rotated_rotated = rotate(rotated,180)
# cv.imshow("Rotated",rotated)
# cv.imshow("2Rotated",rotated_rotated)

# RESIZING AN IMAGE
# resized = cv.resize(img,(250,320),interpolation=cv.INTER_AREA)
# cv.imshow("Resized",resized)


# FLIP AN IMAGE
# flip = cv.flip(resized,-1)
# cv.imshow("Flip",flip)


#CROP AN IMAGE
cropped = img[200:400,300:500]
cv.imshow("Cropped",cropped)


cv.waitKey(0)