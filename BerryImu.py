#!/usr/bin/python
#
#
#        This program  provides the functions to read data from the accelerometer,
#        gyroscope and magnetometer of the BerryIMU
#
#       Based on code obtained from Mark Williams(http://ozzmaker.com/)

from Book import addressbook


class BerryImu(object):
    """Class for getting IMU data"""

    sensor_addresses = dict([('acc', addressbook['ACC_ADDRESS']),
                             ('mag', addressbook['MAG_ADDRESS']),
                             ('gyr', addressbook['GYR_ADDRESS'])])

    acc_gain = []
    mag_gain = []
    gyr_gain = []

    def __init__(self, bus):
        self.bus = bus

    def _write_to_register(self, sensor_type, register, value):
        sensor_type = sensor_type.lower()
        address = self.sensor_addresses[sensor_type]
        self.bus.write_byte_data(address, register, value)

    def _read_from_register(self, address, register):
        return self.bus.read_byte_data(address, register)

    def _read_three_axis_data(self, sensor_type):
        sensor_type = sensor_type.lower()
        address = self.sensor_addresses[sensor_type]

        axes = ["X", "Y", "Z"]
        meas = []
        for axis in axes:
            meas_l = self._read_from_register(address, addressbook["OUT_" + axis.upper() + "_L_" + sensor_type[0].upper()])
            meas_h = self._read_from_register(address, addressbook["OUT_" + axis.upper() + "_H_" + sensor_type[0].upper()])
            meas.append(self._combine_bytes(meas_h, meas_l))

        return meas

    def write_to_acc(self, register, value):
        self._write_to_register('acc', register, value)

    def write_to_mag(self, register, value):
        self._write_to_register('mag', register, value)

    def write_to_gyr(self, register,value):
        self._write_to_register('gyr', register, value)

    def initialise(self):
        # initialise the accelerometer
        self.write_to_acc(addressbook['CTRL_REG1_XM'], 0b01100111) #z,y,x axis enabled, continuos update,  100Hz data rate
        self.write_to_acc(addressbook['CTRL_REG2_XM'], 0b00100000) #+/- 16G full scale
        self.acc_gain = 0.732  # [mg/LSB]  If you change the gain for acc, you need to update this value accordingly

        # initialise the magnetometer
        self.write_to_mag(addressbook['CTRL_REG5_XM'], 0b11110000) #Temp enable, M data rate = 50Hz
        self.write_to_mag(addressbook['CTRL_REG6_XM'], 0b01100000) #+/-12gauss
        self.write_to_mag(addressbook['CTRL_REG7_XM'], 0b00000000) #Continuous-conversion mode
        self.mag_gain = 0.48 # [mgauss/ LSB] If you change the gain for acc, you need to update this value accordingly

        # initialise the gyroscope
        self.write_to_gyr(addressbook['CTRL_REG1_G'], 0b00001111) #Normal power mode, all axes enabled
        self.write_to_gyr(addressbook['CTRL_REG4_G'], 0b00110000) #Continuos update, 2000 dps full scale
        self.gyr_gain = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly

    def read_acc_data(self):
        meas_dig = self._read_three_axis_data('acc')
        meas_dig = [float(meas) for meas in meas_dig]
        acc_raw = [meas * self.acc_gain for meas in meas_dig]
        return acc_raw

    def read_mag_data(self):
        meas_dig = self._read_three_axis_data('mag')
        meas_dig = [float(meas) for meas in meas_dig]
        mag_raw = [meas * self.mag_gain for meas in meas_dig]
        return mag_raw

    def read_gyr_data(self):
        meas_dig = self._read_three_axis_data('gyr')
        meas_dig = [float(meas) for meas in meas_dig]
        gyr_raw = [meas * self.gyr_gain for meas in meas_dig]
        return gyr_raw

    @staticmethod
    def _combine_bytes(high_byte, low_byte):
        combined = (low_byte | high_byte << 8)

        if combined >= 32768:
            combined -= 65536

        return combined
