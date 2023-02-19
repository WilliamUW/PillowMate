import common
import RPi.GPIO as GPIO
import time
import board
import adafruit_dht

def reed_triggered(channel):
    print(channel)

def get_reed():
    RawValue = 0
    return 9
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