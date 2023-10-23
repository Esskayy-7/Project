import random
initiate = input("Enter \'start\' to get started: ")
initiate = initiate.lower()
x = 15

def game_func(x):
    i = 0
    while i < x:
        if i == 0: print("Enter an integer from 1 - 10")    
        number = input("")
        try:
            number = int(number)
        except:
            print("Enter a numerical value only")
            continue
        i += 1 

        if number < random.randrange(1, x):
            print("Too small!!, Try again")
        elif number == random.randrange(1, x):
            print("Yayy!!, you guessed correctly")
            break
        else:
            print("Too large!!, try again")
        if i == x:
            print("\nYou have exhausted your number of trials")
    print(f"Game over \nNumber of trials: {i}")

if initiate == "start": game_func(x)