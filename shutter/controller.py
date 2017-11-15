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
        self.style_notebook()
        self.note = Notebook(self.view.master)
        self.frame = Frame(self.note)
        self.note.add(self.frame, text="Main Screen", compound=TOP)
        self.note.pack()
        self.view.initialize_gui(self.frame)
        # create serial connection
        self.comports = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5']

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

    def style_notebook(self):
        _bgcolor = 'white'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4'  # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2'  # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2'  # Closest X11 color: 'RosyBrown2'
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
        self.style = Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font=font10)
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])
        self.view.master.configure(background=_bgcolor)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
        [('selected', _compcolor), ('active', _ana2color)])
