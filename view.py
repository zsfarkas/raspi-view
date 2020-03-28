from controller import Controller

class View(object):
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_name(self):
        return "No name"

    def update(self):
        pass

    def update_display(self, canvas):
        pass
