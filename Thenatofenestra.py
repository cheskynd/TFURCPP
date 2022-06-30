# Supervisor/Professor: Dr. Jasmine Jones
# Authors: Ndizeye Tschesquis, Blade Hicks, Nancy Landeros
#from pyfirmata import Arduino, util
import time
import cv2
import glob
import numpy as np
import random
import os
import cv2 as cv

#
#board = Arduino('/dev/cu.usbmodem1101')

# Analog Pins
# temp = board.analog[1]  # temperature Sensor
# Lsen = board.analog[2]  # Light Sensor
# Lsen1 = board.analog[3]  # Light Sensor

# Analog Reads
# tempRead = 0
# tempSens = 0
# LsenRead = 0
# LsenRead1 = 0

# Analog setup
# it = util.Iterator(board)
# it.start()

while True:

    # Lsen.enable_reporting()
    # temp.enable_reporting()
    # Lsen1.enable_reporting()
    # LsenRead = Lsen.read()
    # LsenRead1 = Lsen1.read()
    # tempsens = temp.read()

    ''' The initial readings are returned as NoneType so the following if statements forces the program to
    run only when the reading no longer return NoneType values.'''
    # if type(LsenRead1) == float and type(LsenRead) == float and type(tempsens) == float:
    #
    #     '''The Values reading from the temperature and light sensors in Python are values between 0 and 1
    #         so we scale by multiplying each read by 1000 to match the values returned in the Arduino app.'''
    #     LsenRead = LsenRead * 1000
    #     LsenRead1 = LsenRead1 * 1000
    #     tempRead = tempsens * 1000
    #
    #     # The following equations are used to calculate the temperature in Celcius. The initial readings are voltage
    #     tempRead = tempRead / 1024
    #     tempRead = tempRead * 5
    #     tempRead = tempRead - 0.5
    #     tempRead = tempRead * 100

        test = 30
        if test > 25: #tempRead
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
                img_resized = cv.resize(path, (400, 400))   # initial units (1466, 868)
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

                # ToDo: add another if statement for a higher LsenRead value to change the image
                if LsenRead - LsenRead1 >= 10 and LsenRead > 400:
                    process(random.randint(0, len(filenames)))
                pass

            elif LsenRead1 - LsenRead >= 10 and LsenRead1 > 300:
                # ToDO: Add code that will move the image left(right)
                xvar = xvar + random.randint(-10, 10)
                #yvar = yvar + random.randint(-10, 10)
                cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
                cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
                cv.imshow("window", translate(img_resized, xvar, yvar))
                cv.waitKey(250)
                # ToDo: add another if statement for a higher LsenRead1 value to change the image
                if LsenRead1 - LsenRead >= 10 and LsenRead1 > 400:
                    process(random.randint(0, len(filenames)))
                pass
            else:
                # ToDo: add code that will return the image back to it initial location
                print(str(tempRead) + '\n')
        else:
            # ToDo: add code that will cycle the images and increase transperancy
            path = "C:/Users/Makerspace BC/Pictures/Saved Pictures"
            filenames = glob.glob(os.path.join(path, "*"))
            def process(photo):
                img = cv2.imread(filenames[photo])
                cv2.imshow("Slideshow", img)
                if cv2.waitKey(1000) == ord('q'):
                    return
            i = 5
            while i > 0:
                i -= 1
                process(random.randint(0, len(filenames)))
