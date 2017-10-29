from Controller.serial_communication.communication import SerialCommunication
from Controller.View.GUI import *

class Controller:

    TEMP = 1
    LIGHT = 2
    STATUS = 3

    def __init__(self):
        self.sc = SerialCommunication('COM3')
        self.root = Tk()
        self.shutter = GUI(self.root)
        self.root.mainloop()
        self.status = 0

    def send_data_to_gui(self, data):
        self.sc.read()
        # Check the id byte to make sure from what sensor the next byte will be
        if int(data[0], 2) == self.TEMP:
            return int(data[1], 2)          # If the id byte = 1, return the temperature
        elif int(data[0], 2) == self.LIGHT:
            return int(data[1], 2)          # If the id byte = 2, return the light intensity
        elif int(data[0], 2) == self.STATUS:
            return int(data[1], 2)          # If the id byte = 3, return the status

    def check_data(self, data, light, temp):
        self.sc.read()
        if int(data[0], 2) == self.TEMP and temp <= int(data[1], 2):
            self.status = 1
            self.sc.write(self.status)
        if int(data[0], 2) == self.LIGHT and light <= int(data[1], 2):
            self.status = 1
            self.sc.write(self.status)


