# Battleships Game 

import random

class Battleships_game:
    def __init__(self, size=10):
        self.size = size
        self.board = [['O' for _ in range(size)] for _ in range(size)] 
        # the above code makes a 2d graph of board, the 'O' is representing empty sea space.
        self.ship_row = random.randint(0, size - 1)
        self.ship_col = random.randint(0, size - 1)
        # the above code makes the computer pick a random spot on board to place ship 

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
            # this joins the elements of current row into single string with a space in between for better visual
        print()
        # this adds space between rows 


    def take_turn(self):
        guess_row = int(input("Guess row: "))
        guess_col = int(input("Guess column: "))
        return guess_row + guess_col 
    




    def play_game():



class Ships 
        
