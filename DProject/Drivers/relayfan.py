import logging
import traceback

import RPi.GPIO as GPIO
import time

RelayPin = 21

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RelayPin, GPIO.OUT)
    return True

def changeOn():
    print('relay On...')
    GPIO.output(RelayPin, GPIO.LOW)
    return True

def changeOff():
    print('relay Off...')
    GPIO.output(RelayPin, GPIO.HIGH)
    return True

def destroy():
    GPIO.cleanup()
