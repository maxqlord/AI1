"""
Base class for Othello Core
Must be subclassed by student Othello solutions
"""

#
#characters that refer to each type of piece
EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
#list of all types of pieces
PIECES = (EMPTY, BLACK, WHITE, OUTER)
#dict pointing piece to which color it represents
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
#list of possible directiosn
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

class OthelloCore:
    def squares(self):
        """List all the valid squares on the board."""
        #checks all valid indices and removes edges
        return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]


    def initial_board(self):
        """Create a new board with the initial black and white positions filled."""
        #fill with question marks
        board = [OUTER] * 100
        #fill non-edge positions with periods
        for i in self.squares():
            board[i] = EMPTY
        # The middle four squares should hold the initial piece positions.
        board[44], board[45] = WHITE, BLACK
        board[54], board[55] = BLACK, WHITE
        return board


    def print_board(self,board):
        """Get a string representation of the board."""
        rep = ''
        rep += '  %s\n' % ' '.join(map(str, list(range(1, 9))))
        for row in range(1, 9):
            begin, end = 10 * row + 1, 10 * row + 9
            rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
        return rep


    def is_valid(self, move):
        #is index on the board and not a question mark
        """Is move a square on the board?"""
        pass

    def opponent(self, player):
        """Get player's opponent piece."""
        pass

    def find_bracket(self, square, player, board, direction):
        """
        Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found
        """
        #moves until it hits a blank then returns that index
        pass

    def is_legal(self, move, player, board):
        #1. find_bracket has to not return None- it can take a piece
        #2. your or opponent's piece can't be on the tile
        """Is this a legal move for the player?"""
        pass

    ### Making moves

    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.

    def make_move(self, move, player, board):
        #calls make_flips
        """Update the board to reflect the move by the specified player."""
        pass

    def make_flips(self, move, player, board, direction):
        """Flip pieces in the given direction as a result of the move by player."""
        pass

    def legal_moves(self, player, board):
        #run find_bracket on each of your pieces and return the overall list
        """Get a list of all legal moves for player, as a list of integers"""
        pass

    def any_legal_move(self, player, board):
        #if find_bracket is none return false
        """Can player make any moves? Returns a boolean"""
        pass

    def next_player(self,board, prev_player):
        """Which player should move next?  Returns None if no legal moves exist."""
        pass

    def score(self,player, board):
        """Compute player's score (number of player's pieces minus opponent's)."""
        pass


    class IllegalMoveError(Exception):
        def __init__(self, player, move, board):
            self.player = player
            self.move = move
            self.board = board

        def __str__(self):
            return '%s cannot move to square %d' % (PLAYERS[self.player], self.move)
