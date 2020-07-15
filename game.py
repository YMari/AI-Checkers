import pygame
from copy import deepcopy

class Game(pygame.sprite.Sprite):
    def __init__(self, first_player, max_depth):
        '''
        Max depth indicates the maximum depth of the game tree
        Player indicates the colour of the player on the current turn
        '''
        pygame.sprite.Sprite.__init__(self)
        self.turn = first_player # 'red' or 'blue' Side object
        self.max_depth = max_depth
        
        
    def winner(self, board):
        '''
        Checks if the game has ended and returns the winner
        '''
        # if not ended
            # return False

        # if red wins
            # return 'red'

        # if blue wins
            # return 'blue'
        
    def game_evaluation(self, some_board):
        '''
        UTILITY FUNCTION
        Defines the final numeric value for the game when it’s in its terminal state
        '''
        
        # if someone has won the game then return an infinite value
        if self.winner == 'red': # human has won
            return float('inf') 
        elif self.winner == 'blue': # AI has won
            return float('-inf')


        '''
        EVALUATION FUNCTION
        Defines an estimate of the expected utility numeric value from a given state
        Outputs a numeric value that represents the outcome and desirabiity of the board state
        Called when the game has not ended
        The human player is always striving for a more positive (maximum) value
        The AI is always striving for a more negative (minimum) value 
        A negative score indicates that the human player is in a disadvantaged position 
        '''
        
        # the numeric value of the board is determined by the number of the player's kings (+ 30) 
        # and the difference in number of pieces between the player and their opponent (+ 10 for each additional piece) 

        score = 0
        constant = 0
        
        if self.turn == 'red':
            constant = 1
            score += 30 * len(red_kings.sprites())
            difference = len(red_pieces.sprites()) - len(blue_pieces.sprites())
            score += 10 * difference
        elif self.turn == 'blue':
            constant = -1
            score += 30 * len(blue_kings.sprites())
            difference = len(blue_pieces.sprites()) - len(red_pieces.sprites())
            score += 10 * difference

        score = score*constant # the constant mediates the fact that the human wants a more positive score while AI wants more negative 
        return score

    def get_move(self, board):
        '''
        Takes the board matrix as input and returns the best move
        '''
        best_board = None
        cur_depth = self.max_depth + 1

        while not best_board and cur_depth > 0:
            cur_depth -= 1
            (best_board, value) = max_move(board, cur_depth)

        return (best_board, value) 

    def max_move(self, board, cur_depth):
        '''
        Used to recursively traverse the tree
        '''
        return find_move(max_board, cur_depth-1, 'red')

    def min_move(self, board, cur_depth):
        '''
        Used to recursively traverse the tree
        '''
        return find_move(min_board, cur_depth-1, 'blue')

    def find_move(self, board, cur_depth, player):
        '''
        Finds the best move
        Returns the best board and its score 
        '''
        # checks if we are at a leaf
        if (winner() != False) or (cur_depth < 1):
            return (board, game_evaluation(board))

        # this executes if we are not at a leaf
        best_board = None
        
        if player == 'red': # human wants a board with inf score
            best_score = float('-inf')
            moves = red_moves(board) # get board matrices of all possible red moves
            for move in moves:
                max_board = move
                value = min_move(max_board, cur_depth-1)[1]
                if value > best_score:
                    best_score = value
                    best_board = max_board
            
        
        elif player == 'blue': # AI wants a board with -inf score
            best_score = float('inf')
            moves = blue_moves(board) # get board matrices of all possible blue moves
            for move in moves:
                min_board = board
                value = max_move(min_board, cur_depth-1)[1]
                if value < best_score:
                    best_score = value
                    best_board = min_board

        return (best_board, best_score)
            

    def blue_moves(self, board):
        '''
        Receives an input of the current board and returns an array of many board
        matrices representing all possible moves for the blue player
        '''
        possible_moves = []

        return possible_moves


    def red_moves(self, board):
        '''
        Receives an input of the current board and returns an array of many board
        matrices representing all possible moves for the red player
        '''
        possible_moves = []

        return possible_moves  


        
    
