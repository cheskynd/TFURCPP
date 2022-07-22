# Supervisor/Professor: Dr. Jasmine Jones
# Authors: Ndizeye Tschesquis, Blade Hicks, Nancy Landeros

import cv2 as cv
import glob
import os
import random
import numpy as np
from gpiozero import MCP3008
from screeninfo import get_monitors

# This constant make the window full screen.
cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
width = get_monitors()[0].width
height = get_monitors()[0].height

# This is the circuit setup
tempSens = MCP3008(0)
light_sens1 = MCP3008(2)
light_sens2 = MCP3008(1)


def get_photo(photo):
    """
    Gets photo and resizes and returns the resized photo.
    :param photo: Image address as a string
    :return: Resized Photo
    """
    img = cv.imread(photo)
    img = cv.resize(img, (width, height))
    return img


def translate(img, x=0, y=0):
    """
    This function translates an image by moving it on the X or Y-Axis
    :param img: Image to be translated
    :param x: Value to move image across the X-axis
    :param y: Value to move image across the Y-axis
    :return: The translated image
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


def overlay(img, alpha, overlay_width, overlay_height):
    """
    This function modifies the transparency of an image
    :param img: Image used to add transparency
    :param alpha: transparency level of the overlay
    :param overlay_width: The width of the overlay
    :param overlay_height:The height of the overlay
    :return: An overlaid image
    """
    overlay = img.copy()
    output = img.copy()
    cv.rectangle(overlay, (0, 0), (overlay_width, overlay_height), (0, 0, 0), -1)
    cv.addWeighted(overlay, alpha, img, 1 - alpha, 0, output)
    return output


def show_translated_img():
    """
    This functions shows the translated image
    :return: None
    """
    translated_photo = translate(photo, rightSens_Var, leftSens_Var)
    cv.imshow('window', translated_photo)
    cv.waitKey(50)


if __name__ == '__main__':
    # get_photo things
    path = "/home/pi/Desktop/TFURCPP-main/test_imgs"  # This is a folder with the images that are used in this program.
    filenames = glob.glob(os.path.join(path, "*"))

    photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])

    # The alpha values below are used to set the transparency level of the images
    # The Key is the temperature and the Value is the alpha value
    alphas = {70: 0,
              69: .1,
              68: 0.2,
              67: 0.3,
              66: 0.4,
              65: 0.5,
              64: 0.6,
              63: 0.7,
              62: 0.8,
              61: 0.9,
              60: 1.0}
    # These are the initial sensor values
    initial_sens_val1 = light_sens1.value * 1000
    initial_sens_val2 = light_sens2.value * 1000

    # this if statement will set the values for a low light environment
    if initial_sens_val1 < 100:
        start_val = 200
        flicker_val = 310
        change_img_val = 350

    # this if statement will set the values for a medium light environment
    elif 100 < initial_sens_val1 < 200:
        start_val = 250
        flicker_val = 350
        change_img_val = 375
    # this if statement will set the values for a high lighting environment
    elif 200 < initial_sens_val1:
        start_val = 290
        flicker_val = 350
        change_img_val = 375

    while True:
        # All sensor values are scaled by 1000
        light_sens1_val = light_sens1.value * 1000
        light_sens2_val = light_sens2.value * 1000
        temp_value = (((((tempSens.value * 1000) / 1024) * 5) - 0.5) * 100)

        translated_photo = translate(photo)
        print(temp_value, light_sens1_val, light_sens2_val)
        if temp_value > 70:

            # Display an image if light_sens1_val and light_sens2_val are equal of greater that then start_val
            if light_sens1_val >= start_val or light_sens2_val >= start_val:
                # Displays window and image.
                cv.imshow('window', translated_photo)
                cv.waitKey(50)

            # flicker the image on the X-axis if light_sens1_val is between the flicker_val and change_img_val
            if flicker_val < light_sens1_val < change_img_val:
                leftSens_Var = 0
                rightSens_Var = random.randint(-17, 17)
                show_translated_img()

            # flicker the image on the Y-axis if light_sens2_val is between the flicker_val and change_img_val
            if flicker_val < light_sens2_val < change_img_val:
                rightSens_Var = 0
                leftSens_Var = random.randint(-17, 17)
                show_translated_img()

            # change the image if the light sensor values are above the change_img_val value
            if change_img_val < light_sens1_val or change_img_val < light_sens2_val:
                photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
                cv.imshow('window', translated_photo)
                cv.waitKey(10)

        # This will iterate through the Images once the candle is turned off without any overlay
        if temp_value > 70 and light_sens1_val < start_val and light_sens2_val < start_val:
            photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
            cv.imshow('window', translated_photo)
            cv.waitKey(10)

        # This will iterate through the Images once the candle is turned off with overlay as long as the temperature
        # is between 55 and 60
        if 60 < temp_value < 70 and start_val > light_sens1_val and start_val > light_sens2_val:
            int_temp_value = int(temp_value)  # coverts temperature to integer value
            photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
            overlaid = overlay(translated_photo, alphas[int_temp_value], overlay_width=width, overlay_height=height)
            cv.imshow('window', overlaid)
            cv.waitKey(10)

        # If the temperature value is below 60: a black screen will be shown
        if temp_value < 60:
            overlaid = overlay(translated_photo, 1, overlay_width=width, overlay_height=height)
            cv.imshow('window', overlaid)
            cv.waitKey(10)
