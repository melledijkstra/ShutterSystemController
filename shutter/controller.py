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


    def check_data(self):
        if self.model.min_setting_temp <= self.model.temp <= self.model.max_setting_temp | self.model.min_setting_light <= self.model.light <= self.model.max_setting_light:
            self.conn.write(self.model.ROLLDOWN)
        else:
            self.conn.write(self.model.ROLLUP)

    def is_connected(self):
        return self.conn.is_connected()

    # Update button
    def update(self):

        try:
            if (self.view.light_entry.get() >-1 and self.view.light_entry.get() < 101):
                #send update
                print("updated light")
                self.view.light_error.set('')
                self.view.frame.update()
            elif (self.view.light_entry.get() <0 or self.view.light_entry.get() > 100):
                print("!light entry not between 0 and 100")
                self.view.light_error.set('Light intensity should be between 0 and 100.')
                self.view.frame.update()
            else:
                print("!unknown error")
                self.view.light_error.set('Unknown error.')
                self.view.frame.update()
        except:
            print("!light entry not integer")
            self.view.light_error.set('Light intensity should be an integer.')
            self.view.frame.update()

        try:
            if (self.view.temp_entry.get() > -1 and self.view.temp_entry.get() < 101):
                # send update
                print ("updated temperature")
                self.view.temp_error.set('')
                self.view.frame.update()
            elif (self.view.temp_entry.get() <0 or self.view.temp_entry.get() > 100):
                print ("!temp entry not between 0 and 100")
                self.view.temp_error.set('Temperature should be between 0 and 100')
                self.view.frame.update()
            else:
                print("!unknown error")
                self.view.temp_error.set('Unknown error')
                self.view.frame.update()
        except:
            print("!temp entry not integer")
            self.view.temp_error.set('Temperature should be an integer')
            self.view.frame.update()

        try:
            if (self.view.min_distance_entry.get() >-1 and self.view.min_distance_entry.get() < 256 ):
                #send update
                print("updated min distance")
                self.view.min_error.set('')
                self.view.frame.update()
            elif(self.view.min_distance_entry.get()  <-1 or self.view.min_distance_entry.get() > 256):
                print("!min distance entry not between 0 and 255")
                self.view.min_error.set('Minimum distance should be between 0 and 255.')
                self.view.frame.update()
            else:
                print("!unknown error")
                self.view.min_error.set('Unknown error.')
                self.view.frame.update()
        except:
            print("!min distance entry not integer")
            self.view.min_error.set('Minimum distance should be an integer.')
            self.view.frame.update()

        try:
            if (self.view.max_distance_entry.get() >-1 and self.view.max_distance_entry.get() < 256 and self.view.max_distance_entry.get() > self.view.min_distance_entry.get() ):
                #send update
                print("updated max distance")
                self.view.max_error.set('')
                self.view.frame.update()
            else:
                if (self.view.max_distance_entry.get()  <-1 or self.view.max_distance_entry.get() > 256):
                    print("!max distance entry not between 0 and 255")
                    self.view.max_error.set('Maximum distance should be between 0 and 255')
                    self.view.frame.update()
                elif (self.view.max_distance_entry.get() <= self.view.min_distance_entry.get() ):
                    print("!max distance is smaller or equal to min distance")
                    self.view.max_error.set('Maximum distance should be larger than minimum.')
                    self.view.frame.update()
                else:
                    print("!unknown error")
                    self.view.max_error.set('Unknown error')
                    self.view.frame.update()
        except:
            print("!max distance entry not integer")
            self.view.max_error.set('Maximum distance should be an integer.')
            self.view.frame.update()

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
            self.conn.write(self.model.ROLLUP)
            self.status = self.model.ROLLUP
        else:
            print("sending rolldown message")
            self.conn.write(self.model.ROLLDOWN)
            self.model.status = self.model.ROLLDOWN



