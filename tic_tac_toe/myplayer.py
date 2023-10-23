import mygame as mg
letter = None
human_input = None
computer_input = None
move_made = False
# create a player class which takes the letters 'X' and 'O'
class player:
    def __init__(self, letter, input):
        self.letter = letter
        self.input = input
    
    def check_input(self):
        while not move_made:
            try:
                self.input = int(self.input)
                if not  mg.available_moves(self.input):
                    raise ValueError
            except:
                print("Invalid input, try again")
                continue
            else:
                move_made = True
        return True

"""
# Human player class
class humanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

# Computer Player class
class cumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
"""
humanPlayer = player(letter, human_input)
computerPlayer = player(letter, computer_input)
# == PLAYER FUNCTIONALITIES ==
# player input is checked for player
# player move is checked to see if it's a win
