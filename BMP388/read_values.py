from datetime import datetime
import time

import bmp388library
from send_serial import write

bmp = bmp388library.DFRobot_BMP388_I2C(0x77)

def export_txt(output):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    f = open("bmp_storage.txt", "a+")

    try:
        f.write(f'{dt_string} {output}\n')
    except:
         print('Something went wrong when writing to the file')
    finally:
        f.close()

def run():
    try:
        temperature = bmp.readTemperature()
        pressure = bmp.readPressure()

        output = f"T: {temperature} P: {pressure}"

        export_txt(output)
        write(output)

    except:
        print("An exception occurred")

