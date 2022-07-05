import cv2 as cv
import glob
import os
import random
import numpy as np

# This constant make the window full screen.
cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)


# Variable soup


# Functions start here


def get_photo(photo):
    """
    Gets photo and resizes and returns the resized photo.
    :param photo: Image address as a string
    :return: img
    """
    img = cv.imread(photo)
    img = cv.resize(img, (1400, 800))
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
    path = "C:/Users/Makerspace BC/Pictures/Saved Pictures"
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

        translated_photo = translate(photo, rightSens_Var, leftSens_Var)
        overlaid = overlay(translated_photo, alpha, x_size=1466, y_size=868)
        print(LsenRead)
        if tempRead > 25:

            # Conditions for the X sensor
            if LsenRead >= 300 or LsenRead1 >= 300:
                # Displays window and image.
                cv.imshow('window', translated_photo)
                cv.waitKey(50)

            if 350 < LsenRead < 500:
                rightSens_Var = random.randint(-10, 10)
                translated_photo = translate(photo, rightSens_Var, leftSens_Var)
                cv.imshow('window', translated_photo)
                cv.waitKey(50)
                print(LsenRead)

            if 501 < LsenRead < 640:
                photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
                cv.imshow('window', translated_photo)
                cv.waitKey(50)
                print("get New image")

            if 641 < LsenRead < 800:
                cv.imshow('window', overlaid)
                cv.waitKey(50)


                # rightSens_Var1 = random.randint(0, 10)

            #     # todo: If Left Sensor reads 300 or above, move image left on the X-axis (x) pixels.
            # elif LsenRead > 500:
            #     pass
            #     # todo: If Left Sensor reads 500 or above, move image left on the X-axis (x) pixels.
            # elif LsenRead > 800:
            #     pass
            #     # todo: If Left Sensor reads 800 or above, it will trigger an image change.
            #
            # # Conditions for the Y sensor
            # elif LsenRead1 > 300:
            #     pass
            #     # todo: If Right Sensor reads 300 or above, move image up on the Y-axis (x) pixels.
            # elif LsenRead1 > 500:
            #     pass
            #     # todo: If Right Sensor reads 500 or above, move image up on the Y-axis (x) pixels.
            # elif LsenRead1 > 800:
            #     pass
            #     # todo: If Right Sensor reads 800 or above, it will trigger and image change.
            #
            # else:
            #     pass
