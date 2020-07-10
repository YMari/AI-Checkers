# -*- coding: utf-8 -*-

import doctest
import pygame
import numpy
#<<<<<<< HEAD
#=======
import os
#>>>>>>> v1.1

# Some important variables for the entire program 
black, white, red, blue = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255)
size = 50
surface_sz = 400 # Surface size in pixels

# the board holds a matrix representation of the positions of our game pieces 
board = numpy.zeros((8,8))

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        
    def winner():
        """ 
        ()->bool
        
        Returns true if there is a winner of the game, false otherwise.
        """
        return True

class Piece(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, player):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.player = player # for now this is a colour... but eventually we could use this for human vs computer ??
        self.radius = 20
        self.rect = screen.get_rect()
        self.rect.centerx = x_position
        self.rect.centery = y_position
        pygame.draw.circle(screen, self.player, (self.rect.centerx, self.rect.centery), self.radius)

    def move(self, x_start, y_start, x_end, y_end):
        """
        (int,int,int,int)->bool
        
        Takes as input the starting coordinates and ending coordinates of the desired move and
        returns true if the move was performed successfully, and false otherwise.
        
        """
        ## the method is updating the position of the rect but not actually moving the piece
        # using draw.circle does work but doesn't actually move the sprite object itself
        # not sure what to do 

        self.rect.centerx = x_end
        self.rect.centery = y_end

        #screen = pygame.display.get_surface()
        #pygame.draw.circle(screen, self.player, (self.rect.centerx, self.rect.centery), self.radius)
        #return True
#<<<<<<< HEAD
#=======
        
    # potential issue with the coordinates of where the crown will be added   
    def load_image(self, name):
        """ 
        (str) -> image (not sure what kind of object or data type an image would be)
        Loads an image and returns image object"""
        fullname = os.path.join('images', name) # filepath of the image
        try:
            image = pygame.image.load(fullname) # image object loaded from path
            
            # make the image go over the colour of the piece
            if self.player == red:
                image.set_colorkey(red) 
            else:
                image.set_colorkey(blue)
                
            if image.get_alpha() == None: # 
                image = image.convert()
            else:
                image =image.convert_alpha()
        except pygame.error:
            print('Cannot load image: ', fullname)
            raise SystemExit
        return image
        
    def king(self):
        """Kings a piece """
        self.type = "king"
        # here we would add a visual component of a king using load_image
        self.load_image('crown.jpg')
        
#>>>>>>> v1.1

class Space(pygame.sprite.Sprite):
    def __init__(self, shape):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.rect = screen.get_rect()
        screen.fill(black, shape)
        

def main():
    pygame.init()
    
    # Create surface of (width, height) and its window
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    pygame.display.set_caption('Checkers')

    # Fill background
    main_surface.fill(white)

    # Initialize game groups
    pieces = pygame.sprite.RenderUpdates()
    spaces = pygame.sprite.RenderUpdates()

    # overpaint a smaller rectangle on the main surface
    for i in range(8): # x position
        for j in range(8): # y position
            small_rect = (size*i, size*j, size, size)
            if i % 2 != j % 2: # the inequality ensures that the bottom right corner is white for both players (part of the rules)
                # create a black square at alternating gridpoints 
                spaces.add(Space(small_rect))

    # add the pieces to the board
    for i in range(8): # x position
        for j in range(8): # y position            
            if i % 2 != j % 2:
                if j < 3:
                    pieces.add(Piece(*getPixels(i,j),blue))
                    board[j][i] = 1 # updating the matrix with "1" for player 1's pieces
                elif j > 4:
                    pieces.add(Piece(*getPixels(i,j),red))
                    board[j][i] = 2 # updating the matrix with "2" for player 2's pieces
    
    # display surface
    pygame.display.flip()

    piece_selected = pygame.sprite.GroupSingle()
    space_selected = pygame.sprite.GroupSingle()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if window close button clicked then leave game loop
                break
            if event.type == pygame.MOUSEBUTTONDOWN: # select piece to move 
                pos = pygame.mouse.get_pos()
                piece_selected.add(piece for piece in pieces if piece.rect.collidepoint(pos))

            if event.type == pygame.MOUSEBUTTONUP: # position for piece to move
                pos = pos_x, pos_y = pygame.mouse.get_pos()
                space_selected.add(space for space in spaces if space.rect.collidepoint(pos))
                orig_x, orig_y = piece_selected.sprite.rect.centerx, piece_selected.sprite.rect.centery

                # move is not actually moving anything !!
                piece_selected.sprite.move(orig_x, orig_y, pos_x, pos_y)
                pygame.display.update()
    pygame.quit()
    
def getPixels(x_pos, y_pos):
    """
    (int,int) -> (int,int)

    Takes an x and y position with respect to the board spaces - both values are between 0 and 7, with top left corner as (0,0) - 
    and returns the pixel position with respect to the screen size 
        
    """
    
    # dictionary with key as square on board and value as pixel position on screen (centre of the board square) 
    pos_to_pixel = {0:25, 1:75, 2:125, 3:175, 4:225, 5:275, 6:325, 7:375} # should change to soft code 
    x_pixel = pos_to_pixel[x_pos]
    y_pixel = pos_to_pixel[y_pos]

    # write something to catch error if board position is not in dictionary (out of bounds, not an integer, etc) 

    return (x_pixel, y_pixel)
    
    
if __name__ == "__main__":
    #doctest.testmod()
    main()
