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
    cv.rectangle(overlay, (0,0), (x_size,y_size), (0,0,0), -1)
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
        rightSens_Var = random.randint(-10, 10)
        leftSens_Var = random.randint(-10, 10)
        alpha = random.random()
        translated_photo = translate(photo, rightSens_Var, leftSens_Var)
        overlaid = overlay(translated_photo, alpha, x_size=1466, y_size=868)

        # Displays window and image.
        cv.imshow('window', overlaid)
        cv.waitKey(500)
