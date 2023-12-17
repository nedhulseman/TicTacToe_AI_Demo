'''
#---------- Testing board
#-- winner
from TicTacToe import Board
b = Board()
b.update("X",0)
b.update("y",5)
b.update("X",1)
b.update("y",8)
b.update("X",2)

#-- cats game
from TicTacToe import Board
b = Board()
b.update("X",0)
b.update("y",5)
b.update("X",4)
b.update("y",1)
b.update("X",7)
b.update("y",8)
b.update("x",2)
b.update("y",6)
b.update("x",3)
'''
if __name__=="__main__":
    from TicTacToe import Manager
    manager = Manager(X="RandBot", O="RandBot")
    manager.play_game()