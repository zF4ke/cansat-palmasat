import serial
import time

uart = serial.Serial(port='/dev/ttyS0', baudrate=9600)

def write(s):
    try:
        uart.write(str.encode(s))
    except:
        print('Something went wrong when writing to the serial port')

