import common
import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
from datetime import datetime

def reed_triggered(channel):
    with open("Awake.log","a") as af:
        af.write(str(datetime.now()))

def get_reed():
    # RawValue = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(common.REED_SENSOR, GPIO.IN)
    # RawValue = GPIO.input(common.REED_SENSOR)

    try:
        RawValue = GPIO.input(common.REED_SENSOR)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        return RawValue


def get_temp(dhtDevice):
    result = None
    try:
        temperature_c = dhtDevice.temperature
        # humidity = dhtDevice.humidity
        result = temperature_c
    except RuntimeError as error:  
            print(error.args[0])
    finally:
        return result