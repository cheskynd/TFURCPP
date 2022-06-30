import cv2
import glob
import numpy as np
import random
import os
import cv2 as cv

##testing the first if statement from ThenatoFenestra

while True:
    test = 30
    LsenRead = 400
    LsenRead1 = 10
    if test >25:
        # ToDo: There is where a random picture is picked to be displayed once the temperature is greater then defined
        path = "C:/Users/Makerspace BC/Pictures/Saved Pictures"
        filenames = glob.glob(os.path.join(path, "*"))
        def process(photo):
            img = cv2.imread(filenames[photo])
            cv2.imshow("Slideshow", img)
            if cv2.waitKey(0) == ord('q'):
                return
        i = 5
        while i > 0:
            i -= 1
            process(random.randint(0, len(filenames)))

            if LsenRead - LsenRead1 >= 10 and LsenRead > 300:
                # ToDo: Add code that will move the image up(down)
                #path = "C:/Users/Makerspace BC/Pictures/Saved Pictures"
                img_resized = cv.resize(process(photo=len(path)), (400, 400))  # initial units (1466, 868)
                def translate(img, x, y):
                    transMat = np.float32([[1, 0, x], [0, 1, y]])
                    dimensions = (img.shape[1], img.shape[0])
                    return cv.warpAffine(img, transMat, dimensions)
                xvar = 0
                yvar = 0
                while True:
                    # xvar = xvar + random.randint(-10, 10)
                    yvar = yvar + random.randint(-10, 10)
                    cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
                    cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
                    cv.imshow("window", translate(img_resized, xvar, yvar))
                    cv.waitKey(250)
