import DProject.Drivers.PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
from DProject.Drivers import led, relayfan

DO = 17
Buzz = 18
GPIO.setmode(GPIO.BCM)


def setup():
    ADC.setup(0x48)
    led.setup()
    relayfan.setup()
    GPIO.setup(DO, GPIO.IN)
    GPIO.setup(Buzz, GPIO.OUT)
    # GPIO.output(Buzz, 1)


def run(x):
    if x == 0:
        res = '{"danger":"false","prevention":"success"}'
        relayfan.changeOn()
        led.changeOn()
        time.sleep(3)
        led.changeOff()
        # relay.changeOff()
        return res


def prevention():
    status = 1
    count = 0
    result = '{"danger":"false","prevention":"none"}'
    timeCount = 0
    while True:
        print(ADC.read(0))

        tmp = GPIO.input(DO)
        if tmp != status:
            result=run(tmp)
            GPIO.output(Buzz, 1)
            return result
        elif timeCount == 600:
            GPIO.output(Buzz, 1)
            count = 0
            return result

        timeCount += 0.2
        time.sleep(0.2)


def destroy():
    GPIO.output(Buzz, 1)
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        setup()
        prevention()
    except KeyboardInterrupt:
        destroy()