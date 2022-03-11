from picamera import PiCamera
from time import sleep

name = input("Digita o nome da foto que vais tirar: ")
print("Tirando a foto em 5 segundos..")

sleep(5)

camera = PiCamera()

camera.start_preview()
camera.capture(f'./image_{name}.jpg')
camera.stop_preview()
