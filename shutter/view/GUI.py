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
        self.frame.grid_columnconfigure(1, weight=3)
        self.frame.grid_rowconfigure(1, weight=2)
        self.frame.grid_columnconfigure(3, weight=3)
        self.frame.grid_rowconfigure(3, weight=2)

        # ***** BACKGROUND *****
        self.main_background = PhotoImage(file="assets/mainscreen.gif")
        self.lbl_background = Label(self.frame, image=self.main_background)
        self.lbl_background.image = self.main_background
        self.lbl_background.grid(row=2, column=2, sticky=E)

        # ***** CONNECT BUTTON *****
        self.btn_connect = Button(self.frame, text='Make connection', width=14, command=lambda: self.c.connect())
        self.btn_connect.grid(row=2, column=2, padx=5, pady=5)
        self.btn_connect.config(font=("", 30))

        # ***** STATUS BAR *****
        self.status = Label(self.master, text="disconnected", bd=1, bg="white", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    # updates the status bar with connection status
    def update_connection_status(self, status: bool):
        self.status['text'] = "connected" if status else "disconnected"



