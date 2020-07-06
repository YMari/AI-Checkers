# -*- coding: utf-8 -*-
# check branching
"""
Created on Mon Jun 29 22:54:34 2020

@author: Owen
"""
import doctest
import pygame

# Some important variables for the entire program 
black, white, red, blue = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255)
size = 50
surface_sz = 400 # Surface size in pixels

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
    def move(xpiece, ypiece, xmove, ymove): # how do we want to choose a piece to be moved?
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

# maybe we could add a field that just is an id number (1-12) so that the player can more easily choose the piece to move
# the number could then be displayed on the piece
# also do we want to make a pygame.sprite.Group for each side so that we can access the pieces?
class Piece(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, player, id_num):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.x = x_position
        self.y = y_position
        self.player = player # for now this is a colour... but eventually we could use this for human vs computer ??
        self.radius = 20
        self.id = id_num
        pygame.draw.circle(screen, self.player, (self.x, self.y), self.radius)


def main():
    pygame.init()
    
    # Create surface of (width, height) and its window
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    pygame.display.set_caption('Checkers')


    while True:
        
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # Fill background
        main_surface.fill(white)

        # Initialize game groups
        pieces = pygame.sprite.RenderUpdates()

        # do we need a red border? 
        #pygame.draw.rect(main_surface, red, [0, 0, surface_sz, surface_sz], 1)

        # overpaint a smaller rectangle on the main surface
        for i in range(8): # x position
            for j in range(8): # y position
                small_rect = (size*i, size*j, size, size)
                if i % 2 != j % 2: # the inequality ensures that the bottom right corner is white for both players (part of the rules)
                    # create a black square at alternating gridpoints 
                    main_surface.fill(black, small_rect) 

        # add the pieces to the board
        for i in range(8): # x position
            for j in range(8): # y position            
                if i % 2 != j % 2:
                    if j < 3:
                        pieces.add(Piece(*getPixels(i,j),blue))
                    elif j > 4:
                        pieces.add(Piece(*getPixels(i,j),red))
        
        # display surface
        pygame.display.flip()

    pygame.quit()
    
def getPixels(x_pos, y_pos):
    """
    (int,int) -> (int,int)

    Takes an x and y position with respect to the board spaces - both values are between 0 and 7, with top left corner as (0,0) - 
    and returns the pixel position with respect to the screen size 
        
    """
    
    # dictionary with key as square on board and value as pixel position on screen (centre of the board square) 
    pos_to_pixel = {0:25, 1:75, 2:125, 3:175, 4:225, 5:275, 6:325, 7:375} 
    x_pixel = pos_to_pixel[x_pos]
    y_pixel = pos_to_pixel[y_pos]

    # write something to catch error if board position is not in dictionary (out of bounds, not an integer, etc) 

    return (x_pixel, y_pixel)
    
    
if __name__ == "__main__":
    #doctest.testmod()
    main()
