import random
pick_set = set(('r', 'p', 's'))

def start():
    Your_Score = 0
    Computer_Score = 0
    # Play rock, paper scissors 3 times
    i = 0
    while i < 3:
        # prompt the player for an entry
        player = input("Enter \'r\' for rock, \'p\' for paper, and \'s\' for scissors: ")

        # make sure the player entered correctly
        if player not in pick_set: 
            print("Enter exactly as instructed!!")
            continue
        
        # check if the computer and the player entered the same value
        comp = random.choice(['r', 'p', 's'])
        if player == comp:
            print("It's a tie")
            continue

        # Compare the computer and the player's input and assign a result
        def is_win(p, c):
            if (p == 'r' and c == 's') or (p == 'p' and c == 'r') or \
                (p == 's' and c == 'p'):
                return "You win!"
            else:
                return "Computer wins!"
        win = is_win(player, comp)
        print(win)

        # calculate the score
        if win == "You win!": 
            Your_Score  += 1
        else:
            Computer_Score += 1      
        i += 1
        
    # Output the results
    print("\n")
    print(f"Player score: {Your_Score} \nComputer score: {Computer_Score}")

    # Check for the winner
    if Your_Score > Computer_Score:
        print("You are the winner of the game!!")
    else: 
        print("Your opponent won the game!!")

# call the start() function to begin the game
initiate = input("Enter \'start\' to begin: ")
if initiate == 'start': start()