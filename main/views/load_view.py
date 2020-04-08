import time
from gpiozero import DiskUsage, LoadAverage, CPUTemperature
from main.view import View
from main.controller import Controller
from threading import Thread

class LoadView(View):
    def __init__(self, controller: Controller):
        super().__init__(controller)

        self.cpu_temperature = CPUTemperature()
        self.cpu_load = LoadAverage()
        self.disk_usage = DiskUsage()

        self.status_cache = []
        self.global_status = False
        self.last_check = 0

    def get_warning_count(self):
        return (0, 0)

    def update_display(self, canvas, bounding_box):
        canvas.text((0,0), "CPU Load: %.2f %%" % (self.cpu_load.load_average / 4.0 * 100) , fill="white")
        canvas.text((0,10), "CPU Temp: %.2f °C" % self.cpu_temperature.temperature , fill="white")
        canvas.text((0,20), "Disk Usage: %.2f %%" % self.disk_usage.usage, fill="white")

    def get_name(self) -> str:
        return "Load View"
