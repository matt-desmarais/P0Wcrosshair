import pytest
try:
    # For version 3.x python
    import unittest.mock as mock
except ImportError:
    # For version 2.x python
    import mock as mock

from BerryImu import BerryImu


# bus object methods
# bus.write_byte_data(address, register, value)
# bus.read_byte_data(address, register)



class TestBerryImu:

    def test_write_to_register(self):
        bus = mock.Mock()
        imu = BerryImu(bus)
        sensor_type = 'acc'
        register = 0x20
        value = 0b01100111
        imu._write_to_register(sensor_type, register, value)
        bus.write_byte_data.assert_called_with(
            imu.sensor_addresses[sensor_type], register, value)

    def test_read_from_register(self):
        bus = mock.Mock()
        bus.read_byte_data.return_value = b'0AxG'
        imu = BerryImu(bus)

        byte_data = imu._read_from_register(address=1, register=7)
        assert byte_data == b'0AxG'

    def test_read_gyr_data(self):
        # Prepare low byte/high byte output from mock sensor
        bus = mock.Mock()
        side_effect = [1, 0, 2, 0, 3, 0]
        bus.read_byte_data.side_effect=side_effect
        imu = BerryImu(bus)
        imu.gyr_gain = 1
        output = imu.read_gyr_data()

        # check that 6 calls (two for each of the 3 gyr axes) were
        # made to read_byte_data
        assert bus.read_byte_data.call_count == 6
        assert output == [1, 2, 3]

        for item in bus.read_byte_data.call_args_list:
            # Check that all of the calls were made to the gyro address
            assert item[0][0] == imu.sensor_addresses['gyr']

    def test_read_acc_data(self):
        # Prepare low byte/high byte output from mock sensor
        bus = mock.Mock()
        side_effect = [1, 0, 2, 0, 3, 0]
        bus.read_byte_data.side_effect=side_effect
        imu = BerryImu(bus)
        imu.acc_gain = 1
        output = imu.read_acc_data()

        # check that 6 calls (two for each of the 3 gyr axes) were
        # made to read_byte_data
        assert bus.read_byte_data.call_count == 6
        assert output == [1, 2, 3]

        for item in bus.read_byte_data.call_args_list:
            # Check that all of the calls were made to the acc address
            assert item[0][0] == imu.sensor_addresses['acc']


    def test_read_mag_data(self):
        # Prepare low byte/high byte output from mock sensor
        bus = mock.Mock()
        side_effect = [1, 0, 2, 0, 3, 0]
        bus.read_byte_data.side_effect=side_effect
        imu = BerryImu(bus)
        imu.mag_gain = 1
        output = imu.read_mag_data()

        # check that 6 calls (two for each of the 3 gyr axes) were
        # made to read_byte_data
        assert bus.read_byte_data.call_count == 6
        assert output == [1, 2, 3]

        for item in bus.read_byte_data.call_args_list:
            # Check that all of the calls were made to the acc address
            assert item[0][0] == imu.sensor_addresses['mag']


    def test_combine_bytes_negative_number(self):
        bus = mock.Mock()
        imu = BerryImu(bus)

        high_byte = 177
        low_byte = 7899
        output = imu._combine_bytes(high_byte, low_byte)

        assert output < 0

    def test_combine_bytes_positive_number(self):
        bus = mock.Mock()
        imu = BerryImu(bus)

        high_byte = 0
        low_byte = 1
        output = imu._combine_bytes(high_byte, low_byte)

        assert output == low_byte