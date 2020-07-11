class Game(pygame.sprite.Sprite):
    def __init__(self, first_player):
        pygame.sprite.Sprite.__init__(self)
        self.turn = first_player # 'red' or 'blue' Side object
        
    def winner(self):
        '''
        Checks if the game has ended and returns the winner
        '''
        # if not ended
            # return False

        # if red wins
            # return 'red'

        # if blue wins
            # return 'blue'
        
    def game_evaluation(self)
        '''
        UTILITY FUNCTION
        Defines the final numeric value for the game when it’s in its terminal state
        '''
        
        # if someone has won the game then return an infinite value
        if self.winner == 'red': # human has won
            return float('inf') 
        elif self.winner == 'blue' # AI has won
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
