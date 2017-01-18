#!/usr/bin/python
import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen = screen
        self.radius = 10
        self.centerx = 400
        self.centery = 10
        self.color = (40, 230, 40)
        self.speed_factor = 1

    def update(self):
        pass

    def draw_ball(self):
        pygame.draw.circle(self.screen,
                           self.color,
                           (self.centerx, self.centery),
                           self.radius)
