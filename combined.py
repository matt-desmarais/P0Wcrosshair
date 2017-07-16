import time
import datetime
import smbus
import RPi.GPIO as GPIO
from BerryImu import BerryImu
from squid import *

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

clkLastState = GPIO.input(clk)

bus = smbus.SMBus(1)
imu = BerryImu(bus)
imu.initialise()
rgb = Squid(18, 23, 24)


try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                if counter <= 2:
                                    counter += 1
                                else:
                                    counter = 3
                        else:
                                if counter!=0:
                                    counter -= 1
                                else:
                                    counter=0
                        if counter==0:
                            camera.zoom = (0, 0, 1.0, 1.0)
                        if counter==1:
                            camera.zoom = (0.25, 0.25, 0.5, 0.5)
                        if counter==2:
                            camera.zoom = (0.125, 0.125, 0.5, 0.5)
                        if counter==3:
                            camera.zoom = (0.0625, 0.0625, 0.5, 0.5)
                clkLastState = clkState
                
            gyr_meas = imu.read_gyr_data()
	        time.sleep(0.25)
	        gyr_meas2 = imu.read_gyr_data()
	        value = abs(gyr_meas[1] - gyr_meas2[1])

	    if  (value <= 2):
	        rgb.set_color(GREEN)
	    elif(value <= 12):
	        rgb.set_color(YELLOW)
	    elif(value > 12):
	        rgb.set_color(RED)     
finally:
        GPIO.cleanup()
