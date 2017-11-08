from tkinter import *

class Chart():

    def __init__(self, frame: Frame):
        self.running = True
        self.minimum = 0
        self.maximum = 100
        self.f = 1
        self.x_temp_2 = 50
        self.y_temp_2 = 0  # temp_value
        self.x_light_2 = 50
        self.y_light_2 = 0  # light_value

        self.canvas = Canvas(frame, width=1400, height=490, bg='white')  # 0,0 is top left corner
        self.canvas.grid(row=10, column=0, rowspan=2, columnspan=12)

        # Outer lines
        self.canvas.create_line(50, 450, 1350, 450, width=2)  # x-axis
        self.canvas.create_line(50, 450, 50, 50, width=2)  # y-axis

        self.plot_axes()


    def step(self, temp_val, light_val):
        if self.f == 27:
            # new frame
            self.f = 1
            self.x_temp_2 = 50
            self.x_light_2 = 50
            self.canvas.delete('temp')  # only delete items tagged as temp

        # draw temperature line
        x_temp_1 = self.x_temp_2
        y_temp_1 = self.y_temp_2
        self.x_temp_2 = 50 + self.f * 50
        self.y_temp_2 = self.value_to_y(temp_val)          #temp_value
        self.canvas.create_line(x_temp_1, y_temp_1, self.x_temp_2, self.y_temp_2, fill='red', width=3, tags='temp')
        # draw light intensity line
        x_light_1 = self.x_light_2
        y_light_1 = self.y_light_2
        self.x_light_2 = 50 + self.f * 50
        self.y_light_2 = self.value_to_y(light_val)        #light_value
        self.canvas.create_line(x_light_1, y_light_1, self.x_light_2, self.y_light_2, fill='yellow', width=3,
                                tags='temp')

        self.f += 1
        self.id = self.canvas.after(300, self.step)


    def plot_axes(self):
        # inner dot lines
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

    def value_to_y(self, val):
        return 450 - 4 * float(val)