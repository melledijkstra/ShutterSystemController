from shutter.communication import SerialCommunication
from shutter.view import GUI
from shutter.view.subcontroller import SubController
from shutter.view.tabs import *


class Controller:
    def __init__(self, view: GUI):
        # set view
        self.view = view
        # register controller to handle ui interaction
        self.view.register(self)
        self.note = Notebook(self.view.master)
        # create serial connection
        self.comports = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7']

    def connect(self):
        for comport in self.comports:
            try:
                self.conn = SerialCommunication(comport)
                if self.conn.is_connected():
                    self.frame = Frame(self.note)
                    self.note.add(self.frame, text=comport, compound=TOP)
                    self.note.pack()
                    self.tab = Tab(self.frame)
                    self.tab.add_tab(comport)
                    self.subcontroller = SubController(self.conn, self.tab)
                    self.conn.set_listener(self.subcontroller.serial_update)
            except IOError:
                print("Nothing connected to comport: " + comport)
