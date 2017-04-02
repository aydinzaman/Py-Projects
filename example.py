# This program uses the BME_280 sensor using I2c
# and Adafruit GPIO module library
# This program uses two LEDs, one connected to GPIO pin 32, the other connected to
# pin 37. 
# The program turns different LEDs on and off depending on the temperature.


# Author: Aydin Zaman
# 2017-04-01

import RPi.GPIO as GPIO                                           
import time
# We need to import the Adafruit Bme library for this to work
from Adafruit_BME280 import *

# Changing the mode to BOARD (pin number on the board)
GPIO.setmode(GPIO.BOARD)                                          

redpin = 32                                                    
greenpin = 37  

# Looking up the sensor and setting it for output                                                 
sensor = BME280(mode=BME280_OSAMPLE_8)                            
GPIO.setup(redpin, GPIO.OUT)                                   
GPIO.setup(greenpin, GPIO.OUT)                                   
                                                                  
while True:
	try:                                                       
		degrees = sensor.read_temperature()                       
		fah = 9.0/5.0 * degrees + 32
			  
		pascals = sensor.read_pressure()
		hectopascals = pascals / 100                              
			
		humidity = sensor.read_humidity()                         
			
	# Turning the LEDs on and off                                                       
		if fah < 80.0:                                            
			GPIO.output(redpin, GPIO.HIGH)                 
			GPIO.output(greenpin, GPIO.LOW)                 
		else:                                                     
			GPIO.output(redpin, GPIO.LOW)                  
			GPIO.output(greenpin, GPIO.HIGH)                  
																	  
		print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)        
		print 'Celsius   = {0:0.3f} deg C'.format(degrees)        
		print 'Fahrenheit= {0:0.3f} deg F'.format(fah)            
		print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)     
		print 'Humidity  = {0:0.2f} %'.format(humidity)           
		print '======================='                           
		time.sleep(1.0)
	except:
		print("Oops...something went wrong")
		break

# reset the sensor before exiting the program
GPIO.cleanup()
                                  
									
