import myplayer as mp
letter = None
# === FUNCTIONALITIES OF THE GAME ===



class tic_tac_toe:
    def __init__(self):
        self.board = self.make_board()
# create a board
    def make_board():
        return [' ' for _ in range(9)]

    @staticmethod
    def print_num_board():
        row = [[str(num) for num in range(i*3, (i + 1)*3)] for i in range(3)]
        for j in row:
            print("| " +" | ".join(row) + " |")
    
    @staticmethod
    def print_board(self):
        board = [[j for j in self.board[i*3:(i + 1)*3]] for i in range(3)]
        for space in board:
            print("| " + " | ".join(space) + " |")

# take user input
    def take_human_input(self):
        mp.humanPlayer.input = input("Enter a value from 0-8: ")
        mp.player.input = mp.humanPlayer.input
        reply = mp.player.check_input()
        if reply: self.available_moves(mp.humanPlayer.input)

# compare with the spaces to see if available
    def available_moves(self, input):
        check_available = [True for a in self.board if a == ' ' ]
        if check_available[self.input] == ' ': return True

    
# input it into board and list of used spaces
    def input_value(self, input):
        if self.available_moves(mp.humanPlayer.input): 
            self.board[self.input] = letter

# check for win or tie
    def win_lose_tie():
        
# switch player
# take user input
# compare with the spaces to see if available
# input it into board and list of used spaces
# check for win or tie
