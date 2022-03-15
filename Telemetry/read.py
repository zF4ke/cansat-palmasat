import serial
import time

uart = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)

while True:
    uart.readline()

    time.sleep(0.03)

