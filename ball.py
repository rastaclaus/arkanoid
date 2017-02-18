#!/usr/bin/python
import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.speed_factor = 1
        self.y_dir = 1
        self.x_speed = 0

    def update(self):
        self.rect.centery += self.speed_factor * self.y_dir
        self.rect.centerx += self.x_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
