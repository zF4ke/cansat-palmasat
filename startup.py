from multiprocessing import Process
import serial
import time
import sys
import os

sys.path.append(os.path.join(sys.path[0], 'BMP388'))

from BMP388 import read_values as bmp

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
    try:
        uart.write(str.encode(': Buzzer is running.\n'))
        uart.write(str.encode(': piiiiiiiiiiiiiiiii.\n'))
    except:
        print('Something went wrong when writing to the serial port')


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

        if 'buzz' in command:
            startBuzzer()


if __name__ == '__main__':
    initMsg()
    startBMP()
    enableCommands()
    

