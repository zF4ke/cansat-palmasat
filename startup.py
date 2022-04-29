from multiprocessing import Process
import serial
import time
import sys
import os
from picamera import PiCamera

sys.path.append(os.path.join(sys.path[0], 'BMP388'))

from BMP388 import read_values as bmp

sys.path.append(os.path.join(sys.path[0], 'MPU6050'))

from MPU6050 import angle_o_meter

sys.path.append(os.path.join(sys.path[0], 'Camera'))

from Camera import camera

#sys.path.append(os.path.join(sys.path[0], 'Buzzer'))

#from Buzzer import buzz

uart = serial.Serial(port='/dev/ttyS0', baudrate=9600)

def initMsg():
    try:
        uart.write(str.encode('*** Starting ***\n\n'))
    except:
        print('Something went wrong when writing to the serial port')

def startBMP():
    try:
        uart.write(str.encode(': BMP388 is running.\n\n'))
    except:
        print('Something went wrong when writing to the serial port')

    while True:
        bmp.run()

        time.sleep(0.5)


def startBuzzer():
    buzz.play()

    try:
        uart.write(str.encode(': Buzzer is running.\n'))
        uart.write(str.encode(': piiiiiiiiiiiiiiiii.\n'))
    except:
        print('Something went wrong when writing to the serial port')


def startCamera():
    try:
        uart.write(str.encode(': Camera is running.\n\n'))
    except:
        print('Something went wrong when writing to the serial port')

    while True:
        x, y = angle_o_meter.get_angles()
        print(f"x: {x}")
        print(f"y: {y}")

        x_min=-12
        x_max=22

        y_min=-12
        y_max=22

        if (x_min < x < x_max) and (y_min < y < y_max):
        	camera.capture() 

        time.sleep(3)

def enableCommands():  
    try:
        uart.write(str.encode(': Commands enabled.\n'))
    except:
        print('Something went wrong when writing to the serial port')

    while True:
        command = (uart.read(8)).decode('utf-8')

        if 'ping' in command:
            uart.write(str.encode('<> Pong! </>\n'))

        if 'sbmp' in command:
            (Process(target=startBMP)).start()

        if 'scam' in command:
            (Process(target=startCamera)).start()

        if 'buzz' in command:
            (Process(target=startBuzzer)).start()


if __name__ == '__main__':
    initMsg()
    enableCommands()
    

