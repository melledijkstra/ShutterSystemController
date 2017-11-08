from shutter.communication import SerialCommunication
from shutter.view import GUI
from shutter.model import Model

class Controller:

    def __init__(self, view: GUI, model: Model):
        # set view
        self.model = model
        self.view = view
        # register controller to handle ui interaction
        self.view.register(self)
        # create serial connection
        self.conn = SerialCommunication('COM3')
        self.conn.set_listener(self.serial_update)
        self.historyledger = self.model.historyledger


    def check_data(self):
        if self.model.min_setting_temp <= self.model.temp <= self.model.max_setting_temp | self.model.min_setting_light <= self.model.light <= self.model.max_setting_light:
            self.conn.write(self.model.ROLLDOWN)
        else:
            self.conn.write(self.model.ROLLUP)

    def is_connected(self):
        return self.conn.is_connected()

    def update(self):
        try:
            min_light_value = int(self.view.light_min_entry.get())
            if -1 < self.view.light_min_entry.get() < 101:
                self.conn.write(6)                # send id byte
                self.conn.write(min_light_value)  # send value byte
            elif self.view.light_min_entry.get() < 0 or self.view.light_min_entry.get() > 100:
                print("Light entry not between 0 and 100!")
                self.view.light_error.set('Light intensity should be between 0 and 100.')
        except TypeError:
            print("light entry not integer!")

        try:
            max_light_value = int(self.view.light_max_entry.get())
            if -1 < self.view.light_max_entry.get() < 101:
                self.conn.write(7)                  # send id byte
                self.conn.write(max_light_value)    # send value byte
            elif self.view.light_max_entry.get() < 0 or self.view.light_max_entry.get() > 100:
                print("Light entry not between 0 and 100!")
                self.view.light_error.set('Light intensity should be between 0 and 100.')
        except TypeError:
            print("light entry not integer!")

        try:
            min_temp_value = int(self.view.min_temp_entry.get())
            if -1 < self.view.min_temp_entry.get() < 101:
                self.conn.write(4)                  # send id byte
                self.conn.write(min_temp_value)     # send value byte
            elif self.view.min_temp_entry.get() < 0 or self.view.min_temp_entry.get() > 100:
                print ("Temp entry not between 0 and 100!")
                self.view.temp_error.set('Temperature should be between 0 and 100')
        except TypeError:
            print("Temp entry not integer!")

        try:
            max_temp_value = int(self.view.max_temp_entry.get())
            if -1 < self.view.max_temp_entry.get() < 101:
                self.conn.write(5)                  # send id byte
                self.conn.write(max_temp_value)     # send value byte
            elif self.view.max_temp_entry.get() < 0 or self.view.max_temp_entry.get() > 100:
                print ("Temp entry not between 0 and 100!")
                self.view.temp_error.set('Temperature should be between 0 and 100')
        except TypeError:
            print("Temp entry not integer!")

        try:
            max_rolldown_value = int(self.view.max_distance_entry.get())
            if -1 < max_rolldown_value < 256:
                self.conn.write(1)                      # send id byte
                self.conn.write(max_rolldown_value)     # send value byte
            elif max_rolldown_value  <-1 or max_rolldown_value > 256:
                print("Min rollup distance entry not between 0 and 255!")
                self.view.min_error.set('Minimum distance should be between 0 and 255.')
        except TypeError:
            print("Min distance entry not integer!")

        try:
            max_rollup_value = int(self.view.min_distance_entry.get())
            if -1 < max_rollup_value < 256 and self.view.max_distance_entry.get() > self.view.min_distance_entry.get():
                self.conn.write(2)                      # send id byte
                self.conn.write(max_rollup_value)       # send value byte
            else:
                if self.view.max_distance_entry.get()  <-1 or self.view.max_distance_entry.get() > 256:
                    print("Max distance entry not between 0 and 255")
                    self.view.max_error.set('Maximum distance should be between 0 and 255')
                elif self.view.max_distance_entry.get() <= self.view.min_distance_entry.get():
                    print("Max distance is smaller or equal to min distance")
                    self.view.max_error.set('Maximum distance should be larger than minimum.')
        except TypeError:
            print("Max distance entry not integer")

    def isConnected(self):
        return self.conn.is_connected()

    def serial_update(self, data: list):
        # check incoming data
        self.model.update_model(data)
        self.view.update(self.model.temp, self.model.light, self.model.status)

    def inputIncoming(self, byte):
        # check incoming data
        self.model.update_model(byte)
        self.view.update(self.model.temp, self.model.light, self.model.status)

    def connect(self):
        status = self.conn.open_connection()
        self.view.update_connection_status(status)

    def toggle_shutter(self):
        if self.model.status is self.model.ROLLDOWN:
            print("sending rollup message")
            self.conn.write(3)
            self.conn.write(self.model.ROLLUP)
            self.status = self.model.ROLLUP
        else:
            print("sending rolldown message")
            self.conn.write(3)
            self.conn.write(self.model.ROLLDOWN)
            self.model.status = self.model.ROLLDOWN



