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

#This is the circuit setup
tempSens = MCP3008(0)
# tempSens = W1ThermSensor() 
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

if __name__ == '__main__':
    # get_photo things
    path = "/home/pi/Desktop/TFURCPP-main/test_imgs"    
    filenames = glob.glob(os.path.join(path, "*"))
    r = random.randint(0, len(filenames) - 1)

    # Functions calls
    photo = get_photo(filenames[r])
    alphas = {60:0,
              59:.1,
              58:0.2,
              57:0.3,
              56:0.4,
              55:0.5,
              54:0.6,
              53:0.7,
              52:0.8,
              51:0.9,
              50:1.0}

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

        temp_value = (((((tempSens.value * 1000)/1024)*5)-0.5)*100)

        translated_photo = translate(photo, rightSens_Var, leftSens_Var)
        print(temp_value,X_value, Y_value)
        if temp_value > 60:
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

#            if 400 > X_value and 400 < Y_value:
#                photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
#                cv.imshow('window', translated_photo)
                #cv.waitKey(300)

        # This will iterate through the Images once the candle is turned of without any overlay
        if  temp_value > 60 and X_value < 30 and Y_value < 30:
            print(temp_value)

            photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
            cv.imshow('window', translated_photo)
            cv.waitKey(10)
            
        # This will iterate through the Images once the candle is turned of with overlay as long as the temperature is between 55 and 60
        if  50 < temp_value < 60 and 30 > X_value and 30 > Y_value:
      
            int_temp_value = int(temp_value) # coverts temperature to integer value
            
            photo = get_photo(filenames[random.randint(0, len(filenames) - 1)])
            
            overlaid = overlay(translated_photo, alphas[int_temp_value], x_size=width, y_size=height)
            
            cv.imshow('window', overlaid)
            cv.waitKey(10)
            
        # Close the program once temperature is below 55
#        if  temp_value <= 54.99:
#            cv.destroyAllWindows()
        

# todo: Fix the random error
