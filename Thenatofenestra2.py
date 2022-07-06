import cv2 as cv
import glob
import os
import random
import numpy as np
from gpiozero import MCP3008
from gpiozero import PWMLED
from screeninfo import get_monitors

# This constant make the window full screen.
cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
width = get_monitors()[0].width
height = get_monitors()[0].height

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


if __name__ == '__main__':
    # get_photo things
    path = "/media/pi/UBUNTU 20_0/test_imgs"    
    filenames = glob.glob(os.path.join(path, "*"))
    r = random.randint(0, len(filenames) - 1)

    # Functions calls
    photo = get_photo(filenames[r])

    while True:
        # To be modified later with sensor outputs
        tempRead = 26
        LsenRead = random.randint(300, 800)
        LsenRead1 = random.randint(300, 800)
        rightSens_Var = random.randint(0, 0)
        leftSens_Var = random.randint(0, 0)
        alpha = random.random()
        ###############################################
                
        X_value = X_light_sens.value * 1000

        Y_value = Y_light_sens.value * 1000

        temp_value = (((((tempSens.value * 1000)/1024)*5)-0.5)*100)

        translated_photo = translate(photo, rightSens_Var, leftSens_Var)
        overlaid = overlay(translated_photo, alpha, x_size=width, y_size=height)
        print(LsenRead)
        if temp_value > 25:
            # Conditions for the X sensor
            if X_value >= 300 or Y_value >= 300:
                # Displays window and image.
                cv.imshow('window', translated_photo)
                cv.waitKey(50)

            if 350 < X_value < 500:
                rightSens_Var = random.randint(-10, 10)
                translated_photo = translate(photo, rightSens_Var, leftSens_Var)
                cv.imshow('window', translated_photo)
                cv.waitKey(50)
                print(LsenRead)
                
            if 350 < Y_value < 500:
                leftSens_Var = random.randint(-17, 17)
                translated_photo = translate(photo, rightSens_Var, leftSens_Var)
                cv.imshow('window', translated_photo)
                cv.waitKey(50)
                
            if 501 < X_value < 640 or 501 < Y_value < 640:
                photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
                cv.imshow('window', translated_photo)
                cv.waitKey(50)
                print("get New image")

            if 641 < X_value < 800:
                cv.imshow('window', overlaid)
                cv.waitKey(50)

# todo: Fix the random error
