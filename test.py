import RPi.GPIO as GPIO
import time
import smbus

buzzerPin = 9
address = 0x48
bus=smbus.SMBus(1)
cmd = 0x40

def analogRead(chn):
    value=bus.read_byte_data(address,cmd+chn)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    global p 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzerPin, GPIO.OUT)
    p = GPIO.PWM(buzzerPin, 1)
    p.start(0)

def loop():
    while True:
        value = analogRead(0)
        voltage = value / 255.0 * 3.3
        print(value*3+1)
        p.changeFrequency(toneVal)
        time.sleep(0.01)

setup()
loop()