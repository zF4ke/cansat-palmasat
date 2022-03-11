import bmp388library
import time
import serial

bmp = bmp388library.DFRobot_BMP388_I2C(0x77)

while True:
    temperature = bmp.readTemperature()
    pressure = bmp.readPressure()

    print(f"T: {temperature} | P: {pressure}")

    time.sleep(1)
