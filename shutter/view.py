from tkinter import *

class GUI:

    def __init__(self):
        self.master = Tk()
        self.c = None
        self.master.state('zoomed')
        self.master.title = ('Shutter System')

    def set_controller(self, controller):
        self.c = controller

    def run(self):
        self.master.mainloop()

    def structure_gui(self):
        self.frame = Frame(self.master, bg="white")
        self.frame.pack(fill=BOTH, expand=1)

        self.frame.grid_columnconfigure(4, weight=3)
        self.frame.grid_columnconfigure(11, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(9, weight=1)
        self.frame.grid_rowconfigure(6, weight=1)



        # ***** LOGOS *****
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=1)

        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=2, column=1, sticky=E)

        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=4, sticky=E)

        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=2, column=4, sticky=E)

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
        self.lbl_light = Label(self.frame, bg="white", text="light_val"' %')
        self.lbl_light.grid(row=1, column=3, padx=5, pady=5, sticky=E)

        self.lbl_temp = Label(self.frame, bg="white", text="temp_val"' °C')
        self.lbl_temp.grid(row=2, column=3, padx=5, pady=5, sticky=E)

        self.lbl_rolled = Label(self.frame, bg="white", text="roll_val")
        self.lbl_rolled.grid(row=3, column=3, padx=5, pady=5, sticky=E)

        # ***** SETTINGS *****
        self.lbl_settings = Label(self.frame, text='SETTINGS', bg="white")
        self.lbl_settings.grid(row=0, column=7, padx=5, pady=5, sticky=W)
        self.lbl_settings.config(font=("", 30))

        self.lbl_light2 = Label(self.frame, text='Lightintensity:', bg="white")
        self.lbl_light2.grid(row=1, column=7, padx=5, pady=5, sticky=W)
        self.lbl_light2.config(font=("", 12))

        self.lbl_temp2 = Label(self.frame, text='Temperature:', bg="white")
        self.lbl_temp2.grid(row=2, column=7, padx=5, pady=5, sticky=W)
        self.lbl_temp2.config(font=("", 12))

        self.lbl_distance_min = Label(self.frame, text='Minimum Roll Distance:', bg="white")
        self.lbl_distance_min.grid(row=3, column=7, padx=5, pady=5, sticky=W)
        self.lbl_distance_min.config(font=("", 12))

        self.lbl_distance_max = Label(self.frame, text='Maximum Roll Distance:', bg="white")
        self.lbl_distance_max.grid(row=4, column=7, padx=5, pady=5, sticky=W)
        self.lbl_distance_max.config(font=("", 12))

        # Update Button
        self.btn_update = Button(self.frame, text='Update', width=35, command=self.c.update)
        self.btn_update.grid(row=5, column=7, columnspan=2, padx=5, pady=5, sticky=W)
        self.btn_update.config(font=("", 11))



        # ***** SETTINGS INPUT *****
            #light
        self.entry_light = Entry(self.frame, width=12, bg="white")
        self.entry_light.grid(row=1, column=8, padx=5, pady=5, sticky=E)
        self.entry_light.config(font=("", 11))
        self.lbl_entry_light = Label(self.frame, text='%', bg="white")
        self.lbl_entry_light.grid(row=1, column=8, padx=5, pady=5, sticky=E)
        self.lbl_entry_light.config(font=("", 11))
            #temp
        self.entry_temp = Entry(self.frame, width=12)
        self.entry_temp.grid(row=2, column=8, padx=5, pady=5, sticky=E)
        self.entry_temp.config(font=("", 11))
        self.lbl_entry_temp = Label(self.frame, text='°C', bg="white")
        self.lbl_entry_temp.grid(row=2, column=8, padx=5, pady=5, sticky=E)
        self.lbl_entry_temp.config(font=("", 11))
            #distance
        self.input_distance_min = Entry(self.frame, width=12)
        self.input_distance_min.grid(row=3, column=8, padx=5, pady=5, sticky=E)
        self.input_distance_min.config(font=("", 11))
        self.cm_distance_min = Label(self.frame, text='CM', bg="white")
        self.cm_distance_min.grid(row=3, column=8, padx=5, pady=5, sticky=E)
        self.cm_distance_min.config(font=("", 11))

        self.input_distance_max = Entry(self.frame, width=12)
        self.input_distance_max.grid(row=4, column=8, padx=5, pady=5, sticky=E)
        self.input_distance_max.config(font=("", 11))
        self.cm_distance_max = Label(self.frame, text='CM', bg="white")
        self.cm_distance_max.grid(row=4, column=8, padx=5, pady=5, sticky=E)
        self.cm_distance_max.config(font=("", 11))

        # ***** ROLL BUTTON *****
        self.btn_roll = Button(self.frame, text='Roll out/Roll in', width=14, command=self.c.toggle_shutter)
        self.btn_roll.grid(row=4, column=10, padx=5, pady=5)
        self.btn_roll.config(font=("", 11))

        # Update Button
        self.btn_connect = Button(self.frame, text='Make connection', width=14, command=self.c.connect)
        self.btn_connect.grid(row=1, column=10, padx=5, pady=5, sticky=W)
        self.btn_connect.config(font=("", 11))

        # ***** CHART *****


        # ***** STATUS BAR *****
        self.status = Label(self.master, text="connected" if self.c.is_connected() else "disconnected", bd=1, bg="white", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def update_connection_status(self, status: bool):
        self.status['text'] = "connected" if status else "disconnected"

    def update(self, temp, light, status):
        self.lbl_temp['text'] = temp
        self.lbl_light['text'] = light
        if status == 0:
            self.lbl_status['text'] = "Rolled up"
        else:
            self.lbl_status['text'] = "Rolled down"



