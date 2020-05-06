#System Designs - Connect Four
#Only write down function names, what they take in and what they return

red
black
board
rows 
columns
score: repeat games
position
board full?



Class Token:

    def __init__(self, color, coordinates):
        self.color = color
        self.coordinates = coordinates 

   

Class Board:

    def __init__(self):
        self.rows = 5
        self.columns = 5
        self.num_of_moves_played = 0


    def find_position(column_number, self.rows?):
        """Determines what rows have already been filled in chosen column to return coordinates """
        return coordinates


    def choose_column():
        """Asks the user for column choice and checks if column is full"""
        return column_number


    def is_column_available(column_number):
        """Checks if column is full to populate input prompt for user to choose token placement"""
        return boolean


    def set_next_turn(self.num_of_moves_played):
        """Alternates players, player1 moves if board.num_of_moves_played is odd and player2 moves if board.num_of_moves_played is even"""

        return player_number or "board is full, tie"


    def find_four_connected(board,new_token_placed):
    """Takes in the board and checks for connect-four """
    return player if true, else false


def play_again():
    """Ask if user would like to play again"""

    return boolean
