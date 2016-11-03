#!/usr/bin/python
"""game main module"""
import pygame
import game_functions as gf
from settings import Settings


def run_game():
    """enter point"""
    ball_settings = Settings()
    pygame.init()
    screen = gf.init_screen(ball_settings)

    # main loop
    while True:
        gf.event_check()
        gf.update_screen(ball_settings, screen)

if __name__ == '__main__':
    run_game()
