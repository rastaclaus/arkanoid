#!/usr/bin/python
"""bat module"""

import pygame
from pygame.sprite import Sprite


class Bat(Sprite):
    """Представление биты"""

    def __init__(self, ball_settings, screen):
        """создает объект и размещает на экране"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(
            0, 0, ball_settings.bat_width, ball_settings.bat_height)
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom
        self.color = (ball_settings.bat_color)
        self.speed_factor = ball_settings.bat_speed_factor
        self.left_move = False
        self.reght_move = False

    def update(self):
        pass

    def draw_bat(self):
        """Вывод биты на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
