# output board showing the available spaces that can be played
import random
import time
board = [" " for i in range(9)]
inputed_values = [a for a in range(0, 9)]
available_list = list((0, 1, 2, 3, 4, 5, 6, 7, 8))
winner = None


def win_lose_draw_human():
    # check row
    global winner
    rows = human_player // 3
    check_row = [value for value in board[rows*3: (rows + 1) * 3]]
    row_list = [j for j in check_row if j == letter]
    if len(row_list) == 3:
        print(f"The winner is {letter}")
        winner = letter
        
    # check column
    column = human_player % 3
    check_column = [board[column+i*3] for i in range(3)]
    col_list = [j for j in check_column if j == letter]
    if len(col_list) == 3:
        print(f"The winner is {letter}")
        winner = letter

    # check diagonal --> [0, 2, 4, 6, 8]
    diagonal = human_player % 2
    if diagonal == 0:
        check_diagonal1 = [board[i] for i in range(0, 9, 4)]
        diagonal1_list = [j for j in check_diagonal1 if j == letter]
        if len(diagonal1_list) == 3:
            print(f"The winner is {letter}")
            winner = letter
        check_diagonal2 = [board[i*2] for i in range(1, 4)]
        diagonal2_list = [j for j in check_diagonal2 if j == letter]
        if len(diagonal2_list) == 3:
            print(f"The winner is {letter}")
            winner = letter

    
    # check for a tie
    check_tie = [a for a in board if a == " "]
    if winner is None and len(check_tie) == 0:
        print("it's a tie!")
        quit()

def win_lose_draw_computer():
    # check row
    global winner
    rows = computer_player // 3
    check_row = [value for value in board[rows*3: (rows + 1) * 3]]
    row_list = [j for j in check_row if j == letter]
    if len(row_list) == 3:
        print(f"The winner is {letter}")
        winner = letter
        
    # check column
    column = computer_player % 3
    check_column = [board[column+i*3] for i in range(3)]
    col_list = [j for j in check_column if j == letter]
    if len(col_list) == 3:
        print(f"The winner is {letter}")
        winner = letter

    # check diagonal --> [0, 2, 4, 6, 8]
    diagonal = computer_player % 2
    if diagonal == 0:
        check_diagonal1 = [board[i] for i in range(0, 9, 4)]
        diagonal1_list = [j for j in check_diagonal1 if j == letter]
        if len(diagonal1_list) == 3:
            print(f"The winner is {letter}")
            winner = letter
        check_diagonal2 = [board[i*2] for i in range(1, 4)]
        diagonal2_list = [j for j in check_diagonal2 if j == letter]
        if len(diagonal2_list) == 3:
            print(f"The winner is {letter}")
            winner = letter

    
    # check for a tie
    check_tie = [a for a in board if a == " "]
    if winner is None and len(check_tie) == 0:
        print("it's a tie!")
        quit()



# game_board()
def game_board():
    # print(board)
    num_board = [[str(num) for num in available_list[j*3:(j + 1)*3]] for j in range(3)]

    # print(num_board)
    for row in num_board:
        print("| " + " | ".join(row) + " |")

# take the player input
game_board()
while winner is None:
    letter = "X"
    global human_player
    global computer_player
    human_player = input("Enter a value from 0 - 8: ")
    try:
        human_player = int(human_player)
        if human_player in available_list:
            board[human_player] = letter
            available_list[human_player] = letter
        else:
            raise ValueError
    except ValueError:
        print("Invalid input")
        continue
    
    inputed_values.remove(human_player)
    print(f"You moved to {human_player}")
    game_board()
    print()

    # check for win or tie
    win_lose_draw_human()
    if not winner is None:
        quit()

    # time delay before making a move
    time.sleep(1)

    # switch players
    letter = "O"

    # take the computer's input
    computer_player = random.choice(inputed_values)
    if computer_player in available_list:
        board[computer_player] = letter
        available_list[computer_player] = letter
    else:
        continue

    inputed_values.remove(computer_player)
    print(f"Computer moved to {computer_player}")
    game_board()
    print()

    # check for win or tie
    win_lose_draw_computer()
    if not winner is None:
        quit()

