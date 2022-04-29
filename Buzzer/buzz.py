import RPi.GPIO as GPIO
import time

import asgore
import rickroll
import wideputin
import megalovania
import wearenumberone

BuzzerPin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT) 
GPIO.setwarnings(False)

global Buzz 
Buzz = GPIO.PWM(BuzzerPin, 440) 

def play():
    Buzz.start(50) 

    while True:
        asgore.play(Buzz)
        rickroll.play(Buzz)
        wideputin.play(Buzz)
        megalovania.play(Buzz)
        wearenumberone.play(Buzz)



