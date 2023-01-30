import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Histograms help to visualize the distribution
#  of pixel intensity in the image

img = cv.imread('Photos/pic7.jpg')
cv.imshow('Original',img)


# HISTOGRAMS FOR GRAY IMAGES

# # Gray image
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # cv.imshow('Gray Imgae',gray)


# We create a blank
blank = np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('Blank Image',blank)

# mask (Let's take the example of a circle)
mask1 = cv.circle(blank.copy(),(img.shape[1]//4,img.shape[0]//4 + 70),100,255,-1)
mask2 = cv.rectangle(blank.copy(),(img.shape[1]//4-85,img.shape[0]//4 - 15),(img.shape[1]//4+85,img.shape[0]//4 + 155),255,-1)
mask3 = cv.bitwise_or(mask1,mask2)

# # Masked image
# masked = cv.bitwise_and(gray,gray,mask=mask1)
# cv.imshow("Masked image",masked)

# # Calculate the histogram 
# # using mask (mask = none for all the image)
# histograms = cv.calcHist([gray],[0],mask = mask1,histSize=[256],ranges=[0,256])

# # Draw the histogram
# plt.figure(figsize=(8,8))
# plt.title('Gray scale histogram')
# plt.xlim([0,256])
# plt.xlabel('Bins')
# plt.ylabel('N of pixels')

# plt.plot(histograms)
# # plt.hist(np.squeeze(gray),256,(0,256),density=False)
# plt.show()


# HISTOGRAMS FOR DIFFERENT CHANNELS

# # Masked image
masked = cv.bitwise_and(img,img,mask=mask1)
cv.imshow("Masked image",masked)


# Draw the histogram
plt.figure(figsize=(8,8))
plt.title('Colour histogram')
plt.xlim([0,256])
plt.xlabel('Bins')
plt.ylabel('N of pixels')

colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask=mask1,histSize=[256],ranges=[0,256])
    plt.plot(hist,color=col)

plt.show()


cv.waitKey(0)
