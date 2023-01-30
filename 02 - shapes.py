import cv2 as cv
import numpy as np

blank  = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("Blank Image",blank)

# 1. Paint the image with a certain color
# blank[200:350,258:423] = 126,200,256
# cv.imshow("Colored Image",blank)

# pic1 = cv.imread('Photos/pic2.jpg')
# cv.imshow("Picture",pic1)

# 2. Draw a rectangle 
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),
# (255,140,125), thickness=1)
# cv.imshow("Rectangle",blank)

# 3. Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),
# radius=150,color=(0,0,255),thickness=3,lineType=1)
# cv.imshow("Circle",blank)

# 4. Draw a Line 
# cv.line(blank,(0,0),(blank.shape[1],blank.shape[0]), (255,140,125), thickness=1)
# cv.imshow("Line",blank)

# 5. Put text on an image
cv.putText(blank,"My name is KeyPat",(125,250),cv.FONT_HERSHEY_COMPLEX,1.0,(255,255,255),thickness=2)
cv.imshow("Text",blank)

cv.waitKey(0)
