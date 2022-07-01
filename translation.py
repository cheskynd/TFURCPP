import cv2 as cv
import numpy as np
import random


img = cv.imread('C:/Users/Makerspace BC/Pictures/Saved Pictures/download.jpg')

# cv.imshow('Cat', img)
img_resized = cv.resize(img, (400,400)) #1466, 868


#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)



### SCRIPT STARTS HERE
xvar = 0
yvar = 0
while True:
    xvar = xvar + random.randint(-10, 10)
    yvar = yvar + random.randint(-10, 10)
    cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow("window", translate(img_resized, xvar, yvar))
    cv.waitKey(250)

