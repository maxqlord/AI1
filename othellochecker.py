import Othellov1_4_Lord
import othello_core


def runTests():
    myOthello = Othellov1_4_Lord.Othello()
    core = othello_core.OthelloCore()
    player1 = othello_core.WHITE
    player2 = othello_core.BLACK
    board = core.initial_board()
    player = player1
    while(myOthello.any_legal_move(player, board)):

        selectedMove = myOthello.random_move(player, board)
        myOthello.make_move(selectedMove,player, board)
        print(core.print_board(board))
        print("Score: " + str(myOthello.score(player, board)))#works
        player = myOthello.next_player(board, player)


    
    
runTests()
