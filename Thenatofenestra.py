# Authors: Ndizeye Tschesquis, Blade Hicks, Nancy Landeros
from pyfirmata import Arduino, util
import time
import cv2
import glob
import numpy as np

board = Arduino('COM4')
path = glob.glob("C:/Users/Makerspace BC/Pictures/Camera Roll/*.jpg")
images1 = []

# Analog Pins
Lsen = board.analog[1]
Lsen1 = board.analog[3]
temp = board.analog[2]

# Analog Reads
tempRead = 0
tempsens = 0
LsenRead = 0
LsenRead1 = 0

# Digital Pins
LedR = board.digital[13]
LedG = board.digital[12]

# Analog setup
it = util.Iterator(board)
it.start()

while True:
    Lsen.enable_reporting()
    temp.enable_reporting()
    Lsen1.enable_reporting()
    LsenRead = Lsen.read()
    LsenRead1 = Lsen1.read()
    tempsens = temp.read()

    ''' The inital readings are returned as NoneType so the following if statement
    will set each reading to the average reading to avoid error'''
    if type(LsenRead1) != float or type(LsenRead) != float or type(tempsens) != float:
        LsenRead = 400
        LsenRead1 = 400
        tempsens = 0.1457

    '''The Values reading from the temperature and light sensors in Python are values between 0 and 1
        so we multiply each read by 1000 to match the values retuned in the Arduino app.'''
    LsenRead = LsenRead * 1000
    LsenRead1 = LsenRead1 * 1000
    tempRead = tempsens * 1000

    # The follows equations are used to calculate the temperature in Celcius
    tempRead = tempRead / 1024
    tempRead = tempRead * 5
    tempRead = tempRead - 0.5
    tempRead = tempRead * 100

    print(tempRead)
    if tempRead > 22:
        # There is where a random picture is picked to be displayed once the temperature is greater then defined
        if LsenRead > LsenRead1 and LsenRead > 500:
            LedR.write(1)
            LedG.write(0)
        elif LsenRead < LsenRead1 and LsenRead1 > 500:
            LedG.write(1)
            LedR.write(0)
        else:
            LedG.write(0)
            LedR.write(0)

for file in path:
    img = cv2.imread(file)
    img = cv2.resize(img, (200, 200))
    images1.append(img)
    num_rows, num_cols = img.shape[:2]
    translate = np.float32([[1, 0, 70], [0, 1, 110]])
    imgtran = cv2.warpAffine(img, translate, (num_cols + 70, num_rows + 110))
    translate = np.float32([[1, 0, -30], [0, 1, -50]])
    imgtran = cv2.warpAffine(imgtran, translate, (num_cols + 70 + 30, num_rows + 110 + 50))
    cv2.namedWindow('translation', cv2.WINDOW_NORMAL)
    cv2.imshow("translation", imgtran)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
