from tkinter import *
from tkinter.ttk import *
from shutter.view.chart import Chart


class Tab:
    def __init__(self, frame):
        self.frame = frame

        self.c = None

    def register(self, controller):
        self.c = controller

    def add_tab(self, tabname):

        # ***** LOGOS *****
        # Icon light status
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light)
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=1, sticky=E)

        # Icon temp status
        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp)
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=2, column=1, sticky=E)

        # Icon light settings 1
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light)
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=6, pady=5, sticky=E)
        # Icon light settings 2
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light)
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=2, column=6, sticky=E)

        # Icon temp settings 1
        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp)
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=3, column=6, sticky=E)

        # Icon temp settings 2
        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp)
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=4, column=6, sticky=E)

        # Icon distance status
        self.logo_distance = PhotoImage(file="assets/distance.GIF")
        self.lbl_distance = Label(self.frame, image=self.logo_distance)
        self.lbl_distance.image = self.logo_distance
        self.lbl_distance.grid(row=3, column=1, sticky=E)

        # Icon distance settings min
        self.logo_distance = PhotoImage(file="assets/distance.GIF")
        self.lbl_distance = Label(self.frame, image=self.logo_distance)
        self.lbl_distance.image = self.logo_distance
        self.lbl_distance.grid(row=5, column=6, sticky=E)

        # Icon distance settings max
        self.logo_distance = PhotoImage(file="assets/distance.GIF")
        self.lbl_distance = Label(self.frame, image=self.logo_distance)
        self.lbl_distance.image = self.logo_distance
        self.lbl_distance.grid(row=6, column=6, sticky=E)

        # ***** STATUS *****
        self.lbl_status = Label(self.frame, text='STATUS')
        self.lbl_status.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        # self.lbl_status.config(("", 30))

        self.lbl_light = Label(self.frame, text='Lightintensity:')
        self.lbl_light.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        # self.lbl_light.config(("", 12))

        self.lbl_temp = Label(self.frame, text='Temperature:')
        self.lbl_temp.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        # self.lbl_temp.config(("", 12))

        self.lbl_rolled = Label(self.frame, text='Rolled:')
        self.lbl_rolled.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        # self.lbl_rolled.config(("", 12))

        # ***** STATUS OUTPUT *****
        # Show light intensity in %
        self.lbl_light = Label(self.frame, text=" %")
        self.lbl_light.grid(row=1, column=3, padx=5, pady=5, sticky=E)
        # self.lbl_light.config(("", 12))

        # Show temperature in celsius
        self.lbl_temp = Label(self.frame, text=" °C")
        self.lbl_temp.grid(row=2, column=3, padx=5, pady=5, sticky=E)
        # self.lbl_temp.config(("", 12))

        # Rolled out/Rolled in depending on status shutter
        self.lbl_rolled = Label(self.frame, text="")
        self.lbl_rolled.grid(row=3, column=3, padx=5, pady=5, sticky=E)
        # self.lbl_rolled.config(("", 12))

        # ***** SETTINGS *****
        self.lbl_settings = Label(self.frame, text='SETTINGS')
        self.lbl_settings.grid(row=0, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_settings.config(("", 30))

        self.lbl_light_min = Label(self.frame, text='Minimum Lightintensity:')
        self.lbl_light_min.grid(row=1, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_light_min.config(("", 12))

        self.lbl_light_max = Label(self.frame, text='Maximum Lightintensity:')
        self.lbl_light_max.grid(row=2, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_light_max.config(("", 12))

        self.lbl_temp_min = Label(self.frame, text='Minimum Temperature:')
        self.lbl_temp_min.grid(row=3, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_temp_min.config(("", 12))

        self.lbl_temp_max = Label(self.frame, text='Maximum Temperature:')
        self.lbl_temp_max.grid(row=4, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_temp_max.config(("", 12))

        self.lbl_distance_min = Label(self.frame, text='Minimum Roll Distance:')
        self.lbl_distance_min.grid(row=5, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_distance_min.config(("", 12))

        self.lbl_distance_max = Label(self.frame, text='Maximum Roll Distance:')
        self.lbl_distance_max.grid(row=6, column=7, padx=5, pady=5, sticky=W)
        # self.lbl_distance_max.config(("", 12))

        # Input error label
        self.light_error = StringVar()
        self.temp_error = StringVar()
        self.min_error = StringVar()
        self.max_error = StringVar()

        self.lbl_light_error = Label(self.frame, textvariable=self.light_error)
        self.lbl_light_error.grid(row=5, column=10, columnspan=2, rowspan=3)
        self.lbl_temp_error = Label(self.frame, textvariable=self.temp_error)
        self.lbl_temp_error.grid(row=5, column=10, columnspan=2, rowspan=3)
        self.lbl_min_error = Label(self.frame, textvariable=self.min_error)
        self.lbl_min_error.grid(row=5, column=10, columnspan=2, rowspan=3)
        self.lbl_max_error = Label(self.frame, textvariable=self.max_error)
        self.lbl_max_error.grid(row=5, column=10, columnspan=2, rowspan=3)

        # ***** SETTINGS INPUT *****
        # min light
        self.light_min_entry = IntVar()
        self.entry_light_min = Entry(self.frame, width=12, textvariable=self.light_min_entry)
        self.entry_light_min.grid(row=1, column=8, padx=5, pady=5, sticky=E)
        # self.entry_light_min.config(("", 11))
        self.lbl_entry_light_min = Label(self.frame, text='%')
        self.lbl_entry_light_min.grid(row=1, column=8, padx=5, pady=5, sticky=E)
        # self.lbl_entry_light_min.config(("", 11))

        # max light
        self.light_max_entry = IntVar()
        self.entry_light_max = Entry(self.frame, width=12, textvariable=self.light_max_entry)
        self.entry_light_max.grid(row=2, column=8, padx=5, pady=5, sticky=E)
        # self.entry_light_max.config(("", 11))
        self.lbl_entry_light_max = Label(self.frame, text='%')
        self.lbl_entry_light_max.grid(row=2, column=8, padx=5, pady=5, sticky=E)
        # self.lbl_entry_light_max.config(("", 11))

        # min temp
        self.min_temp_entry = IntVar()
        self.entry_temp_min = Entry(self.frame, width=12, textvariable=self.min_temp_entry)
        self.entry_temp_min.grid(row=3, column=8, padx=5, pady=5, sticky=E)
        # self.entry_temp_min.config(("", 11))
        self.lbl_entry_temp_min = Label(self.frame, text='°C')
        self.lbl_entry_temp_min.grid(row=3, column=8, padx=5, pady=5, sticky=E)
        # self.lbl_entry_temp_min.config(("", 11))

        # max temp
        self.max_temp_entry = IntVar()
        self.entry_temp_max = Entry(self.frame, width=12, textvariable=self.max_temp_entry)
        self.entry_temp_max.grid(row=4, column=8, padx=5, pady=5, sticky=E)
        # self.entry_temp_max.config(("", 11))
        self.lbl_entry_temp_max = Label(self.frame, text='°C')
        self.lbl_entry_temp_max.grid(row=4, column=8, padx=5, pady=5, sticky=E)
        # self.lbl_entry_temp_max.config(("", 11))

        # min distance
        self.min_distance_entry = IntVar()
        self.input_distance_min = Entry(self.frame, width=12, textvariable=self.min_distance_entry)
        self.input_distance_min.grid(row=5, column=8, padx=5, pady=5, sticky=E)
        # self.input_distance_min.config(("", 11))
        self.cm_distance_min = Label(self.frame, text='CM')
        self.cm_distance_min.grid(row=5, column=8, padx=5, pady=5, sticky=E)
        # self.cm_distance_min.config(("", 11))

        # max distance
        self.max_distance_entry = IntVar()
        self.input_distance_max = Entry(self.frame, width=12, textvariable=self.max_distance_entry)
        self.input_distance_max.grid(row=6, column=8, padx=5, pady=5, sticky=E)
        # self.input_distance_max.config(("", 11))
        self.cm_distance_max = Label(self.frame, text='CM')
        self.cm_distance_max.grid(row=6, column=8, padx=5, pady=5, sticky=E)
        # self.cm_distance_max.config(("", 11))

        # ***** ROLL BUTTON *****
        self.btn_roll = Button(self.frame, text='Roll out/Roll in', width=14, command=lambda: self.c.toggle_shutter())
        self.btn_roll.grid(row=2, column=10, padx=5, pady=5, sticky=W)
        # self.btn_roll.config(("", 11))

        # Update Settings button
        self.btn_update = Button(self.frame, text='Update Settings', width=14, command=lambda: self.c.update_settings())
        self.btn_update.grid(row=6, column=10, columnspan=2, padx=5, pady=5, sticky=W)
        # self.btn_update.config(("", 11))

        # ***** CHART *****
        self.chart = Chart(self.frame)

        # ***** CHART LEGEND *****
        self.lbl_lgd = Label(self.frame, text="LEGEND")
        self.lbl_lgd.grid(row=5, column=2, padx=5, pady=5, sticky=SW)
        # self.lbl_lgd.config(("", 16))
        # label temperature
        self.lbl_lgd_temp = Label(self.frame, text="Temperature: ")
        self.lbl_lgd_temp.grid(row=6, column=2, padx=5, pady=5, sticky=W)
        # self.lbl_lgd_temp.config(("", 12))
        # label red line
        self.logo_red = PhotoImage(file="assets/redline.GIF")
        self.lbl_red = Label(self.frame, image=self.logo_red)
        self.lbl_red.image = self.logo_red
        self.lbl_red.grid(row=6, column=3, sticky=W)
        # label light
        self.lbl_lgd_light = Label(self.frame, text="Light intensity: ")
        self.lbl_lgd_light.grid(row=6, column=4, padx=5, pady=5, sticky=W)
        # self.lbl_lgd_light.config(("", 12))
        # label yellow line
        self.logo_yellow = PhotoImage(file="assets/yellowline.GIF")
        self.lbl_yellow = Label(self.frame, image=self.logo_yellow)
        self.lbl_yellow.image = self.logo_yellow
        self.lbl_yellow.grid(row=6, column=5)

        '''# ***** STATUS BAR *****
        self.status = Label(self.tab, text="-", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)'''

    def update(self, temp, light, status, cm_status):
        # update light and temp status
        self.lbl_temp['text'] = temp + " °C"
        self.lbl_light['text'] = light + " %"
        cm_status = 'too far' if int(cm_status) < 1 else cm_status+'cm'
        if status == 0:
            self.lbl_rolled['text'] = "Rolled up (" + cm_status + ")"
        else:
            self.lbl_rolled['text'] = "Rolled down (" + cm_status + ")"
        # add values to graph
        self.chart.step(temp, light)
