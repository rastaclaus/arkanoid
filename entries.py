# -*- coding=UTF-8 -*-
class Ball():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.life_time = 0

    def change_xspeed(self, xv):
        self.x_velocity += xv

    def change_yspeed(self, yv):
        self.y_velocity += yv

    def update_position(self, delta_time=1):
        self.life_time += delta_time
        self.x += self.x_velocity * delta_time
        self.y += self.y_velocity * delta_time

    def get_position(self):
        return self.x, self.y

    def teleport(self, x, y):
        self.x, self.y = x, y


class Ball_view(Ball):
    def __init__(self, x, y, radius, screen):
        super().__init__(x, y, radius)
        self.screen = screen

    def blitme(self):
        self.screen
