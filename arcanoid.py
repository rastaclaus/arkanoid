#!/usr/bin/env python
# -*- coding=UTF-8 -*-
"""game main module"""
import pygame
import game_functions as gf
from settings import Settings
from bat import Bat
from ball import Ball


def run_game():
    """enter point"""
    game_settings = Settings()
    pygame.init()
    screen = gf.init_screen(game_settings)
    bat = Bat(game_settings, screen)
    ball = Ball(game_settings, screen)
    ball.rect.centerx = game_settings.screen_width / 2

    # main loop
    while True:
        gf.event_check(bat)
        gf.update_screen(game_settings, screen, bat, ball)

if __name__ == '__main__':
    run_game()
