#!/usr/bin/python
"""game main module"""
import sys
import pygame
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ball_settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
