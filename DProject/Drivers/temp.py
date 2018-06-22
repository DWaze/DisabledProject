import os
import logging
import traceback

ds18b20 = ''


def setup():
    global ds18b20
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i


def read():
    #	global ds18b20
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature


def run():
    try:
        res="%0.3f C" % read()
        if read() is not None:
            print(res)
        return res
    except Exception as e:
        logging.error(traceback.format_exc())
        print(e)
        destroy()

def destroy():
    pass


if __name__ == '__main__':
    try:
        setup()
        run()
    except KeyboardInterrupt:
        destroy()