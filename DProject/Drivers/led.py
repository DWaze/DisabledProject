import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def setup():
    GPIO.setup(24,GPIO.OUT)

def changeOn():
    GPIO.output(24, GPIO.HIGH)
    print("LED on")


def changeOff():
    print("LED off")
    GPIO.output(24,GPIO.LOW)