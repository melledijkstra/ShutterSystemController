from serial import *
import time

class SerialCommunication:

    def __init__(self, port):
        # open serial port at 19k2 (default = 8 data bits, 1 stop bit, no parity)
        self.port = port
        self.baud = 19200
        self.open_connection()
        self.data = []

    def open_connection(self):
        print("making connection with " + self.port)
        try:
            self.ser = Serial(port=self.port, baudrate=self.baud)
            time.sleep(2)       # wait for the Arduino to connect
            self._connected = True
        except SerialException as e:
            self._connected = False
            print(e.strerror)
        return self._connected

    def isConnected(self):
        return self._connected

    def read(self):
        while True:
            self.data = []
            line = self.ser.read()  # read the id byte
            line = line.hex()
            self.data.append(line) # add the id byte to the list
            line = self.ser.read()  # read the value byte
            line = line.hex()
            self.data.append(line) # add the value byte to the list
            # print(self.data)
            # return self.data

    def write(self, status):
        # if byte == 1 byte lang:
        self.ser.write(status)

    # def send_data_to_gui(self, data):
    #     # Check the id byte to make sure from what sensor the next byte will be
    #     if int(data[0], 2) == LIGHT:    # If the id byte = 1, call the function to show the light on the gui
    #     elif int(data[0], 2) == TEMP:  # If the id byte = 2, call the function to show the temperature on the gui
    #         return int(data[1], 2)
    #     elif int(data[0], 2) == STATUS:  # If the id byte = 3, call the function to show the status on the gui
    #         return int(data[1], 2)

    def set_listener(self, func):
        self.trigger = func


if __name__ == '__main__':
    sc = SerialCommunication('COM3')
    sc.read()
