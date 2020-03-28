from default_view import DefaultView
from test_view import TestView
from controller import Controller
from time import sleep

class MainLoop:
    def __init__(self, view_classes):
        self.controller = Controller(self._activate_next_view)

        self.views = self._init_view_classes(self.controller, view_classes)
        self.current_view_index = 0

    def _init_view_classes(self, controller: Controller, view_classes):
        views = []
        for view_class in view_classes:
            print("adding view " + str(view_classes) + "...")
            views.append(view_class(controller))
        
        return views

    def _activate_next_view(self):
        if self.current_view_index + 1 >= len(self.views):
            self.current_view_index = 0
        else: 
            self.current_view_index += 1

        print("view activated: '" + self._get_current_view().get_name() + "'")

    def spin(self):
        print("starting main loop...")
        try:
            while True:
                if self._get_current_view() != None:
                    with self.controller.get_canvas() as canvas:
                        bounding_box = self.controller.get_device_bounding_box()
                        self._get_current_view().update_display(canvas, bounding_box)

                for view in self.views:
                    view.update()

                sleep(0.1)
        except (KeyboardInterrupt):
            print("\nshutting down...")

    def _get_current_view(self):
        return self.views[self.current_view_index]


if __name__ == "__main__":
    view_classes = [
        DefaultView,
        TestView
    ]

    main_loop = MainLoop(view_classes=view_classes)
    main_loop.spin()
