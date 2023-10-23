import random

# create a function that asks the user for feedback when calles
def start():
    low_bound = 1
    feedback = ''
    dum = None
    guess = None
    high_bound = None
    # creates a loop that ends when the computer guesses correctly
    while high_bound != low_bound and feedback != 'c':
        # prompt for a guess
        high_bound = input("guess a number from 1 and input the end range of what you want the computer to guess: ")

        # make sure the inputed value is an integer
        try:
            high_bound = int(high_bound)
        except: 
            print("Please enter a numerical value only")
            continue
        # guess until feedback is confirmed to be true
        while feedback != 'c':
            if low_bound == high_bound:
                guess = low_bound
                break
            elif low_bound > high_bound:
                dum = low_bound
                low_bound = high_bound
                high_bound = dum
    
            guess = random.randrange(low_bound, high_bound)
            feedback = input(f'If {guess} is too high, enter \'h\' if it\'s too low enter \'l\', and if it\'s correct, enter \'c\': ').lower()
            if feedback == 'l':
                low_bound = guess + 1
            elif feedback == 'h':
                high_bound = guess - 1
            elif feedback == 'c':
                print("Yayy, correct!!")
            else:
                print("Please input exactly as instructed")
                continue
    print(f"The value was narrowed down to {guess}")
    confirm = input("Is this correct, \'y\' for yes, and \'n\' for no: ")
    if confirm.lower() == 'y':
        print("Yayy!!")
    else:
        print("An error must have occured when inputing")

initiate = input("Enter \'start\' to begin: ").lower()
if initiate == 'start': start()