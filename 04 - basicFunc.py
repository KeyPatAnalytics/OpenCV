import cv2 as cv

# FUNCTION TO RESCALE OUR IMAGES
def rescale(frame,scale=0.60):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

pic = cv.imread('Photos/pic1.jpg')

img = rescale(pic)
# cv.imshow("Original",img)

# # CONVERT TO GRAY
# img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",img_gray)


# To BLUR AN IMAGE = REMOVE NOISE (r)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# EDGE CASCADE (to detect the edges in the image)
# canny = cv.Canny(blur,125,175)
# cv.imshow("Canny",canny)

# Dilating the image
# dilated = cv.dilate(canny,(3,3),iterations=3)
# cv.imshow("Dilated",dilated)

# Eroding the dilated (getting back the edges)
# eroded = cv.erode(dilated,(3,3),iterations=3)
# cv.imshow("Eroded",eroded)



# RESIZE AN IMAGE
resized = cv.resize(pic, (500,500),interpolation=cv.INTER_AREA)
cv.imshow("Resized",resized)

# TO CROPE AN IMAGE
cropped = pic[500:700,400:600]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
