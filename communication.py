import serial

ser = serial.Serial()


# to list ports run the following command in shell
# python3 -m serial.tools.list_ports

def connect_ethercat():
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM0'
    ser.open()


# Format: XXXnnn => XXX: data ref; nnn: data value; 6 bytes of data
def read_data():
    data_in = ser.read(6)
    return data_in


# Format: Xxxnnn => X: zone ref (A, B, C, D, E); xx: button number (1-99); nnn: value (0 to 100)
# return value should be 6 bytes
def write_data(data_out):
    ret = ser.write(data_out)
    return ret
