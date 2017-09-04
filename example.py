# This program uses the BME_280 sensor using I2c
# and Adafruit GPIO module library
# This program uses two LEDs, one connected to GPIO pin 32, the other connected to
# pin 37.
# The program turns different LEDs on and off depending on the temperature.


# Author: Aydin Zaman
# 2017-04-01
import sys
import traceback
import time
import RPi.GPIO as GPIO
from Adafruit_BME280 import *

degrees = 0
fah = 0
hectopascals = 0
humidity = 0
GPIO.setmode(GPIO.BOARD)


# Looking up the sensor and setting it for output
redpin = 32
greenpin = 37

sensor = BME280(mode=BME280_OSAMPLE_8)
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)

def blinkLED():
    # Turning the LEDs on and off
    if fah < 80.0 and fah > 70.0:
        GPIO.output(greenpin, GPIO.HIGH)
        GPIO.output(redpin, GPIO.LOW)
    else:
        GPIO.output(greenpin, GPIO.LOW)
        GPIO.output(redpin, GPIO.HIGH)


def readSensor():
    global degrees, fah, pascals, hectopascals, humidity

    # Changing the mode to BOARD (pin number on the board)
    degrees = sensor.read_temperature()
    fah = 9.0 / 5.0 * degrees + 32
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()
    
def printInfo():
    print 'Fahrenheit= {0:0.3f} deg F'.format(fah)
    print 'Celsius   = {0:0.3f} deg C'.format(degrees)
    print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
    print 'Humidity  = {0:0.2f} %'.format(humidity)
    print '==========={0}==========='.format(time.strftime("%Y-%m-%d %H:%M"))

def main_loop() :
    while True:
        try:
            readSensor()
            printInfo()
            blinkLED()
            time.sleep(2.0)
        except:
            print("Oops...something went wrong")
            traceback.print_exc(file=sys.stdout)
            break

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    try:
        main_loop()
    except :
        traceback.print_exc(file=sys.stdout)
    finally:
    # reset the sensor before exiting the program
        GPIO.cleanup()