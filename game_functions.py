#!/usr/bin/python
"""game util function module"""

import sys
import pygame


def init_screen(game_settings):
    """screen init with settings"""
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Ball")
    return screen


def event_check(bat):
    """processing game  event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_check(event, bat)
        elif event.type == pygame.KEYUP:
            keyup_check(event, bat)


def keyup_check(event, bat):
    if event.key == pygame.K_LEFT:
        bat.left_move = False
    elif event.key == pygame.K_RIGHT:
        bat.right_move = False


def keydown_check(event, bat):
    if event.key == pygame.K_LEFT:
        bat.left_move = True
    elif event.key == pygame.K_RIGHT:
        bat.right_move = True
    elif event.key == pygame.K_q:
        sys.exit()



def update_screen(game_settings, screen, bat, ball):
    """screen redraw"""
    screen.fill(game_settings.bg_color)
    bat.update()
    bat.draw_bat()
    ball.draw_ball()
    pygame.display.flip()
