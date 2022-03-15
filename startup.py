sys.path.append(os.path.join(sys.path[0], 'BMP388'))

from BMP388 import read_values as bmp

import serial
import time
import sys
import os

def initMsg():
    uart = serial.Serial(port='/dev/ttyS0', baudrate=9600)

    try:
        uart.write(str.encode('*** Starting ***'))
    except:
        print('Something went wrong when writing to the serial port')

def startBMP():

    while True:
        bmp.run()

        time.sleep(0.1)

if __name__ == '__main__':
    initMsg()
    
