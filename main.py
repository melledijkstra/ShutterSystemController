from shutter.controller import Controller
from shutter.view.GUI import GUI

if __name__ == '__main__':
    view = GUI()
    controller = Controller(view)
    view.run()
