import random

class Battleships_game:
    def __init__(self, size=5):
        # Initialize the Battleship game with a default board size of 5x5
        self.size = size
        # Create an empty game board filled with 'O'
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        # Place the battleship at a random position on the board
        self.ship_row = random.randint(0, size - 1)
        self.ship_col = random.randint(0, size - 1)
        # Initialize the number of attempts made by the player
        self.attempts = 0

    def print_board(self):
        # Print the current state of the game board
        for row in self.board:
            print(" ".join(row))
        print()

    def take_turn(self):
        # Get the player's guess for the row
        guess_row = input("Guess row (or type 'exit' to end the game): ")

        if guess_row.lower() == 'exit':
            # If the player wants to exit, return 'exit' for both row and column
            return 'exit', 'exit'

        try:
            # Convert the input to an integer for the row
            guess_row = int(guess_row)
            # Get the player's guess for the column
            guess_col = int(input("Guess column: "))
            # Return the player's guess as a tuple
            return guess_row, guess_col
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input. Please enter a valid integer for the row.")
            # Recursively call take_turn to get a valid input
            return self.take_turn()

    def play_game(self):
        # Start the Battleship game
        print("Welcome to Battleship!")

        while True:
            # Display the current state of the game board
            self.print_board()
            # Get the player's turn
            guess_row, guess_col = self.take_turn()

            if guess_row == 'exit' or guess_col == 'exit':
                # If the player wants to exit, end the game
                print("Game ended. Thanks for playing!")
                break

            # Increment the number of attempts made by the player
            self.attempts += 1

            if 0 <= guess_row < self.size and 0 <= guess_col < self.size:
                if self.board[guess_row][guess_col] == "X":
                    # If the player has already guessed the same spot, notify and ask for another guess
                    print("Oops, you've already guessed that. Try again.")
                else:
                    # Mark the guessed spot with 'X' on the board
                    self.board[guess_row][guess_col] = "X"
                    print(f"LOL, you missed. That makes {self.attempts} attempts. Try again loser.")
            else:
                # If the guessed spot is outside the board, ask for another guess
                print("Bro... that's not even in the ocean. Try again")

if __name__ == "__main__":
    # Run the Battleship game
    game = Battleships_game()
    game.play_game()
