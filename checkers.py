# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:54:34 2020

@author: Owen
"""
import doctest
import pygame

class Game(pygame.sprite.Sprite):
    def __init__(self):
        # some stuff
    
    def move(direction):
        """
        (str)->bool
        
        Takes as input a string indicating the direction of the desired move and
        returns true if the move was performed successfully, and false otherwise.
        
        """
        return True
        
    def winner():
        """ 
        ()->bool
        
        Returns true if there is a winner of the game, false otherwise.
        """
        return True

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        # some stuff 


# encounters error opening pygame window
def main():
    pygame.init()
    
    size = 50
    surface_sz = 400   # Desired physical surface size, in pixels

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    black, white, red = (0, 0, 0), (255, 255, 255), (255, 0, 0) 

    while True:
        
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill(white)

        # do we need a red border? 
        #pygame.draw.rect(main_surface, red, [0, 0, surface_sz, surface_sz], 1)

        # Overpaint a smaller rectangle on the main surface
        for j in range(0, 9): # x position
            for i in range(0, 9): # y position
                small_rect = (size*j, size*i, size, size)
                if i % 2 == j % 2:
                    # create a black square at every grid spot with even x and y
                    main_surface.fill(black, small_rect) 

        # display surface
        pygame.display.flip()

    pygame.quit()
    
    
    
if __name__ == "__main__":
    #doctest.testmod()
    main()
