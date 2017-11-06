from shutter.communication import SerialCommunication
from shutter.view import GUI
from shutter.model import Model

class Controller:

    def __init__(self):
        self.model = Model()
        # setup serial communication
        self.conn = SerialCommunication('COM3')
        self.conn.set_listener(self.serial_update)
        # set view
        self.view = GUI()
        self.view.set_controller(self)
        self.view.structure_gui()
        self.view.run()

    def check_data(self):
        if self.model.min_setting_temp <= self.model.temp <= self.model.max_setting_temp | self.model.min_setting_light <= self.model.light <= self.model.max_setting_light:
            self.conn.write(self.model.ROLLDOWN)
        else:
            self.conn.write(self.model.ROLLUP)

    def is_connected(self):
        return self.conn.is_connected()

    def serial_update(self, data: list):
        # check incoming data
        self.model.update_model(data)
        self.view.update(self.model.temp, self.model.light, self.model.status)

    def connect(self):
        status = self.conn.open_connection()
        self.view.update_connection_status(status)

    def toggle_shutter(self):
        if self.model.status is self.model.ROLLDOWN:
            print("sending rollup message")
            self.conn.write(self.model.ROLLUP)
            self.status = self.model.ROLLUP
        else:
            print("sending rolldown message")
            self.conn.write(self.model.ROLLDOWN)
            self.model.status = self.model.ROLLDOWN



