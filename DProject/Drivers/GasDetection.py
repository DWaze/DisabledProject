import DProject.Drivers.PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

DO = 17
Buzz = 18
GPIO.setmode(GPIO.BCM)


def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)
    GPIO.setup(Buzz, GPIO.OUT)
    GPIO.output(Buzz, 1)


def check(x):
    res = ""
    if x == 0:
        res = '{"danger":"true","prevention":"pending"}'
    return res


def detect():
    status = 1
    result = '{"danger":"false","prevention":"none"}'
    timeCount = 0
    while True:
        print(ADC.read(0))

        tmp = GPIO.input(DO)
        if tmp != status:
            result = check(tmp)
            status = tmp
        if status == 0:
            GPIO.output(Buzz, 0)
            return result
        elif timeCount == 600:
            GPIO.output(Buzz, 1)
            return result

        time.sleep(0.2)
        timeCount += 0.2


def destroy():
    GPIO.output(Buzz, 1)
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        setup()
        detect()
    except KeyboardInterrupt:
        destroy()