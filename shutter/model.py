class Model:

    TEMP = 1
    LIGHT = 2
    STATUS = 3

    ROLLDOWN = 1
    ROLLUP = 0

    def __init__(self):
        self.temp = 0
        self.light = 0
        self.status = 0
        self.max_setting_temp = 100
        self.max_setting_light = 100
        self.min_setting_temp = 0
        self.min_setting_light = 0

    def update_model(self, data):
        if data[0] == self.TEMP:
            self.temp = data[1]
        if data[0] == self.LIGHT:
            self.light = data[1]
        if data[0] == self.STATUS:
            self.status = data[1]
