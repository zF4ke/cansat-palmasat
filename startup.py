import serial
import time
import sys
import os

sys.path.append(os.path.join(sys.path[0], 'BMP388'))

from BMP388 import read_values as bmp

def initMsg():
    uart = serial.Serial(port='/dev/ttyS0', baudrate=9600)

    try:
        uart.write(str.encode('*** Starting ***\n'))
    except:
        print('Something went wrong when writing to the serial port')

    time.sleep(3)

def startBMP():
    try:
        uart.write(str.encode('\n\n: BMP388 is running.\n\n'))
    except:
        print('Something went wrong when writing to the serial port')


    while True:
        bmp.run()

        time.sleep(0.1)

if __name__ == '__main__':
    initMsg()
    startBMP()
    
