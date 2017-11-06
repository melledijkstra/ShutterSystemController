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

    #Update button
        #Check value's in entry's. If value is OK, send value. If value is not OK, refuse and try again.
    def update(self):
        #light_entry
        #temp_entry
        #min_distance_entry
        #max_distance_entry
        try:
            if (self.view.light_entry.get() >-1 and self.view.light_entry.get() < 101):
                #send update
                print("updated light ")
            elif (self.view.light_entry.get() <0 or self.view.light_entry.get() > 100):
                print("light entry not between 0 and 100")
            else:
                print("unknown error")
        except:
            print("light entry not integer")

        try:
            if (self.view.temp_entry.get() >-1 and self.view.temp_entry.get() < 101):
                #send update
                print ("updated temperature")
            elif (self.view.temp_entry.get() <0 or self.view.temp_entry.get() > 100):
                print ("temp entry not between 0 and 100")
            else:
                print("unknown error")
        except:
            print("temp entry not integer")

        try:
            if (self.view.min_distance_entry.get() >-1 and self.view.min_distance_entry.get() < 256 ):
                #send update
                print("updated min distance")
            elif(self.view.min_distance_entry.get()  <-1 or self.view.min_distance_entry.get() > 256):
                print("min distance entry not between 0 and 255")
            else:
                print("unknown error")
        except:
            print("min distance entry not integer")

        try:
            if (self.view.max_distance_entry.get() >-1 and self.view.max_distance_entry.get() < 256 and self.view.max_distance_entry.get() > self.view.min_distance_entry.get() ):
                #send update
                print("updated max distance")
            else:
                if (self.view.max_distance_entry.get()  <-1 or self.view.max_distance_entry.get() > 256):
                    print("max distance entry not between 0 and 255")
                elif (self.view.max_distance_entry.get() <= self.view.min_distance_entry.get() ):
                    print("max distance is smaller or equal to min distance")
                else:
                    print("unknown error")
        except:
            print("max distance entry not integer")

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



