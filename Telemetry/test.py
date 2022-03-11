import RPi.GPIO as GPIO
import time
import serial

filename = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)

uart = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)

GPIO.output(18, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(18, GPIO.LOW)
time.sleep(0.5)

uart.write('Hi')
