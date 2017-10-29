from serial import Serial
import time

class SerialCommunication:

    def __init__(self, port):
        # open serial port at 19k2 (default = 8 data bits, 1 stop bit, no parity)
        self.ser = Serial(port=port, baudrate=19200)
        time.sleep(2)       # wait for the Arduino to connect
        print(self.ser)     # check which port is really used
        self.data = []
        self.int_value = 0

    def read(self):
        while True:
            self.data = []
            line = self.ser.read()  # read the id byte
            line = line.hex()
            self.data.append(line) # add the id byte to the list
            line = self.ser.read()  # read the value byte
            line = line.hex()
            self.data.append(line) # add the value byte to the list
            print(self.data)
            return self.data

    def write(self, status):
        # if byte == 1 byte lang:
            self.ser.write(status)



