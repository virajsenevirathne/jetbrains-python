import random


def mask_word():
    """
    Get the masked word to show to the player
    :return: masked string
    """
    masked_string = [char if char in letters else "-" for char in selected_word]
    return "".join(masked_string)


def get_input():
    """
    Get a correctly formatted input from the user. Correct input is a single lower case letter.
    :return: True if letter appear in the word, player input letter
    """
    while True:
        print(f"\n{mask_word()}")
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.islower():
            print("Please enter a lowercase English letter")
        else:
            return letter in selected_word, letter


def print_outcome(player_won):
    """
    Helper function to write the game outcome to the palyer.
    :param player_won: True if player won the game
    """
    if player_won:
        print(f"You guessed the word {selected_word}!\n"
              f"You survived!\n")
    else:
        print("You lost!\n")


def play_game():
    """
    This function takes care of the game itself. It tracks number of lives and calculates outcomes based on user inputs.
    """
    global wrong_letters
    global letters
    lives = 8
    while lives != 0:
        is_valid, ch = get_input()
        if is_valid:
            if ch not in letters:
                letters.add(ch)
                if mask_word() == selected_word:
                    print_outcome(True)
                    break
            else:
                print("You've already guessed this letter")
        else:
            if ch in wrong_letters:
                print("You've already guessed this letter")
            else:
                wrong_letters.add(ch)
                print("That letter doesn't appear in the word")
                lives -= 1
    else:
        print_outcome(False)


print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

selected_word = random.choice(words)

letters = set()  # Set to hold correctly guessed letters by the user
wrong_letters = set()  # Set to hold incorrect letters given by the user

while True:
    user_input = input("Type \"play\" to play the game, \"exit\" to quit: ")

    if user_input == "play":
        play_game()
    elif user_input == "exit":
        break
