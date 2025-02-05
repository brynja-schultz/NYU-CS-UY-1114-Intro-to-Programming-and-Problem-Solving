# Author: Brynja Schultz
# Assignment #4 - Guessing Game
# Date due: 2021-11-11
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW (changing MAX_MISSES is ok) ########
import random
import sys

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1


def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """

    print()
    print('=' * BORDER_LENGTH)
    print()

    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))

####### DO NOT EDIT CODE ABOVE (changing MAX_MISSES is ok) ########


def blank_chars(word):
    """Returns a list of underscore characters with the same length as word.
    :param word: target word as a string
    :return: a list of underscore characters ('_')
    >>> blank_chars("happiness")
    ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    """
    word_list = []

    for i in range(len(word)):
        word_list += ['_']

    return word_list


def space_chars(chars):
    """Returns a string with the characters in chars list separated by spaces.
    :param chars: a list of characters
    :return: a string containing characters in chars with intervening spaces
    >>> space_chars(['h', '_', 'p', 'p', '_', 'n', '_', '_', '_'])
    'h _ p p _ n _ _ _'
    """
    characters_string = " ".join(chars)

    return characters_string


def get_guess():
    """Prompts the user for a guess to check for the game's current word. When the user
    enters input other than a single character, the function prompts the user again
    for a guess. Only when the user enters a single character will the prompt for
    a guess stop being displayed. The function returns the single-character guess
    entered by the user.
    :return guess: a single character guessed by user
    """
    guess = input("Guess:\t")

    while not guess.isalpha() or len(guess) > SINGLE_CHAR_LENGTH:
        guess = input("Guess:\t")

    return guess.lower()


def check_guess(word, guess):
    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.
    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """
    positions = []

    for i in range(len(word)):
        if word[i] == guess:
            positions += [i]

    return positions


def update_chars(chars, guess, positions):
    """Updates the list of characters, chars, so that the characters
    at the index values in the positions list are updated to the
    character guess.
    :param chars: a list of characters
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    for i in range(len(positions)):
        chars[positions[i]] = guess


def add_to_misses(misses, guess):
    """Adds the character guess to the misses list.
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :return: None
    """
    misses += guess


def update_state(chars, misses, guess, positions):
    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    if len(positions) > 0:
        update_chars(chars, guess, positions)

    else:
        add_to_misses(misses, guess)


def is_round_complete(chars, misses):
    """Indicates whether or not a round has ended. This function returns True
    when the user has successfully guessed the target word or exceeds the
    number of allowed misses. Otherwise, the function returns False,
    indicating that the round is not complete. A message revealing the
    user's success or failure guessing the target word is output by this
    function when the round is complete.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :return status: True when round is finished, False otherwise
    """
    if len(misses) > MAX_MISSES:
        print("")
        print("SORRY! NO GUESSES LEFT.")
        return True

    elif chars.count('_') == 0:
        print("")
        print("YOU GOT IT!")
        return True

    else:
        return False


def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function
    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """
    word_list = []

    file = open(filepath, 'r')

    write_file = open("new_file.txt", 'w')

    for line in file:
        word_list += [line.strip()]

    write_file.close()
    file.close()

    return word_list


def get_word(words):
    """Selects a single word randomly from words list and returns it.
    :param words: list of strings
    :return word: string from words list
    """
    word = words[random.randrange(0, len(words)-1)]

    return word


def is_game_complete():
    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.
    :return response: boolean representing game completion status
    """
    play_again = 0

    while play_again != 'n' or play_again != 'N' or play_again != 'Y' or play_again != 'y':

        play_again = input("Play again (Y/N)? ")

        if play_again.lower() == 'y':
            return False

        elif play_again.lower() == 'n':
            return True


def run_guessing_game(words_filepath):
    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.
    :param words_filepath: the location of the file of words for the game
    :return: None
    """
    # checks if file is valid
    try:
        list_of_words = read_words(words_filepath)
    except FileNotFoundError:
        print("The provided file location is not valid. Please enter a valid path to a file.")
        return None

    print("Welcome to The Guessing Game!")
    play_again = False

    while not play_again:
        # game continues when user wants to play again
        word = get_word(list_of_words)
        hidden_word = blank_chars(word)
        misses = []

        while not is_round_complete(hidden_word, misses):
            # user can continue to guess while they are under the max guesses and have yet to guess the word
            display_game_state(hidden_word, misses)
            # returns user's guess
            guess = get_guess()
            # returns position of guess
            positions = check_guess(word, guess)

            if len(positions) == 0:
                add_to_misses(misses, guess)

            else:
                update_chars(hidden_word, guess, positions)

        # displays word regardless if the user won or lost
        display_game_state(word, misses)
        play_again = is_game_complete()

    print("\nGoodbye.")


def main():

    ########## DO NOT EDIT ASSIGNMENT STATEMENT BELOW #########

    filepath = sys.argv[-1]

    ########## DO NOT EDIT ASSIGNMENT STATEMENT ABOVE #########

    # call run_guessing_game() with filepath as argument and remove pass below
    run_guessing_game(filepath)


if __name__ == '__main__':
    main()
