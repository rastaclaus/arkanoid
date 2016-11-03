#!/usr/bin/python
"""game main module"""
import pygame
import game_functions as gf
from settings import Settings


def run_game():
    """enter point"""
    ball_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (ball_settings.screen_width, ball_settings.screen_height))

    pygame.display.set_caption("Ball")

    # main loop
    while True:
        gf.event_check()
        screen.fill(ball_settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
