import Othellov2_4_Lord
import othello_core
import time


def runTests():
    myOthello = Othellov2_4_Lord.Othello()
    core = othello_core.OthelloCore()
    player1 = othello_core.WHITE
    player2 = othello_core.BLACK
    scoreList = []
    for x in range(0, 1000):
        board = core.initial_board()
        player = player1

        while (myOthello.any_legal_move(player, board) == True or myOthello.any_legal_move(myOthello.opponent(player), board) == True):
            if (myOthello.any_legal_move(player, board) == False):
                player = myOthello.opponent(player)
            if(player == player1):
                selectedMove = myOthello.choose(player, board, player)
            else:
                selectedMove = myOthello.random_move(player, board)
            myOthello.make_move(selectedMove, player, board)

            #print("Player 1 Score: " + str(myOthello.score(player1, board)))  # works
            player = myOthello.next_player(board, player)
        #print(core.print_board(board))
        finalScore = myOthello.score(player1, board)
        print(str(x + 1) + ": " + str(finalScore))
        scoreList.append(finalScore)
    print(scoreList)
    winCounter = 0
    tieCounter = 0
    lossCounter = 0
    for game in scoreList:
        if game > 0:
            winCounter+=1
        elif game == 0:
            tieCounter+=1
        else:
            lossCounter+=1
    print("Wins: " + str(winCounter))
    print("Ties: " + str(tieCounter))
    print("Losses (how does this even happen): " + str(lossCounter))


initialTime = time.time()
runTests()
finalTime = time.time()
print("Time: " + str(finalTime - initialTime))