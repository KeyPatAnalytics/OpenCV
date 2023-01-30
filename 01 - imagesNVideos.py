import cv2 as cv

### +++++  WORKING WITH PICTURES ++++++####
# im = cv.imread('Photos/pic1.jpg')
# cv.imshow("Great picture",im)
# cv.waitKey(0)

### +++++  WORKING WITH VIDEOS ++++++####
# capture = cv.VideoCapture('Videos/video1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video",frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

### +++++  RESIZE AND RESCALE PICTURES AND VIDEOS++++++####
def rescaleFrame(frame,scale):
    # Images, videos, live videos
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)

    dimensions = (width, heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# capture = cv.VideoCapture('Videos/video1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     rescaledFrame = rescaleFrame(frame,scale=0.6)

#     cv.imshow("Video",frame)
#     cv.imshow("Rescaled Video",rescaledFrame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


## CHANGE RESOLUTION LIVE VIDEO
def changeRes(capture,width,height):
    capture.set(3,width)
    capture.set(4,height)
