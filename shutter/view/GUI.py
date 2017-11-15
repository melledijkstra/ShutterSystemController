from tkinter import *
from PIL import Image, ImageTk

class GUI:

    def __init__(self):
        self.master = Tk()
        self.master.state('zoomed')
        self.master.title = 'Shutter System'
        self.c = None

    def register(self, controller):
        self.c = controller

    def run(self):
        self.master.mainloop()

    def initialize_gui(self, frame):

        self.frame = frame

        # ***** BACKGROUND *****
        width, height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        image = Image.open("assets/mainscreen.GIF")
        # Resize image to width and height of window
        if image.size != (width, height):
            image = image.resize((width, height), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        bg_label = Label(self.frame, image=image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = image

        # ***** CONFIG COLUMNS/ROWS *****
        self.frame.grid_columnconfigure(1, weight=3)
        self.frame.grid_rowconfigure(1, weight=2)
        self.frame.grid_columnconfigure(3, weight=3)
        self.frame.grid_rowconfigure(3, weight=2)


        # ***** CONNECT BUTTON *****
        self.btn_connect = Button(self.frame, text='Make connection', relief=SOLID, borderwidth=4, width=14, command=lambda: self.c.connect())
        self.btn_connect.grid(row=2, column=2, padx=5, pady=5)
        self.btn_connect.config(font=("", 12))

        # ***** STATUS BAR *****
        self.status = Label(self.master, text="disconnected", bd=1, bg="white", relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    # updates the status bar with connection status
    def update_connection_status(self, status: bool):
        self.status['text'] = "connected" if status else "disconnected"



