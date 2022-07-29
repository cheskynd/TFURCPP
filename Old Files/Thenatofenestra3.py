import cv2 as cv
import glob
import os
import random
import time
import numpy as np
from gpiozero import MCP3008
from gpiozero import PWMLED
from screeninfo import get_monitors


# This constant make the window full screen.
cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
width = get_monitors()[0].width
height = get_monitors()[0].height

#This is the circuit setup

X_light_sens = MCP3008(2)
Y_light_sens = MCP3008(1)
led = PWMLED(21)

def get_photo(photo):
    """
    Gets photo and resizes and returns the resized photo.
    :param photo: Image address as a string
    :return: img
    """
    img = cv.imread(photo)
    img = cv.resize(img, (width, height))
    return img


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


def overlay(img, alpha, x_size, y_size):
    overlay = img.copy()
    output = img.copy()
    cv.rectangle(overlay, (0, 0), (x_size, y_size), (0, 0, 0), -1)
    cv.addWeighted(overlay, alpha, img, 1 - alpha, 0, output)
    return output

def show_translated_img():
    translated_photo = translate(photo, rightSens_Var, leftSens_Var)
    cv.imshow('window', translated_photo)
    cv.waitKey(50)
    
def get_filename():
    return filenames[random.randint(0, len(filenames) - 1)]

if __name__ == '__main__':
    # get_photo things
    path = "/media/pi/UBUNTU 20_0/test_imgs"    
    filenames = glob.glob(os.path.join(path, "*"))
    rightSens_Var = 0
    leftSens_Var = 0
    # Functions calls
    photo = get_photo(get_filename())
    alphas = {0:0,
              1:.1,
              2:0.2,
              3:0.3,
              4:0.4,
              5:0.5,
              6:0.6,
              7:0.7,
              8:0.8,
              9:0.9,
              10:1.0}
    time_eclipsed = 0
    while True:
        X_value = X_light_sens.value * 1000

        Y_value = Y_light_sens.value * 1000

        translated_photo = translate(photo, 0, 0)

        # Conditions for the X sensor
        if X_value >= 40 or Y_value >= 40:
            time_eclipsed = 0
            # Displays window and image.
            cv.imshow('window', translated_photo)
            cv.waitKey(50)

        if 45 < X_value < 180:
            rightSens_Var = random.randint(-17, 17)
            show_translated_img()
            
        if 45 < Y_value < 180:
            leftSens_Var = random.randint(-17, 17)
            show_translated_img()


        if 180 < X_value or 180 < Y_value:
            photo = get_photo(get_filename())
            cv.imshow('window', translated_photo)
            cv.waitKey(10)

        # This will iterate through the Images once the candle is turned of with overlay as long as the temperature is between 55 and 60
        start_time = time.time()
        while 30 > X_value and 30 > Y_value and time_eclipsed < 10:
            print(X_value,Y_value, "\n")
            photo = get_photo(get_filename())
            overlaid = overlay(photo, alphas[int(time_eclipsed)], x_size=width, y_size=height)
            cv.imshow('window', overlaid)
            cv.waitKey(1)
            
            end_time = time.time()
            time_eclipsed = end_time-start_time
            
             
        
        black_img = get_photo("/home/pi/Desktop/black_img.jpg")
        cv.imshow('window',black_img)
        cv.waitKey(1)
            


                
                
