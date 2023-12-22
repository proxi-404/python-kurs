import numpy as np

class connect4(object):
    def __init__(self, ROWS: int=6, COLUMNS: int=7) -> None:
        self.ROWS = ROWS
        self.COLUMS = COLUMNS
        self.game_board = np.zeros((ROWS, COLUMNS))
        self.game_over = False
        self.draw = False
        
    def insert_piece(self, piece: int, column: int) -> None:
        location = self.get_open_row(column)
        self.game_board[location][column] = piece

    
    def check_full_col(self, column: int) -> bool:
        if self.game_board[self.ROWS - 1][column] != 0:
            return True
        else: 
            return False

    def is_valid_location(self, column: int) -> bool:
        if column > self.COLUMS-1 or column < 0:
            return False
        else:
            if not self.check_full_col(column):
                return True
            else: 
                return False
            
    def get_open_row (self, column: int) -> int:
        for i in range(self.ROWS):
            if self.game_board[i][column] == 0:
                return i

    def check_winning_move(self, player) -> None:
        # check for horizontal win 
        for y in range(self.ROWS):
            for x in range(self.COLUMS - 3):
                if self.game_board[y][x] == player and self.game_board[y][x+1] == player and self.game_board[y][x+2] == player and self.game_board[y][x+3] == player:
                    print("horizontal")
                    self.game_over = True

        # check for vertical win
        for y in range(self.ROWS -3):
            for x in range(self.COLUMS):
                if self.game_board[y][x] == player and self.game_board[y+1][x] == player and self.game_board[y+ 2][x] == player and self.game_board[y+3][x] == player:
                    self.game_over = True

        # check for diagonal win left top, bottom right
        for y in range(self.ROWS -3):
            for x in range(self.COLUMS-3):
                if self.game_board[y][x] == player and self.game_board[y+1][x+1] == player and self.game_board[y+2][x+2] == player and self.game_board[y+3][x+3] == player:
                    self.game_over = True

        # check for diagonal win left bottom, top right
        for y in range(self.ROWS-3):
            for x in range(3, self.COLUMS):
                if self.game_board[y][x] == player and self.game_board[y+1][x-1] == player and self.game_board[y+2][x-2] == player and self.game_board[y+3][x-3] == player:
                    self.game_over = True

    def get_player_input(self) -> int:
        choice = int(input("Bitte gib eine Zahl zwischen 0 und 6 ein: "))
        while not self.is_valid_location(choice): 
            choice=int(input("Die Eingegebne Zahl ist außerhalb des Spielfelds oder die Reihe ist voll. Gib bitte eine Valide Zahl ein: "))
        return choice

    def check_draw(self) -> bool: 
        if np.any(self.game_board[:, :] == 0):
            self.draw = False
        else: 
            self.draw = True
        

    def print_board(self) -> None:
        self.flipped_board = np.flip(self.game_board, 0)
        print("\n     0    1    2    3    4    5    6  ", end="")
        for x in range(self.ROWS):
            print("\n   +----+----+----+----+----+----+----+")
            print(x, " |", end="")
            for y in range(self.COLUMS):
                if(self.flipped_board[x][y] == 1):
                    print("", "🔴", end=" |")
                elif(self.flipped_board[x][y] == 2):
                    print("", "🔵", end=" |")
                else:
                    print(" ", '', end="  |")
        print("\n   +----+----+----+----+----+----+----+")

active_game = True

while active_game:

    game = connect4()
    turn = 0

    while not game.game_over and not game.draw:
        game.print_board()

        if turn % 2 == 0:
            currentPlayer = 'Player 1'
            chip = 1
        else:
            currentPlayer = 'Player 2'
            chip = 2
        print(f"{currentPlayer}: \n")
        position = game.get_player_input()
        game.insert_piece(chip, position)
        game.check_winning_move(chip)
        game.check_draw()
        turn += 1

    if game.draw:
        game.print_board()
        print("Unentschieden!")


    if game.game_over and not game.check_draw():
        game.print_board()

        print(f"{currentPlayer} hat gewonnen!")


    replay = input("Möchtet ihr erneut spielen? (J/N)")

    if replay.lower() == 'n':
        active_game = False
        print("Spiel zuende!")
    elif replay.lower() == 'j':
        print('Starte neues Spiel!')
    

