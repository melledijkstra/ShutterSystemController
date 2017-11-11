from time import gmtime, strftime

class Model:

    MAXROLLDOWNDISTANCE = 1
    MAXROLLUPDISTANCE = 2
    ROLL = 3
    TEMPUPPERLIMIT = 4
    TEMPLOWESTLIMIT = 5
    LIGHTUPPERLIMIT = 6
    LIGHTLOWESTLIMIT = 7

    def __init__(self):
        self.historyledger = {}
        self.temp = ''
        self.light = ''
        self.status = ''
        self.max_setting_temp = 100
        self.max_setting_light = 100
        self.min_setting_temp = 0
        self.min_setting_light = 0

    def update_model(self, data):

        TEMP = 1
        LIGHT = 2

        try:
            time = strftime("%H:%M:%S", gmtime())
            for lists in data:
                id = lists[0]
                value = lists[1]
                if int(id) == TEMP:
                    self.temp = value
                if int(id) == LIGHT:
                    self.light = value

            # create dict with time and values
            self.historyledger[time] = {TEMP: self.temp, LIGHT: self.light}

        except IOError:
            print("Invalid data from Arduino")