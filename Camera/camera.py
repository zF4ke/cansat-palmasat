from picamera import PiCamera
from time import sleep
from datetime import datetime

def capture():
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    camera = PiCamera()
    camera.capture(f'./pictures/image_{dt_string}.jpg')
    camera.close()
