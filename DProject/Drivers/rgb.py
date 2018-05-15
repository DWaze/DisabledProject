import RPi.GPIO as GPIO
import sys
import logging
import traceback

R = 11
G = 13
B = 15


def setup(Rpin, Gpin, Bpin):
    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)  # Set pins' mode is output
        GPIO.output(pins[i], GPIO.HIGH)  # Set pins to high(+3.3V) to off led

    p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
    p_G = GPIO.PWM(pins['pin_G'], 1999)
    p_B = GPIO.PWM(pins['pin_B'], 5000)

    p_R.start(100)  # Initial duty Cycle = 0(leds off)
    p_G.start(100)
    p_B.start(100)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)  # Turn off all leds


def setColor(col):  # For example : col = 0x112233
    R_val = (col & 0xff0000) >> 16
    G_val = (col & 0x00ff00) >> 8
    B_val = (col & 0x0000ff) >> 0
    print(R_val)
    print(G_val)
    print(B_val)
    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100 - R_val)  # Change duty cycle
    p_G.ChangeDutyCycle(100 - G_val)
    p_B.ChangeDutyCycle(100 - B_val)


def ChangeColor(col):
    setColor(col)


def destroy():
    p_R.stop()
    p_G.stop()
    p_B.stop()
    off()
    GPIO.cleanup()


def run(col, pos):
    try:
        if (pos == 0):
            setup(R, G, B)
            ChangeColor(col)
        else:
            ChangeColor(col)
    except Exception as e:
        logging.error(traceback.format_exc())
        print(e)
        destroy()
