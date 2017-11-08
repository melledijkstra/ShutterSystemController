from tkinter import *


class Chart():
    def __init__(self, frame: Frame):
        self.line = 1
        self.x_temp_2 = 50
        self.y_temp_2 = 0
        self.x_light_2 = 50
        self.y_light_2 = 0

        self.canvas = Canvas(frame, width=1400, height=490, bg='white')  # 0,0 is top left corner
        self.canvas.grid(row=10, column=0, rowspan=2, columnspan=12)

        # Outer lines
        self.canvas.create_line(50, 450, 1350, 450, width=2)  # x-axis
        self.canvas.create_line(50, 450, 50, 50, width=2)  # y-axis

        self.plot_axes()

    def step(self, temp_val, light_val):
        #if out of range create 'new frame' and throw away old items
        if self.line == 27:
            # new frame
            self.line = 1
            self.x_temp_2 = 50
            self.x_light_2 = 50
            self.canvas.delete('temp')  # only delete items tagged as temp
        #first value on graph should be equal to first value
        if self.line == 1:
            self.y_light_2 = self.value_to_y(light_val)
            self.y_temp_2 = self.value_to_y(temp_val)
        # draw temperature line
        x_temp_1 = self.x_temp_2        #write last value to x1
        y_temp_1 = self.y_temp_2        #write last value to y1
        self.x_temp_2 = 50 + self.line * 50             # x-axis temp value
        self.y_temp_2 = self.value_to_y(temp_val)       # y-axis temp_value
        self.canvas.create_line(x_temp_1, y_temp_1, self.x_temp_2, self.y_temp_2, fill='red', width=3, tags='temp')
        # draw light intensity line
        x_light_1 = self.x_light_2      #write last value to x1
        y_light_1 = self.y_light_2      #write last value to y1
        self.x_light_2 = 50 + self.line * 50            # x-axis light value
        self.y_light_2 = self.value_to_y(light_val)     # y-axis light_value
        self.canvas.create_line(x_light_1, y_light_1, self.x_light_2, self.y_light_2, fill='yellow', width=3, tags='temp')

        self.line += 1

    #Draws ax lines on screen
    def plot_axes(self):
        # x-axis
        for i in range(27):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 450, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 450, text='%d' % (1 * i), anchor=N)
        self.canvas.create_text(60, 470, text='Time (minutes)', anchor=N)
        # y-axis
        for i in range(11):
            y = 450 - (i * 40)
            self.canvas.create_line(50, y, 1350, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)
        self.canvas.create_text(20, 440, text='Value', anchor=E, angle=90)

    # Sets value to right amount of pixels on screen
    def value_to_y(self, val):
        if float(val) > 100:
            #if value above 100 remain 100
            return 450 - 4 * float(100.0)
        else:
            return 450 - 4 * float(val)
