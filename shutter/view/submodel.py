from time import gmtime, strftime


class Model:
    ROLLDOWN = 1
    ROLLUP = 0

    ROLLDOWN = 1
    ROLLUP = 0

    MAXROLLDOWNDISTANCE = 1
    MAXROLLUPDISTANCE = 2
    ROLL = 3
    TEMPUPPERLIMIT = 4
    TEMPLOWESTLIMIT = 5
    LIGHTUPPERLIMIT = 6
    LIGHTLOWESTLIMIT = 7

    TEMP = 1
    LIGHT = 2
    STATUS = 3

    def __init__(self):
        self.historyledger = {}
        self.temp = ''
        self.light = ''
        self.cm_status = ''
        self.status = 0
        self.max_setting_temp = 100
        self.max_setting_light = 100
        self.min_setting_temp = 0
        self.min_setting_light = 0

    def update_model(self, data):

        try:
            time = strftime("%H:%M:%S", gmtime())
            for lists in data:
                message_id = int(lists[0])
                value = lists[1]
                if message_id == self.TEMP:
                    self.temp = value
                if message_id == self.LIGHT:
                    self.light = value
                if message_id == self.STATUS:
                    # if value >= max_down_dist:
                    #   self.status = DOWN
                    # else:
                    #   self.status = UP
                    self.cm_status = value

            # create dict with time and values
            self.historyledger[time] = {self.TEMP: self.temp, self.LIGHT: self.light}

        except IOError or ValueError:
            print("Invalid data from Arduino")
