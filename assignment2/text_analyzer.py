# Author: Brynja Schultz
# Assignment #2 - TextAnalyzer
# Date due: 2021-10-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT FUNCTIONS BELOW ########

def character_is_digit(char):
    """Indicates whether the value referenced by char parameter
    is a digit character

    :param char: character to check
    :return: True when char is a digit character, False otherwise

    >>> test_char = 'b'
    >>> character_is_digit(test_char)
    False
    >>> test_char = '2'
    >>> character_is_digit(test_char)
    True
    """

    return char.isdigit()


def character_is_letter(char):
    """Indicates whether the value referenced by char parameter
    is a letter

    :param char: character to check
    :return: True when char is a letter, False otherwise

    >>> test_char = 'b'
    >>> character_is_letter(test_char)
    True
    >>> test_char = '2'
    >>> character_is_letter(test_char)
    False
    """

    return char.isalpha()

####### DO NOT EDIT FUNCTIONS ABOVE ########


def character_is_whitespace(char):
    """Indicates whether the value referenced by char parameter
    is a whitespace character (' ', '\n', '\t')
    :param char: character to check
    :return: True when char is space character, False otherwise
    >>> test_char = ' '
    >>> character_is_whitespace(test_char)
    True
    >>> test_char = '#'
    >>> character_is_whitespace(test_char)
    False
    >>> test_char = '\n'
    >>> character_is_whitespace(test_char)
    True
    >>> test_char = '\t'
    >>> character_is_whitespace(test_char)
    True
    """
    if char == ' ':
        return True
    elif char == '\n':
        return True
    elif char == '\t':
        return True
    else:
        return False


def character_ends_sentence(char):
    """Indicates whether the value referenced by char parameter
    is a period, question mark, or exclamation point
    :param char: character to check
    :return: True when char ends sentence, False otherwise
    >>> test_char = 'k'
    >>> character_ends_sentence(test_char)
    False
    >>> test_char = '.'
    >>> character_ends_sentence(test_char)
    True
    >>> test_char = '?'
    >>> character_ends_sentence(test_char)
    True
    >>> test_char = '!'
    >>> character_ends_sentence(test_char)
    True
    """
    # returns True if character ends a sentence
    if char == '.':
        return True
    elif char == '!':
        return True
    elif char == '?':
        return True

    # returns False if character does NOT end a sentence
    else:
        return False


def print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences):
    """Prints the number of total characters, spaces, digits, letters,
    and sentences identified in the text being analyzed.
    :param num_chars: number of total characters in text
    :param num_spaces: number of spaces in text
    :param num_digits: number of digits in text
    :param num_letters: number of letters in text
    :param num_sentences: number of sentences in text
    :return: None
    >>> num_chars = 234
    >>> num_spaces = 14
    >>> num_digits = 16
    >>> num_letters = 201
    >>> num_sentences = 21
    >>> print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences)
    <BLANKLINE>
    Count of characters: 234
    Count of spaces: 14
    Count of digits: 16
    Count of letters: 201
    Count of sentences: 21
    <BLANKLINE>
    """
    print("\nCount of characters: ", num_chars, "\nCount of spaces: ", num_spaces, "\nCount of digits: ", num_digits, "\nCount of letters: ", num_letters, "\nCount of sentences: ", num_sentences)


def analyze_text():
    """Calls the functions to compute the number of total characters,
    spaces, digits, letters, and sentences in user-supplied text and to
    output the final counts when text input by user.
    :return: True when text provided, False when no text provided
    """
    text = input("\nPlease enter text to analyze (press ENTER/return without text to exit): ")

    # returns False if return was pressed/no text was entered
    if text == '':
        return False

    # returns True if text is inputted
    else:
        characters = len(text)  # total number of characters in the text

        # setting count of types of characters to 0
        whitespaces = 0
        digits = 0
        letters = 0
        ends_sentence = 0

        # testing each character in the text & increased the count of each type of character as they are found
        for i in range(len(text)):
            if character_is_whitespace(text[i]):
                whitespaces += 1
            elif character_is_digit(text[i]):
                digits += 1
            elif character_is_letter(text[i]):
                letters += 1
            elif character_ends_sentence(text[i]):
                ends_sentence += 1

        # prints total data on text
        print_results(characters, whitespaces, digits, letters, ends_sentence)

        return True


def run_text_analyzer():
    """Text is analyzed when it is inputted by user, program finishes when nothing is inputted
    """
    # text is analyzed while text is inputted
    while analyze_text():
        pass

    # program ends when no text is inputted
    else:
        print("\nGoodbye.")


def main():
    """Runs a program for analyzing character counts from
    input text
    """
    print("Welcome to the Text Analyzer!")
    run_text_analyzer()

    
####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
