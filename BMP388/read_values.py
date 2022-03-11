import bmp388library
import time
from datetime import datetime

bmp = bmp388library.DFRobot_BMP388_I2C(0x77)

while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    try:
        temperature = bmp.readTemperature()
        pressure = bmp.readPressure()

        output = f"T: {temperature} | P: {pressure}"

        f = open("bmp_storage.txt", "a+")

        try:
            f.write(f'dt_string {output}\n')
        except:
            print('Something went wrong when writing to the file')
        finally:
            f.close()

        print(output)

    except:
        print("An exception occurred")

        time.sleep(1)
