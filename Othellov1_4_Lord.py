import othello_core
import random
core = othello_core.OthelloCore()
class Othello():
    
    def is_valid(self, move):
        """Is move a square on the board?"""
        if(11 <= move < 89 and 1 <= (move % 10) <= 8):
            return True

    def opponent(self, player):
        """Get player's opponent piece."""
        if(player is othello_core.WHITE):
            return othello_core.BLACK
        return othello_core.WHITE



    def find_bracket(self, square, player, board, direction):

        bracket = square + direction
        if board[bracket] == player:
            return None
        opp = self.opponent(player)
        while board[bracket] == opp:
            bracket += direction
        return None if board[bracket] in (othello_core.OUTER, othello_core.EMPTY) else bracket

    def is_legal(self, move, player, board):
        """Is this a legal move for the player?"""
        for direction in othello_core.DIRECTIONS:
            if(self.find_bracket(move,player, board, direction) != None and board[move] == othello_core.EMPTY):
                return True
        return False
    ### Making moves

    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.

    def make_move(self, move, player, board):
        """Update the board to reflect the move by the specified player."""
        print(move)
        board[move] = player
        for direction in othello_core.DIRECTIONS:
            self.make_flips(move, player, board, direction)
        return board

    def make_flips(self, move, player, board, direction):
        bracket = self.find_bracket(move, player, board, direction)
        if not bracket:
            return
        square = move + direction
        while square != bracket:
            board[square] = player
            square += direction

    def legal_moves(self, player, board):
        """Get a list of all legal moves for player, as a list of integers"""
        legalArray = []
        for square in core.squares():
            if(self.is_legal(square, player, board)):
                legalArray.append(square)
                #print("Legal Square: " + str(square))
            #print("Illegal Square: " + str(square))
        return legalArray
    def any_legal_move(self, player, board):
        """Can player make any moves? Returns a boolean"""
        if(len(self.legal_moves(player,board)) == 0):
            return False
        return True

    def next_player(self,board, prev_player):
        """Which player should move next?  Returns None if no legal moves exist."""
        if self.any_legal_move(self.opponent(prev_player), board):
            return self.opponent(prev_player)
        elif self.any_legal_move(prev_player, board):
            return prev_player
        return None

    def score(self,player, board):
        """Compute player's score (number of player's pieces minus opponent's)."""
        playerCount = 0
        opponentCount = 0
        for square in core.squares():
            selectedSquare = board[square]
            if(selectedSquare == player):
                playerCount += 1
            elif(selectedSquare == self.opponent(player)):
                opponentCount += 1
        return playerCount - opponentCount
    def random_move(self, player, board):
        movesList = self.legal_moves(player, board)
        return random.choice(movesList)
        
