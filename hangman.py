import random
import string
# Create a function with the functionality
def start():
    # computer chooses from a list of words randomly
    player_guess = ""
    word_list = list()
    used_letters = list()
    fhand = open("words.txt", "rt")
    alphabet = string.ascii_uppercase
    for line in fhand:
        line = line.strip()
        word_list.append(line)

    rand_word = random.choice(word_list).upper()

    # Prompt the player for a value and do so until either the blanks are filled up or the player has attempted len(word) + 4 times
    i = 6
    while i != 0:
        print('Used letters: ', ' '.join(used_letters))
        word_blank = [a if a in used_letters else "_" for a in rand_word]
        print('Current word: ', ' '.join(word_blank))
        print(f"lives left: {i}")

        player_guess = input("\nEnter a letter, no repeat: ").upper()
        print("\n")
        # Make sure the player inputs a letter only
        if not player_guess in alphabet:
            print("Enter letters only!!\n")
            continue

        # assign each value in the rand_word a blank unless the player chooses correctly
        elif not player_guess in used_letters:
            used_letters.append(player_guess)
            word_blank = [a if a in used_letters else "_" for a in rand_word]

        # Make sure the player doesn't repeat a letter
        else:
            print("No repeat!! \n")
            continue
        word_blank = ' '.join(word_blank)

        if word_blank == ' '.join(rand_word):
            print(f"Yayy!!, you got the word {word_blank}")
            break
        elif not player_guess in rand_word:
            i -= 1 
        if i == 0:
            print(f"Sorry, you're out of lives, the word was {rand_word} \nYour guess: {word_blank}")

start()