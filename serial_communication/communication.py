from serial import Serial
import time

class SerialCommunication:

    TEMP = 1
    LIGHT = 2
    STATUS = 3

    def __init__(self, port):
        # open serial port at 19k2 (default = 8 data bits, 1 stop bit, no parity)
        self.ser = Serial(port=port, baudrate=19200)
        time.sleep(2)       # wait for the Arduino to connect
        print(self.ser)     # check which port is really used
        self.bytes = []
        self.int_value = 0

    def read(self):
        while True:
            self.bytes = []
            line = self.ser.read()  # read the id byte
            line = line.hex()
            self.bytes.append(line) # add the id byte to the list
            line = self.ser.read()  # read the value byte
            line = line.hex()
            self.bytes.append(line) # add the value byte to the list
            print(self.bytes)
            return self.bytes

    def write(self, byte: bytes):
        # if byte == 1 byte lang:
            self.ser.write(byte)

    # def send_data_to_gui(self, data):
    #     # Check the id byte to make sure from what sensor the next byte will be
    #     if int(data[0], 2) == LIGHT:    # If the id byte = 1, call the function to show the light on the gui
    #     elif int(data[0], 2) == TEMP:  # If the id byte = 2, call the function to show the temperature on the gui
    #         return int(data[1], 2)
    #     elif int(data[0], 2) == STATUS:  # If the id byte = 3, call the function to show the status on the gui
    #         return int(data[1], 2)

sc = SerialCommunication('COM3')
sc.read()


