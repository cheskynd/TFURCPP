# Authors: Ndizeye Tschesquis, Blade Hicks, Nancy Landeros
from pyfirmata import Arduino, util
import time


board = Arduino('/dev/ttyACM1')
#Analog Pins
Lsen = board.analog[1]
Lsen1 = board.analog[3]
temp = board.analog[2]

#Analog Reads
tempRead = 0
tempsens = 0
LsenRead = 0
LsenRead1 = 0

#Digital Pins
LedR = board.digital[13]
LedG = board.digital[12]

#Analog setup
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
    LsenRead = LsenRead*1000
    LsenRead1 = LsenRead1*1000
    tempRead = tempsens*1000
    
    #The follows equations are used to calculate the temperature in Celcius
    tempRead = tempRead/1024
    tempRead = tempRead*5
    tempRead = tempRead-0.5
    tempRead = tempRead * 100
    

    if tempRead > 22:
        if LsenRead > LsenRead1 and LsenRead > 500:
            LedR.write(1)
            LedG.write(0)
        elif LsenRead < LsenRead1 and LsenRead1 > 500:
            LedG.write(1)
            LedR.write(0)
        else:
            LedG.write(0)
            LedR.write(0)

    
    
        
        


        
    


