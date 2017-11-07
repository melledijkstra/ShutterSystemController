from shutter.controller import Controller
from shutter.model import Model
from shutter.view import GUI

if __name__ == '__main__':
    view = GUI()
    model = Model()
    controller = Controller(view, model)
