#!/usr/bin/python
"""game util function module"""

import sys
import pygame


def event_check():
    """processing game  event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
