from BerryImu import BerryImu
from squid import *
import smbus

bus = smbus.SMBus(1)
imu = BerryImu(bus)
imu.initialise()
rgb = Squid(16, 20, 21)

while True:
	gyr_meas = imu.read_gyr_data()
       	time.sleep(0.15)
        gyr_meas2 = imu.read_gyr_data()

        value = abs(gyr_meas[1] - gyr_meas2[1])

        if  (value <= 2):
             rgb.set_color(GREEN)
    	elif(value <= 8):
            rgb.set_color(YELLOW)
        elif(value > 8):
            rgb.set_color(RED)     

