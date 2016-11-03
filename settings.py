#!/usr/bin/python
"""game settings module"""


class Settings():
    """settings container"""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (20, 20, 20)
        self.bat_width = 70
        self.bat_height = 15
        self.bat_color = (230, 230, 230)
        self.bat_speed_factor = 1
