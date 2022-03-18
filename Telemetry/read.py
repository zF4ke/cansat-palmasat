import serial
import time

uart = serial.Serial(port='/dev/ttyS0', baudrate=9600)

while True:
    print(uart.read(8))

    #time.sleep(1)

