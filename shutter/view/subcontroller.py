from shutter.view.submodel import Model


class SubController:
    def __init__(self, connection, tab):
        self.model = Model()
        self.conn = connection
        self.tab = tab
        self.tab.register(self)

    def is_connected(self):
        return self.conn.is_connected()

    def update(self):
        try:
            min_light_value = int(self.tab.light_min_entry.get())
            if -1 < self.tab.light_min_entry.get() < 101:
                self.conn.write(self.model.LIGHTUPPERLIMIT)  # send id byte
                self.conn.write(min_light_value)  # send value byte
            elif self.tab.light_min_entry.get() < 0 or self.tab.light_min_entry.get() > 100:
                print("Light entry not between 0 and 100!")
                self.tab.light_error.set("Light intensity should be between 0 and 100.")
        except TypeError:
            print("Light entry not integer!")

        try:
            max_light_value = int(self.tab.light_max_entry.get())
            if -1 < self.tab.light_max_entry.get() < 101:
                self.conn.write(self.model.LIGHTLOWESTLIMIT)  # send id byte
                self.conn.write(max_light_value)  # send value byte
            elif self.tab.light_max_entry.get() < 0 or self.tab.light_max_entry.get() > 100:
                print("Light entry not between 0 and 100!")
                self.tab.light_error.set("Light intensity should be between 0 and 100.")
        except TypeError:
            print("light entry not integer!")

        try:
            min_temp_value = int(self.tab.min_temp_entry.get())
            if -1 < self.tab.min_temp_entry.get() < 101:
                self.conn.write(self.model.TEMPUPPERLIMIT)  # send id byte
                self.conn.write(min_temp_value)  # send value byte
            elif self.tab.min_temp_entry.get() < 0 or self.tab.min_temp_entry.get() > 100:
                print("Temp entry not between 0 and 100!")
                self.tab.temp_error.set("Temperature should be between 0 and 100")
        except TypeError:
            print("Temp entry not integer!")

        try:
            max_temp_value = int(self.tab.max_temp_entry.get())
            if -1 < self.tab.max_temp_entry.get() < 101:
                self.conn.write(self.model.TEMPLOWESTLIMIT)  # send id byte
                self.conn.write(max_temp_value)  # send value byte
            elif self.tab.max_temp_entry.get() < 0 or self.tab.max_temp_entry.get() > 100:
                print("Temp entry not between 0 and 100!")
                self.tab.temp_error.set("Temperature should be between 0 and 100")
        except TypeError:
            print("Temp entry not integer!")

        try:
            max_rolldown_value = int(self.tab.max_distance_entry.get())
            if -1 < max_rolldown_value < 256:
                self.conn.write(self.model.MAXROLLDOWNDISTANCE)  # send id byte
                self.conn.write(max_rolldown_value)  # send value byte
            elif max_rolldown_value < -1 or max_rolldown_value > 256:
                print("Min rollup distance entry not between 0 and 255!")
                self.tab.min_error.set("Minimum distance should be between 0 and 255.")
        except TypeError:
            print("Min distance entry not integer!")

        try:
            max_rollup_value = int(self.tab.min_distance_entry.get())
            if -1 < max_rollup_value < 256 and self.tab.max_distance_entry.get() > self.tab.min_distance_entry.get():
                self.conn.write(self.model.MAXROLLUPDISTANCE)  # send id byte
                self.conn.write(max_rollup_value)  # send value byte
            else:
                if self.tab.max_distance_entry.get() < -1 or self.tab.max_distance_entry.get() > 256:
                    print("Max distance entry not between 0 and 255")
                    self.tab.max_error.set("Maximum distance should be between 0 and 255")
                elif self.tab.max_distance_entry.get() <= self.tab.min_distance_entry.get():
                    print("Max distance is smaller or equal to min distance")
                    self.tab.max_error.set("Maximum distance should be larger than minimum.")
        except TypeError:
            print("Max distance entry not integer")

    def isConnected(self):
        return self.conn.is_connected()

    def serial_update(self, data: list):
        # check incoming data
        self.model.update_model(data)
        self.tab.update(self.model.temp, self.model.light)
        self.tab.update_status(self.model.status, self.model.cm_status)

    def connect(self):
        status = self.conn.open_connection()
        self.tab.update_connection_status(status)

    def toggle_shutter(self):
        if self.model.status == self.model.ROLLDOWN:
            print("sending rollup message")
            self.conn.write(self.model.ROLL)
            self.conn.write(self.model.ROLLUP)
            self.model.status = self.model.ROLLUP
        else:
            print("sending rolldown message")
            self.conn.write(self.model.ROLL)
            self.conn.write(self.model.ROLLDOWN)
            self.model.status = self.model.ROLLDOWN

        self.tab.update_status(self.model.status, self.model.cm_status)
