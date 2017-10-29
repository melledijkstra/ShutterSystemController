from shutter.communication import SerialCommunication
from shutter.view import GUI

class Controller():

    TEMP = 1
    LIGHT = 2
    STATUS = 3

    ROLLDOWN    = 1
    ROLLUP      = 0

    def __init__(self):
        self.status = self.ROLLUP
        # setup serial communication
        self.conn = SerialCommunication('COM3')
        self.conn.set_listener(self.inputIncoming)
        # set view
        self.view = GUI()
        self.view.set_controller(self)
        self.view.structure_gui()
        self.view.run()

    def send_data_to_gui(self, data):
        self.conn.read()
        # Check the id byte to make sure from what sensor the next byte will be
        if int(data[0], 2) == self.TEMP:
            return int(data[1], 2)          # If the id byte = 1, return the temperature
        elif int(data[0], 2) == self.LIGHT:
            return int(data[1], 2)          # If the id byte = 2, return the light intensity
        elif int(data[0], 2) == self.STATUS:
            return int(data[1], 2)          # If the id byte = 3, return the status

    def check_data(self, data: list, light: int, temp: float):
        if (int(data[0], 2) == self.TEMP and temp <= int(data[1], 2)) | \
            int(data[0], 2) == self.LIGHT and light <= int(data[1], 2):
            self.conn.write(self.ROLLDOWN)

    def update(self):
        print("updated")

    def isConnected(self):
        return self.conn.isConnected()

    def inputIncoming(self, byte):
        # check incoming data
        pass

    def connect(self):
        status = self.conn.open_connection()
        self.view.update_connection_status(status)

    def toggle_shutter(self):
        if self.status is self.ROLLDOWN:
            print("sending rollup message")
            self.conn.write(self.ROLLUP)
            self.status = self.ROLLUP
        else:
            print("sending rolldown message")
            self.conn.write(self.ROLLDOWN)
            self.status = self.ROLLDOWN



