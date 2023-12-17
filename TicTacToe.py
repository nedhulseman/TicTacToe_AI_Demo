

import random



class Board:
    def __init__(self):
        self.board = [None] * 9
        self.open_squares = list(range(0, 9))
        self.acceptable_letters = ["X", "x", "O", "o"]
        self.clean_vis_board = \
        '''
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        '''
        self.vis_board = self.clean_vis_board
        self.winning_combos = [
            (0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6),
        ]
        self.winner = False
        self.winning_letter = ""
        self.cats = False
        self.turn = "X"

    def print_layout(self):
        message = "\n\nThe board uses the following coordinated for play:\n"
        print(message+self.clean_vis_board.format(*list(range(0,9))))
    def update(self, letter, loc):
        if self.winner == False and self.cats==False:
            assert letter == self.turn
            assert letter in self.acceptable_letters
            assert loc in self.open_squares

            self.board[loc] = letter.upper()
            self.open_squares.remove(loc)
            self.check_winner()
            self.turn = "X" if self.turn=="O" else "O"
            
            if self.winner==True:
                self.print_winner()
            self.check_cats()
            if self.cats == True:
                self.print_cats()
        else:
            raise ValueError("Game is over.")
    def print(self):
        printable_board = [" " if i==None else str(i) for i in self.board ]
        print(self.clean_vis_board.format(*printable_board))
    def check_winner(self):
        for combo in self.winning_combos:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and (self.board[combo[0]]!= None):
                self.winner = True
                self.winning_letter = self.board[combo[0]]
                return True
        return False
    def check_cats(self):
        if self.check_winner() == False and len(self.open_squares)==0:
            self.cats = True
    def print_winner(self):
        print("!!!!\n\nLetter {} wins!\n\n!!!!".format(self.winning_letter))
        self.print()
    def print_cats(self):
        print("Game has ended in a split.")

class Manager:
    def __init__(self, X, O):
        self.player_modes = ["RandBot", "Human"]
        self.board = Board()
        players_objects = {"Human": Player(engine=X), "RandBot": Player(engine=O)}
        self.players = {"X": players_objects[X], "O":players_objects[O]}
        self.turn = "X"
        self.boards = []
    def play_game(self, verbose=False):
        if verbose==True:
            self.board.print_layout()
        while self.board.winner == False and self.board.cats == False:
            while True:
                try:
                    if verbose==True:
                        print("\n\n########## {} Turn ##########".format(self.turn))
                        print("############################\n\n\n")
                        self.board.print()
                    move = self.players[self.turn].move(self.board)
                    self.board.update(self.turn, move)
                    if verbose==True:
                        print("{} chooses square: {}".format(self.players[self.turn].engine, move))
                    self.boards.append(self.board.board.copy())
                    self.turn = "X" if self.turn=="O" else "O"
                    break
                except:
                    pass
        return self.boards, self.board.winning_letter
            


class Player:
    def __init__(self, engine):
        self.engine = engine
    def move(self, board):
        if self.engine == "Human":
            return self.human(board)
        if self.engine == "RandBot":
            return self.randbot(board)
    def human(self, board):
        print("What is your move?\nAvailable moves: {}".format(board.open_squares))
        move = int(input())
        return move
    def randbot(self, board):
        move = random.sample(board.open_squares, 1)[0]
        return move

