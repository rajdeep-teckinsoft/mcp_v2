import serial
from serial import SerialException

ser = serial.Serial()


# to list ports run the following command in shell
# python3 -m serial.tools.list_ports

def connect_ethercat():
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM0'
    try:
        ser.open()
        return True
    except SerialException:
        return False


def read_data():
    data_in = ser.read(1)
    return data_in


def write_data(data_out):
    # formatted_data = data_out.encode()
    # ret = ser.write(formatted_data)
    ret = ser.write(data_out)
    return ret
