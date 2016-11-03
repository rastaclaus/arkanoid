#!/usr/bin/python
"""game util function module"""

import sys
import pygame


def init_screen(ball_settings):
    """screen init with settings"""
    screen = pygame.display.set_mode(
        (ball_settings.screen_width, ball_settings.screen_height))
    pygame.display.set_caption("Ball")
    return screen


def event_check():
    """processing game  event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ball_settings, screen):
    """screen redraw"""
    screen.fill(ball_settings.bg_color)
    pygame.display.flip()
