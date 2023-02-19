#! /usr/bin/python3
import common
import sensor
# from sensor import *
import time
import time
import board
import adafruit_dht
import drivers
from time import sleep
import pytz
from datetime import datetime
import RPi.GPIO as GPIO

SLEEP_ENABLE = False
display = None
pause = False

def reed_triggered(channel):
    global pause 
    pause = True
    display.lcd_clear()
    # time.sleep(1)
    display.lcd_display_string("You wake up.",1)
    print("WakeUp detected.")
    with open("Awake.log","a") as af:
        af.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        af.write('\n')
    time.sleep(1)
    display.lcd_clear()
    pause = False

def btn_toggled(channel):
    global pause 
    pause = True
    print("BTN get!")
    global SLEEP_ENABLE
    SLEEP_ENABLE = not SLEEP_ENABLE
    global display
    display.lcd_clear()
    # time.sleep(1)
    pause = False


if __name__ == "__main__":
    # Load the driver and set it to "display"
    # If you use something from the driver library use the "display." prefix first
    PROD = True
    display = drivers.Lcd()
    dhtDevice = adafruit_dht.DHT11(board.D25)
    # # Setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(common.REED_SENSOR, GPIO.IN)
    GPIO.setup(common.BTN_SENSOR, GPIO.IN)
    GPIO.add_event_detect(common.REED_SENSOR, GPIO.RISING, 
        callback=reed_triggered, bouncetime=5000)
    GPIO.add_event_detect(common.BTN_SENSOR, GPIO.RISING, 
        callback=btn_toggled, bouncetime=1000)
    

    prev = None
    while 1:
        # print(sensor.get_reed())
        # print(sensor.get_temp(dhtDevice))
        if not pause:
            if prev is None:
                display.lcd_clear()
                prev = True
            this_reed = 9 # sensor.get_reed()
            this_temp = sensor.get_temp(dhtDevice)
            if this_temp is not None and PROD:
                with open("Temperature.log", "a") as f:
                    f.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "," + str(this_temp))
                    f.write("\n")
            if this_reed is None or this_temp is None:
                prev = None
            if SLEEP_ENABLE:
                display.lcd_display_string(str(this_reed) + " "*2 + str(this_temp) + "C",1)
                display.lcd_display_string(str(datetime.now(tz=pytz.timezone('America/Toronto')).strftime("%Y-%m-%d %H:%M")), 2)
            else:
                display.lcd_display_string(str(datetime.now(tz=pytz.timezone('America/Toronto')).strftime("%Y-%m-%d %H:%M")), 1)
        time.sleep(common.DELAY)
        
    


