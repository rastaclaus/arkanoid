#!/usr/bin/python
"""game main module"""
import sys
import pygame


def run_game():
    """enter point"""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Ball")

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((130, 130, 130))
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
