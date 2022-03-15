import serial
import time

uart = serial.Serial(port='/dev/ttyS0', baudrate=9600)

while True:
    uart.readline()

    time.sleep(0.03)

