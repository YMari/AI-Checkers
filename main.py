# -*- coding: utf-8 -*-

import doctest
import pygame
import time
import numpy
import math
import os

from game import *

# Some important variables 
black, white, red, blue = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255)
size = 50
surface_sz = 400 # Surface size in pixels

# the board holds a matrix representation of the positions of our game pieces 
board = numpy.zeros((8,8))

class Piece(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.player = player # a colour
        self.radius = 20

        
        ##### Note that our pieces do not have a "rect", meaning they don't have positions on the board
        ##### I couldn't figure out how to make the pieces move if they had a rect, so I figured it was just easier to redraw new circles on every turn using draw_board()
        
        #self.rect = 
        #self.rect.centerx = x_position
        #self.rect.centery = y_position

        
    ''' REMOVE METHOD ?? NOT NEEDED NOW THAT WE HAVE DRAW_BOARD()
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
    '''
    
    def get_colour(num):
        if num == 1:
            return blue
        elif num == 2:
            return red
        else:
            return None
    
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
        
#<<<<<<< HEAD
    def capture(x_coord, y_coord, colour):
#>>>>>>> owens_checkers
        """
        Removes a piece from the matrix.
        """
        board[y_coord][x_coord] = 0
#<<<<<<< HEAD
        draw_board()
        pygame.display.update()
#=======
        pieces.remove(*getPixels(x_coord, y_coord), colour) # remove piece from group
        draw_board() # build new board with changes
        pygame.display.update() # display new board
#>>>>>>> owens_checkers
        
        
def draw_board(board):
    '''
    Updates the position of the pieces on the board after every move, by copying the board array 
    '''
    draw_background() # we must make the board blank before drawing the pieces again, or else the old positions will remain drawn 
    screen = pygame.display.get_surface()
    radius = 20
    i = 0
    for row in board:
        j = 0
        for space in row:
            if space == 1:
                pygame.draw.circle(screen, red, getPixels(j,i), radius)
            elif space == 2:
                pygame.draw.circle(screen, blue, getPixels(j,i), radius)
            j+=1
        i+=1
    
def draw_background():
    '''
    This method is used to reset the board by making it blank without any pieces
    It is only used by draw_board after each move
    Note that it is not used when the board is initially set up in main() because we do not want to create new Space objects every time 

    '''
    screen = pygame.display.get_surface()
    # overpaint a smaller rectangle on the main surface
    for i in range(8): # x position
        for j in range(8): # y position
            small_rect = (size*i, size*j, size, size)
            if i % 2 != j % 2: # the inequality ensures that the bottom right corner is white for both players (part of the rules)
                # create a black square at alternating gridpoints
                pygame.draw.rect(screen, black, small_rect)
            else:
                pygame.draw.rect(screen, white, small_rect)

class Space(pygame.sprite.Sprite):
    def __init__(self, shape, color, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.rect = pygame.draw.rect(screen, color, shape)
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        

# Initialize game groups
pieces = pygame.sprite.RenderUpdates()
blue_pieces = pygame.sprite.RenderUpdates()
blue_kings = pygame.sprite.RenderUpdates()
red_pieces = pygame.sprite.RenderUpdates()
red_kings = pygame.sprite.RenderUpdates()
spaces = pygame.sprite.RenderUpdates()

def main():
    pygame.init()

    # Main game object with first player as red (human)
    game = Game('red', 5) 
    
    # Create surface of (width, height) and its window
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    pygame.display.set_caption('Checkers')

    # Fill background
    main_surface.fill(white)

    # Create the board
    for i in range(8): # x position
        for j in range(8): # y position
            small_rect = (size*i, size*j, size, size)
            if i % 2 != j % 2: # the inequality ensures that the bottom right corner is white for both players (part of the rules)
                # create a black square at alternating gridpoints 
                spaces.add(Space(small_rect, black, i, j))
            else:
                spaces.add(Space(small_rect, white, i, j))
                

    # add the pieces to the board
    for i in range(8): # x position
        for j in range(8): # y position            
            if i % 2 != j % 2:
                if j < 3:
                    blue_piece = Piece(*getPixels(i,j),blue)
                    pieces.add(blue_piece)
                    blue_pieces.add(blue_piece)
                    board[j][i] = 2 # updating the matrix with "2" for blue pieces
                elif j > 4:
                    red_piece = Piece(*getPixels(i,j),red)
                    pieces.add(red_piece)
                    red_pieces.add(red_piece)
                    board[j][i] = 1 # updating the matrix with "1" for red pieces


    draw_board(board) # adding the pieces to the board now that they have been added to the board matrix 
    
    # display surface
    pygame.display.flip()

    piece_selected = pygame.sprite.GroupSingle()
    space_selected = pygame.sprite.GroupSingle()
    temp_selected = pygame.sprite.GroupSingle()
    second_click = False # this variable is used to differentiate the two click events (MOUSEBUTTONDOWN) 
    awaiting_red = True
    
    while True:
       
        # human's turn
        if game.turn == 'red':
            awaiting_red = True
            while awaiting_red:
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: # if window close button clicked then leave game loop
                        break
                        
                    if event.type == pygame.MOUSEBUTTONDOWN and second_click == False: # click piece to move 
                        pos = pygame.mouse.get_pos()
                        temp_selected.add(space for space in spaces if space.rect.collidepoint(pos)) 
                        my_space = temp_selected.sprite
                        if board[my_space.y_pos][my_space.x_pos] != 0: # we are selecting a non-empty space
                            piece_selected.add(my_space)
                            second_click = True
                              
                    elif event.type == pygame.MOUSEBUTTONDOWN and second_click == True: # click new position for piece 
                        pos = pygame.mouse.get_pos()
                        space_selected.add(space for space in spaces if space.rect.collidepoint(pos)) # position for piece to move
                        
                        # if player choses to move by one diagonal, allow move
                        if dist(piece_selected.sprite.x_pos, space_selected.sprite.x_pos, piece_selected.sprite.y_pos, \
                                space_selected.sprite.y_pos) == math.sqrt(2):
                            # updating the board array 
                            my_color = board[piece_selected.sprite.y_pos][piece_selected.sprite.x_pos]
                            board[piece_selected.sprite.y_pos][piece_selected.sprite.x_pos] = 0
                            board[space_selected.sprite.y_pos][space_selected.sprite.x_pos] = my_color

                        # add else block and check for piece in jump if player chose to move more than one diagonal
                        # otherwise do nothing or prompt user to choose a valid move
                        elif dist(piece_selected.sprite.x_pos, space_selected.sprite.x_pos, piece_selected.sprite.y_pos, \
                                space_selected.sprite.y_pos) == 2 * math.sqrt(2):
                            x_jumped = (space_selected.sprite.x_pos - piece_selected.sprite.x_pos)/2 + piece_selected.sprite.x_pos
                            y_jumped = (space_selected.sprite.y_pos - piece_selected.sprite.y_pos)/2 + piece_selected.sprite.y_pos

                            # jumped a piece
                            if board[y_jumped][x_jumped] != 0 and\
                                board[y_jumped][x_jumped] != board[piece_selected.sprite.y_pos][piece_selected.sprite.x_pos]:

                                Piece.capture(x_jumped, y_jumped, Piece.get_colour(board[y_jumped][x_jumped]))

                        second_click = False
                        awaiting_red = False
                        
        # computer's turn
        elif game.turn == 'blue':
            move = game.get_move(board)

            # updating the board matrix 
            for i in range(8): # x position
                for j in range(8): # y position
                    new_space = move[0][j][i]
                    board[j][i] = new_space

        # for some reason the screen doesn't update until after both players have made moves?? can't figure out how to fix this 
        draw_board(board)
        pygame.display.update()
        game.change_turn()
        
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

def dist(x1, x2, y1, y2):
    """ Distance helper method"""
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
    
    
if __name__ == "__main__":
    #doctest.testmod()
    main()
