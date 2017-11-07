from tkinter import *
import time

class GUI:

    def __init__(self):
        self.master = Tk()
        self.master.state('zoomed')
        self.master.title = 'Shutter System'
        self.initialize_gui()
        self.c = None

    def register(self, controller):
        self.c = controller

    def run(self):
        self.master.mainloop()

    def initialize_gui(self):
        self.frame = Frame(self.master, bg="white")
        self.frame.pack(fill=BOTH, expand=1)

        # ***** CONFIG COLUMNS/ROWS *****
        self.frame.grid_columnconfigure(6, weight=3)
        self.frame.grid_columnconfigure(11, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(9, weight=1)
        self.frame.grid_rowconfigure(12, weight=2)

        # ***** LOGOS *****
        #Icon light status
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=1)

        #Icon temp status
        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=2, column=1, sticky=E)

        #Icon light settings 1
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=6, pady=5, sticky=SE)
        # Icon light settings 2
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=2, column=6, sticky=E)

        #Icon temp settings 1
        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=3, column=6, sticky=E)

        #Icon temp settings 2
        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=4, column=6, sticky=E)

        #Icon distance status
        self.logo_distance = PhotoImage(file="assets/distance.GIF")
        self.lbl_distance = Label(self.frame, image=self.logo_distance, bg="white")
        self.lbl_distance.image = self.logo_distance
        self.lbl_distance.grid(row=3, column=1, sticky=E)

        #Icon distance settings min
        self.logo_distance = PhotoImage(file="assets/distance.GIF")
        self.lbl_distance = Label(self.frame, image=self.logo_distance, bg="white")
        self.lbl_distance.image = self.logo_distance
        self.lbl_distance.grid(row=5, column=6, sticky=E)

        #Icon distance settings max
        self.logo_distance = PhotoImage(file="assets/distance.GIF")
        self.lbl_distance = Label(self.frame, image=self.logo_distance, bg="white")
        self.lbl_distance.image = self.logo_distance
        self.lbl_distance.grid(row=6, column=6, sticky=E)


        # ***** STATUS *****
        self.lbl_status = Label(self.frame, text='STATUS', bg="white")
        self.lbl_status.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.lbl_status.config(font=("", 30))

        self.lbl_light = Label(self.frame, text='Lightintensity:', bg="white")
        self.lbl_light.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.lbl_light.config(font=("", 12))

        self.lbl_temp = Label(self.frame, text='Temperature:', bg="white")
        self.lbl_temp.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        self.lbl_temp.config(font=("", 12))

        self.lbl_rolled = Label(self.frame, text='Rolled:', bg="white")
        self.lbl_rolled.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        self.lbl_rolled.config(font=("", 12))

        # ***** STATUS OUTPUT *****
        #Show light intensity in %
        self.lbl_light = Label(self.frame, bg="white", textvariable="light_val", text=" %")
        self.lbl_light.grid(row=1, column=3, padx=5, pady=5, sticky=E)
        self.lbl_light.config(font=("", 12))

        #Show temperature in celsius
        self.lbl_temp = Label(self.frame, bg="white", textvariable="temp_val", text=" °C")
        self.lbl_temp.grid(row=2, column=3, padx=5, pady=5, sticky=E)
        self.lbl_temp.config(font=("", 12))

        #Rolled out/Rolled in depending on status shutter
        self.lbl_rolled = Label(self.frame, bg="white", textvariable="roll_val")
        self.lbl_rolled.grid(row=3, column=3, padx=5, pady=5, sticky=E)
        self.lbl_rolled.config(font=("", 12))

        # ***** SETTINGS *****
        self.lbl_settings = Label(self.frame, text='SETTINGS', bg="white")
        self.lbl_settings.grid(row=0, column=7, padx=5, pady=5, sticky=W)
        self.lbl_settings.config(font=("", 30))

        self.lbl_light_min = Label(self.frame, text='Minimum Lightintensity:', bg="white")
        self.lbl_light_min.grid(row=1, column=7, padx=5, pady=5, sticky=SW)
        self.lbl_light_min.config(font=("", 12))

        self.lbl_light_max = Label(self.frame, text='Maximum Lightintensity:', bg="white")
        self.lbl_light_max.grid(row=2, column=7, padx=5, pady=5, sticky=W)
        self.lbl_light_max.config(font=("", 12))

        self.lbl_temp_min = Label(self.frame, text='Minimum Temperature:', bg="white")
        self.lbl_temp_min.grid(row=3, column=7, padx=5, pady=5, sticky=W)
        self.lbl_temp_min.config(font=("", 12))

        self.lbl_temp_max = Label(self.frame, text='Maximum Temperature:', bg="white")
        self.lbl_temp_max.grid(row=4, column=7, padx=5, pady=5, sticky=W)
        self.lbl_temp_max.config(font=("", 12))

        self.lbl_distance_min = Label(self.frame, text='Minimum Roll Distance:', bg="white")
        self.lbl_distance_min.grid(row=5, column=7, padx=5, pady=5, sticky=W)
        self.lbl_distance_min.config(font=("", 12))

        self.lbl_distance_max = Label(self.frame, text='Maximum Roll Distance:', bg="white")
        self.lbl_distance_max.grid(row=6, column=7, padx=5, pady=5, sticky=W)
        self.lbl_distance_max.config(font=("", 12))

        # Input error label
        self.light_error = StringVar()
        self.temp_error = StringVar()
        self.min_error = StringVar()
        self.max_error =StringVar()

        self.lbl_light_error = Label(self.frame, textvariable=self.light_error, bg="white", fg="red")
        self.lbl_light_error.grid(row=6, column=7, columnspan=2, rowspan=3)
        self.lbl_temp_error = Label(self.frame, textvariable=self.temp_error, bg="white", fg="red")
        self.lbl_temp_error.grid(row=6, column=7, columnspan=2, rowspan=3)
        self.lbl_min_error = Label(self.frame, textvariable=self.min_error, bg="white", fg="red")
        self.lbl_min_error.grid(row=6, column=7, columnspan=2, rowspan=3)
        self.lbl_max_error = Label(self.frame, textvariable=self.max_error, bg="white", fg="red")
        self.lbl_max_error.grid(row=6, column=7, columnspan=2, rowspan=3)

        # ***** SETTINGS INPUT *****
        #min light
        self.light_min_entry = IntVar()
        self.entry_light_min = Entry(self.frame, width=12, textvariable=self.light_min_entry)
        self.entry_light_min.grid(row=1, column=8, padx=5, pady=5, sticky=SE)
        self.entry_light_min.config(font=("", 11))
        self.lbl_entry_light_min = Label(self.frame, text='%', bg="white")
        self.lbl_entry_light_min.grid(row=1, column=8, padx=5, pady=5, sticky=SE)
        self.lbl_entry_light_min.config(font=("", 11))

        #max light
        self.light_max_entry = IntVar()
        self.entry_light_max = Entry(self.frame, width=12, textvariable=self.light_max_entry)
        self.entry_light_max.grid(row=2, column=8, padx=5, pady=5, sticky=E)
        self.entry_light_max.config(font=("", 11))
        self.lbl_entry_light_max = Label(self.frame, text='%', bg="white")
        self.lbl_entry_light_max.grid(row=2, column=8, padx=5, pady=5, sticky=E)
        self.lbl_entry_light_max.config(font=("", 11))

        #min temp
        self.min_temp_entry = IntVar()
        self.entry_temp_min = Entry(self.frame, width=12, textvariable=self.min_temp_entry)
        self.entry_temp_min.grid(row=3, column=8, padx=5, pady=5, sticky=E)
        self.entry_temp_min.config(font=("", 11))
        self.lbl_entry_temp_min = Label(self.frame, text='°C', bg="white")
        self.lbl_entry_temp_min.grid(row=3, column=8, padx=5, pady=5, sticky=E)
        self.lbl_entry_temp_min.config(font=("", 11))

        #max temp
        self.max_temp_entry = IntVar()
        self.entry_temp_max = Entry(self.frame, width=12, textvariable=self.max_temp_entry)
        self.entry_temp_max.grid(row=4, column=8, padx=5, pady=5, sticky=E)
        self.entry_temp_max.config(font=("", 11))
        self.lbl_entry_temp_max = Label(self.frame, text='°C', bg="white")
        self.lbl_entry_temp_max.grid(row=4, column=8, padx=5, pady=5, sticky=E)
        self.lbl_entry_temp_max.config(font=("", 11))

        #min distance
        self.min_distance_entry = IntVar()
        self.input_distance_min = Entry(self.frame, width=12, textvariable=self.min_distance_entry)
        self.input_distance_min.grid(row=5, column=8, padx=5, pady=5, sticky=E)
        self.input_distance_min.config(font=("", 11))
        self.cm_distance_min = Label(self.frame, text='CM', bg="white")
        self.cm_distance_min.grid(row=5, column=8, padx=5, pady=5, sticky=E)
        self.cm_distance_min.config(font=("", 11))

        #max distance
        self.max_distance_entry = IntVar()
        self.input_distance_max = Entry(self.frame, width=12, textvariable=self.max_distance_entry)
        self.input_distance_max.grid(row=6, column=8, padx=5, pady=5, sticky=E)
        self.input_distance_max.config(font=("", 11))
        self.cm_distance_max = Label(self.frame, text='CM', bg="white")
        self.cm_distance_max.grid(row=6, column=8, padx=5, pady=5, sticky=E)
        self.cm_distance_max.config(font=("", 11))

        # ***** ROLL BUTTON *****
        self.btn_roll = Button(self.frame, text='Roll out/Roll in', width=14, command=lambda: self.c.toggle_shutter)
        self.btn_roll.grid(row=2, column=10, padx=5, pady=5, sticky=W)
        self.btn_roll.config(font=("", 11))

        # ***** CONNECT BUTTON *****
        self.btn_connect = Button(self.frame, text='Make connection', width=14, command=lambda: self.c.connect)
        self.btn_connect.grid(row=1, column=10, padx=5, pady=5, sticky=W)
        self.btn_connect.config(font=("", 11))

        # Update Settings button
        self.btn_update = Button(self.frame, text='Update Settings',width=14 , command=lambda: self.c.update)
        self.btn_update.grid(row=6, column=10, columnspan=2, padx=5, pady=5, sticky=W)
        self.btn_update.config(font=("", 11))

        # ***** CHART *****
        self.running = True
        self.minimum = 0
        self.maximum = 100
        self.f = 1
        self.x_temp_2 = 50
        self.y_temp_2 = 0   #temp_value
        self.x_light_2 = 50
        self.y_light_2 = 0    #light_value

        self.canvas = Canvas(self.frame, width=1400, height=490, bg='white')  # 0,0 is top left corner
        self.canvas.grid(row=10, column=0, rowspan=2, columnspan=12)

        #Outer lines
        self.canvas.create_line(50, 450, 1350, 450, width=2)  # x-axis
        self.canvas.create_line(50, 450, 50, 50, width=2)  # y-axis

        #inner dot lines
        #x-axis
        for i in range(27):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 450, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 450, text='%d' % (1 * i), anchor=N)
        self.canvas.create_text(60, 470, text='Time (minutes)', anchor=N)
        #y-axis
        for i in range(11):
            y = 450 - (i * 40)
            self.canvas.create_line(50, y, 1350, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)
        self.canvas.create_text(20, 440, text='Value', anchor=E, angle=90)

        # ***** CHART LEGEND *****
        self.lbl_lgd = Label(self.frame, text="LEGEND", bg="white")
        self.lbl_lgd.grid(row=5, column=2, padx=5, pady=5, sticky=SW)
        self.lbl_lgd.config(font=("", 16))
        #label temperature
        self.lbl_lgd_temp = Label(self.frame, text="Temperature: ", bg="white")
        self.lbl_lgd_temp.grid(row=6, column=2, padx=5, pady=5, sticky=W)
        self.lbl_lgd_temp.config(font=("", 12))
        #label red line
        self.logo_red = PhotoImage(file="assets/redline.GIF")
        self.lbl_red = Label(self.frame, image=self.logo_red, bg="white")
        self.lbl_red.image = self.logo_red
        self.lbl_red.grid(row=6, column=3, sticky=W)
        #label light
        self.lbl_lgd_light = Label(self.frame, text="Light intensity: ", bg="white")
        self.lbl_lgd_light.grid(row=6, column=4, padx=5, pady=5, sticky=W)
        self.lbl_lgd_light.config(font=("", 12))
        #label yellow line
        self.logo_yellow = PhotoImage(file="assets/yellowline.GIF")
        self.lbl_yellow = Label(self.frame, image=self.logo_yellow, bg="white")
        self.lbl_yellow.image = self.logo_yellow
        self.lbl_yellow.grid(row=6, column=5)

        # ***** STATUS BAR *****
        self.status = Label(self.master, text="disconnected", bd=1, bg="white", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    # updates the status bar with connection status
    def update_connection_status(self, status: bool):
        self.status['text'] = "connected" if status else "disconnected"

    def update(self, temp, light, status):
        #update light and temp status
        self.lbl_temp['text'] = temp
        self.lbl_light['text'] = light
        #update rolled status
        if status == 0:
            self.lbl_rolled['text'] = "Rolled up"
        else:
            self.lbl_rolled['text'] = "Rolled down"
        #add values to graph
        self.x_temp_2 = temp
        self.x_light_2 = light
        self. step_chart()

    # chart steps
    def step_chart(self):
        if self.f == 27:
            # new frame
            self.f = 1
            self.x_temp_2 = 50
            self.x_light_2 = 50
            self.canvas.delete('temp')  # only delete items tagged as temp

        #draw temperature line
        x_temp_1 = self.x_temp_2
        y_temp_1 = self.y_temp_2
        self.x_temp_2 = 50 + self.f * 50
        #self.y_temp_2 = 250         #temp_value
        self.canvas.create_line(x_temp_1, y_temp_1, self.x_temp_2, self.y_temp_2, fill='red',width=3, tags='temp')
        #draw light intensity line
        x_light_1 = self.x_light_2
        y_light_1 = self.y_light_2
        self.x_light_2 = 50 + self.f * 50
        #self.y_light_2 = 290        #light_value
        self.canvas.create_line(x_light_1, y_light_1, self.x_light_2, self.y_light_2, fill='yellow',width=3 , tags='temp')

        self.f += 1
        self.id = self.canvas.after(300, self.step_chart)