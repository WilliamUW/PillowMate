#! /usr/bin/python3
import common
import sensor
from sensor import *
import time
import time
import board
import adafruit_dht
import drivers
from time import sleep
import pytz
from datetime import datetime
import RPi.GPIO as GPIO

def main():
    return 

if __name__ == "__main__":
    # Load the driver and set it to "display"
    # If you use something from the driver library use the "display." prefix first
    display = drivers.Lcd()
    dhtDevice = adafruit_dht.DHT11(board.D25)
    # Setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(common.REED_SENSOR, GPIO.IN)
    GPIO.add_event_detect(common.REED_SENSOR, GPIO.RISING, 
        callback=reed_triggered, bouncetime=100)
    

    prev = None
    while 1:
        # print(sensor.get_reed())
        # print(sensor.get_temp(dhtDevice))
        if prev is None:
            display.lcd_clear()
            prev = True
        this_reed = sensor.get_reed()
        this_temp = sensor.get_temp(dhtDevice)
        if this_reed is None or this_temp is None:
            prev = None
        display.lcd_display_string(str(this_reed) + " "*2 + str(this_temp) + "C",1)
        display.lcd_display_string(str(datetime.now(tz=pytz.timezone('America/Toronto')).strftime("%Y-%m-%d %H:%M")), 2)
        time.sleep(1)
    
    


