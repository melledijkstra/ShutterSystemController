from tkinter import *

class GUI:

    def __init__(self):
        self.master = Tk()
        self.c = None

    def set_controller(self, controller):
        self.c = controller

    def run(self):
        self.master.mainloop()

    def structure_gui(self):
        self.frame = Frame(self.master, width=1000, height=600, bg="white")
        self.frame.pack()

        # ***** LOGOS *****
        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=0)

        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=2, column=0)

        self.logo_light = PhotoImage(file="assets/light.GIF")
        self.lbl_light = Label(self.frame, image=self.logo_light, bg="white")
        self.lbl_light.image = self.logo_light
        self.lbl_light.grid(row=1, column=3, sticky=E)

        self.logo_temp = PhotoImage(file="assets/temp.GIF")
        self.lbl_temp = Label(self.frame, image=self.logo_temp, bg="white")
        self.lbl_temp.image = self.logo_temp
        self.lbl_temp.grid(row=2, column=3, sticky=E)

        # ***** STATUS *****
        self.lbl_status = Label(self.frame, text='STATUS', bg="white")
        self.lbl_status.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.lbl_status.config(font=(20))

        self.lbl_light = Label(self.frame, text='Lightintensity:', bg="white")
        self.lbl_light.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.lbl_temp = Label(self.frame, text='Temperature:', bg="white")
        self.lbl_temp.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.lbl_rolled = Label(self.frame, text='Rolled:', bg="white")
        self.lbl_rolled.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # ***** STATUS OUTPUT *****
        self.lbl_light = Label(self.frame, bg="white", text="light_val"' %')
        self.lbl_light.grid(row=1, column=2, padx=5, pady=5, sticky=E)

        self.lbl_temp = Label(self.frame, bg="white", text="temp_val"' °C')
        self.lbl_temp.grid(row=2, column=2, padx=5, pady=5, sticky=E)

        self.lbl_rolled = Label(self.frame, bg="white", text="roll_val")
        self.lbl_rolled.grid(row=3, column=2, padx=5, pady=5, sticky=E)

        # ***** SETTINGS *****
        self.lbl_settings = Label(self.frame, text='SETTINGS', bg="white")
        self.lbl_settings.grid(row=0, column=4, padx=5, pady=5, sticky=W)
        self.lbl_settings.config(font=(20))

        self.lbl_light2 = Label(self.frame, text='Lightintensity:', bg="white")
        self.lbl_light2.grid(row=1, column=4, padx=5, pady=5, sticky=W)

        self.lbl_temp2 = Label(self.frame, text='Temperature:', bg="white")
        self.lbl_temp2.grid(row=2, column=4, padx=5, pady=5, sticky=W)

        # Update Button
        self.btn_update = Button(self.frame, text='Update', width=10, command=self.c.update)
        self.btn_update.grid(row=3, column=5, padx=5, pady=5, sticky=W)

        # Update Button
        self.btn_update = Button(self.frame, text='Make connection', width=10, command=self.c.connect)
        self.btn_update.grid(row=3, column=6, padx=5, pady=5, sticky=W)

        # ***** SETTINGS INPUT *****
        self.entry_light = Entry(self.frame, width=12, bg="white")
        self.entry_light.grid(row=1, column=5, padx=5, pady=5, sticky=E)
        self.lbl_entry_light = Label(self.frame, text='%', bg="white")
        self.lbl_entry_light.grid(row=1, column=5, padx=5, pady=5, sticky=E)

        self.entry_temp = Entry(self.frame, width=12)
        self.entry_temp.grid(row=2, column=5, padx=5, pady=5, sticky=E)
        self.lbl_entry_temp = Label(self.frame, text='°C', bg="white")
        self.lbl_entry_temp.grid(row=2, column=5, padx=5, pady=5, sticky=E)

        # ***** DISTANCE *****
        self.lbl_distance = Label(self.frame, text='Maximum Distance:', bg="white")
        self.lbl_distance.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        self.input_distance = Entry(self.frame, width=12)
        self.input_distance.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        self.cm_distance = Label(self.frame, text='CM', bg="white")
        self.cm_distance.grid(row=5, column=1, padx=5, pady=5, sticky=E)

        # ***** ROLL BUTTON *****
        self.btn_roll = Button(self.frame, text='Roll out', width=12, command=self.c.toggle_shutter)
        self.btn_roll.grid(row=8, column=1, padx=5, pady=5)

        # ***** CHART *****


        # ***** STATUS BAR *****
        self.status = Label(self.master, text="connected" if self.c.isConnected() else "disconnected", bd=1, bg="white", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def update_connection_status(self, status: bool):
        self.status['text'] = "connected" if status else "disconnected"
