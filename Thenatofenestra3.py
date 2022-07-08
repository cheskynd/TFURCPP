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
def get_random_int():
    return filenames[random.randint(0, len(filenames) - 1)]

def get_alpha(x):
    if x == 0:
        return 1.0
    
    elif x == 1:
        return 0.9
    
    elif x == 2:
        return 0.8
    
    elif x == 3:
        return 0.7
    
    elif x == 4:
        return 0.6
    
    elif x == 5:
        return 0.5

    elif x == 6:
        return 0.4
    
    elif x == 7:
        return 0.3
    
    elif x == 8:
        return 0.2
    
    elif x == 9:
        return 0.1
    
    elif x == 10:
        return 0.0
    
    
if __name__ == '__main__':
    # get_photo things
    path = "/media/pi/UBUNTU 20_0/test_imgs"    
    filenames = glob.glob(os.path.join(path, "*"))
    r = random.randint(0, len(filenames) - 1)
    time_started = False

    # Functions calls
    photo = get_photo(filenames[r])
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

    while True:
        # To be modified later with sensor outputs
        
        LsenRead = random.randint(300, 800)
        LsenRead1 = random.randint(300, 800)
        rightSens_Var = random.randint(0, 0)
        leftSens_Var = random.randint(0, 0)
#         alpha = random.random()
        ###############################################
        
        X_value = X_light_sens.value * 1000

        Y_value = Y_light_sens.value * 1000

        translated_photo = translate(photo, rightSens_Var, leftSens_Var)
        #print(X_value, Y_value)
        #if temp_value > 50:
            # Conditions for the X sensor
        if X_value >= 40 or Y_value >= 40:
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
            photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
            cv.imshow('window', translated_photo)
            cv.waitKey(10)

        # This will iterate through the Images once the candle is turned of with overlay as long as the temperature is between 55 and 60
        if 30 > X_value and 30 > Y_value:
            photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
            x = 0
            while x < 10: 
                overlaid = overlay(translated_photo, get_alpha(x), x_size=width, y_size=height)
                cv.imshow('window', overlaid)
                cv.waitKey(1)
                x+= 1

                

