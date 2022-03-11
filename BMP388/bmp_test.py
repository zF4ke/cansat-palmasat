import bmp388library
import time
import serial

bmp = bmp388library.DFRobot_BMP388_I2C(0x77)

while True:
    test = bmp.readAltitude()
    
    print(test)

    time.sleep(1)
