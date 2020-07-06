# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:01:42 2020

@author: Owen
"""
import pygame


# the side that the pieces belong to
# same as colour of the piece
# container for accessing the pieces
class Side(pygame.sprite.Group):
    def __init__(self, colour):
        pygame.sprite.Group.__init__(self)
        self.colour = colour