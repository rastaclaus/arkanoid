#!/usr/bin/python
"""bat module"""

import pygame
from pygame.sprite import Sprite


class Bat(Sprite):
    """Представление биты"""

    def __init__(self, game_settings, screen):
        """создает объект и размещает на экране"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(
            0, 0, game_settings.bat_width, game_settings.bat_height)
        self.rect.centerx = screen.get_rect().centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = screen.get_rect().bottom
        self.color = (game_settings.bat_color)
        self.speed_factor = game_settings.bat_speed_factor
        self.left_move = False
        self.right_move = False

    def update(self):
        if self.left_move and self.rect.left >= self.screen.get_rect().left:
            self.centerx -= self.speed_factor
        elif self.right_move and \
                self.rect.right <= self.screen.get_rect().right:
            self.centerx += self.speed_factor
        self.rect.centerx = int(self.centerx)

    def blitme(self):
        """Вывод биты на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
