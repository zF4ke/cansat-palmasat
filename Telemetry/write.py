import serial
import time

uart = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)

message = "Hello, World!"

while message != "stop":
    message = input('')
    uart.write(str.encode(message))

    time.sleep(0.5)

