from tkinter import *
from shutter.view.chart import Chart
from shutter.view.tabs import Tab

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

        # ***** CONNECT BUTTON *****
        self.btn_connect = Button(self.frame, text='Make connection', width=14, command=lambda: self.c.connect())
        self.btn_connect.grid(row=1, column=10, padx=5, pady=5, sticky=W)
        self.btn_connect.config(font=("", 11))

        # ***** STATUS BAR *****
        self.status = Label(self.master, text="-", bd=1, bg="white", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    # updates the status bar with connection status
    def update_connection_status(self, status: bool):
        self.status['text'] = "connected" if status else "disconnected"



