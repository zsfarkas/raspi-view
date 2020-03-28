from view import View
from controller import Controller

class DefaultView(View):
    def __init__(self, controller: Controller):
        super().__init__(controller)

    def update_display(self, canvas, bounding_box):
        canvas.rectangle(bounding_box, outline="white", fill="black")
        canvas.text((30, 40), "Hello World", fill="white")

    def get_name(self):
        return "Default View"

