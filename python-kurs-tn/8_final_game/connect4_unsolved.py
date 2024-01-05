import numpy as np

class connect4(object):
    # here you should initialize all the variables needed for the implementation 
    def __init__(self, ROWS: int=6, COLUMNS: int=7) -> None:
        pass
        
    # here you should implement the insertion of the chip into the game board
    def insert_piece(self, piece: int, column: int) -> None:
        pass
    
    # check if the column the piece should be inserted is full
    def check_full_col(self, column: int) -> bool:
        pass

    # check if the selected location for the chip is out of the board boundaries
    def is_valid_location(self, column: int) -> bool:
        pass
    
    # return the row where the piece can be placed
    def get_open_row (self, column: int) -> int:
        pass

    # check if the game is won by one of the players
    def check_winning_move(self, player) -> None:
        pass
    
    # Get the player input
    def get_player_input(self) -> int:
        choice = int(input("Bitte gib eine Zahl zwischen 0 und 6 ein: "))
        while not self.is_valid_location(choice): 
            choice=int(input("Die Eingegebne Zahl ist außerhalb des Spielfelds oder die Reihe ist voll. Gib bitte eine Valide Zahl ein: "))
        return choice

    # check if the game board is a draw
    def check_draw(self) -> bool: 
        pass

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
