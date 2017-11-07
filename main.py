from shutter.controller import Controller
from shutter.model import Model
from shutter.view.GUI import GUI

if __name__ == '__main__':
    view = GUI()
    model = Model()
    controller = Controller(view, model)

    view.run()
