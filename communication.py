import serial

ser = serial.Serial('', 115200)


def read_data():
    data_in = ser.readline()
    return data_in


def write_data(data_out):
    ser.write(data_out)
    return
