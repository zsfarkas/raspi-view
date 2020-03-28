from enum import Enum
import time
from gpiozero import LED, Button

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

class Controller(object):
    def __init__(self, push_handler, port=1, address=0x3C):
        self.led_red = LED(6)
        self.led_red.on()
        self.led_blue = LED(12)
        self.led_blue.blink()
        self.button = Button(5)

        self.button.when_activated = push_handler

        serial = i2c(port=1, address=0x3C)
        self.device = sh1106(serial)

    def get_canvas(self):
        return canvas(self.device) 

    def get_device_bounding_box(self):
        return self.device.bounding_box
