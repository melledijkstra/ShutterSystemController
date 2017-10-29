from tkinter import *
from Controller.Controller.Controller import *

class GUI:

    def __init__(self, master):
        frame = Frame(master, width=300, height=250, bg="white")
        frame.pack()
        self.is_updated = False
        c = Controller()


        # ***** LOGOS *****
        logo_light = PhotoImage(file="light.GIF")
        label_light = Label(frame, image=logo_light, bg="white")
        label_light.image=logo_light
        label_light.grid(row=1, column=0)

        logo_temp = PhotoImage(file="temp.GIF")
        label_temp = Label(frame, image=logo_temp, bg="white")
        label_temp.image=logo_temp
        label_temp.grid(row=2, column=0)

        logo_light = PhotoImage(file="light.GIF")
        label_light = Label(frame, image=logo_light, bg="white")
        label_light.image = logo_light
        label_light.grid(row=1, column=3, sticky=E)

        logo_temp = PhotoImage(file="temp.GIF")
        label_temp = Label(frame, image=logo_temp, bg="white")
        label_temp.image = logo_temp
        label_temp.grid(row=2, column=3, sticky=E)


        # ***** STATUS *****
        label_status = Label(frame, text='STATUS', bg="white")
        label_status.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        label_status.config(font=(20))

        label_light = Label(frame, text='Lightintensity:', bg="white")
        label_light.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        label_temp = Label(frame, text='Temperature:', bg="white")
        label_temp.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        label_rolled = Label(frame, text='Rolled:', bg="white")
        label_rolled.grid(row=3, column=1, padx=5, pady=5, sticky=W)



        # ***** STATUS OUTPUT *****
        label_light = Label(frame, bg="white", text="light_val"' %')
        label_light.grid(row=1, column=2, padx=5, pady=5, sticky=E)

        label_temp = Label(frame, bg="white", text="temp_val"' °C')
        label_temp.grid(row=2, column=2, padx=5, pady=5, sticky=E)

        label_rolled = Label(frame, bg="white", text="roll_val")
        label_rolled.grid(row=3, column=2, padx=5, pady=5, sticky=E)


        # ***** SETTINGS *****
        label_settings = Label(frame, text='SETTINGS', bg="white")
        label_settings.grid(row=0, column=4, padx=5, pady=5, sticky=W)
        label_settings.config(font=(20))

        label_light2 = Label(frame, text='Lightintensity:', bg="white")
        label_light2.grid(row=1, column=4, padx=5, pady=5, sticky=W)

        label_temp2 = Label(frame, text='Temperature:', bg="white")
        label_temp2.grid(row=2, column=4, padx=5, pady=5, sticky=W)

        #Update Button
        button_update = Button(frame, text='Update', width=10, command=c.check_data(self.light, self.temp))
        button_update.grid(row=3, column=5, padx=5, pady=5, sticky=W)

        # ***** SETTINGS INPUT *****
        self.light = StringVar()
        entry_light = Entry(frame, width=12, bg="white", textvariable= self.light)
        entry_light.grid(row=1, column=5, padx=5, pady=5, sticky=E)
        label_entry_light = Label(frame, text='%', bg="white")
        label_entry_light.grid(row=1, column=5, padx=5, pady=5, sticky=E)

        self.temp = StringVar()
        entry_temp = Entry(frame, width=12, textvariable=self.temp)
        entry_temp.grid(row=2, column=5, padx=5, pady=5, sticky=E)
        label_entry_temp = Label(frame, text='°C', bg="white")
        label_entry_temp.grid(row=2, column=5, padx=5, pady=5, sticky=E)


        # ***** DISTANCE *****
        label_distance = Label(frame, text='Maximum Distance:', bg="white")
        label_distance.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        input_distance = Entry(frame, width=12)
        input_distance.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        cm_distance = Label(frame, text='CM', bg="white")
        cm_distance.grid(row=5, column=1, padx=5, pady=5, sticky=E)


        # ***** ROLL BUTTON *****
        roll_button = Button(frame, text='Roll out', width=12)
        roll_button.grid(row=8, column=1, padx=5, pady=5)


        # ***** CHART *****



        # ***** STATUS BAR *****
        #status = Label(frame, text="statusbar", bd=1, bg="white", relief=SUNKEN, anchor=W)
        #status.pack(side=BOTTOM, fill=X)

    '''def show_values(self, temperature, light, status):

    def is_updated(self):
        self.is_updated = True
        return self.is_updated
    '''


root = Tk()
Shutter = GUI(root)
root.mainloop()




