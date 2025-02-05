# Author: Brynja Schultz
# Assignment #2 - Calculator
# Date due: 2021-10-14
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def print_menu():
    """Prints available calculator operations.
    :return: None
    >>> print_menu()
    <BLANKLINE>
    1) Perform addition
    2) Perform subtraction
    3) Perform multiplication
    4) Perform division
    """
    print("\n1) Perform addition", "\n2) Perform subtraction", "\n3) Perform multiplication", "\n4) Perform division")


def do_calculation():
    """Prompts user for calculation choice and calls
    function to perform calculation
    :return: the character entered by user
    """

    option = 0

    while option != 'q':
        # prints menu options to user
        print_menu()

        option = input("Please enter an option (1-4) or 'q' to quit: ")

        # function quits when user inputs 'q'
        if option == 'q':
            print("\nGoodbye.")

        # calculator operator occurs, depending on the option inputted
        elif int(option) == 1:
            do_addition()
        elif int(option) == 2:
            do_subtraction()
        elif int(option) == 3:
            do_multiplication()
        elif int(option) == 4:
            do_division()

        # if user inputs something other than the options listed, they are asked again to input an option
        else:
            print("That was not a valid choice. Try again.")


def do_addition():
    """Informs user that addition was chosen, sums two
    numbers input by the user, and outputs the result.
    :return: None
    """
    print("\nYou have chosen the addition operation.")

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("The sum is", first_number + second_number)


def do_subtraction():
    """Informs user that subtraction was chosen, calculates
    the difference between two numbers input by the user, and
    outputs the result.
    :return: None
    """
    print("\nYou have chosen the subtraction operation.")

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("The difference is", first_number - second_number)


def do_multiplication():
    """Informs user that multiplication was chosen, multiplies two
    numbers input by the user, and outputs the result.
    :return: None
    """
    print("\nYou have chosen the multiplication operation.")

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("The product is", first_number * second_number)


def do_division():
    """Informs user that division was chosen, divides two
    numbers input by the user, and outputs the result.
    :return: None
    """
    print("\nYou have chosen the division operation.")

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("The result of the division of the two numbers is", first_number / second_number)


def main():
    """Runs a program for performing basic arithmetic
    operations between two numbers
    """
    print("Welcome to the CS 1114 Calculator!")
    do_calculation()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
