# Author: Brynja Schultz
# Assignment #3 - Blackjack
# Date due: 2021-10-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card
    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """
    card = random.choice(CARD_LABELS)

    return card


def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)
    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value
    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """
    if card_label == 'A':
        card_value = ACE_VALUE
    elif card_label == 'J' or card_label == 'Q' or card_label == 'K':
        card_value = FACE_CARD_VALUE
    else:
        card_value = int(card_label)

    return card_value


def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """
    player_card1 = deal_card()
    player_card2 = deal_card()

    total_value = get_card_value(player_card1) + get_card_value(player_card2)

    print("Player drew", player_card1, "and", player_card2 + ".")
    print("Player's total is", str(total_value) + ".")

    player_choice = 0

    while total_value < BLACKJACK and player_choice != 's':
        player_choice = input("\nHit (h) or Stay (s)? ")
        if player_choice == 'h':
            new_card = deal_card()
            total_value += get_card_value(new_card)

            print("\nPlayer drew", str(new_card) + ".")
            print("Player's total is", str(total_value) + ".")
    if player_choice == 's':
        print()

    return total_value


def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total
    :return: the total value of the cards dealt
    """
    dealer_card1 = deal_card()
    dealer_card2 = deal_card()

    total_value = get_card_value(dealer_card1) + get_card_value(dealer_card2)

    print("The dealer has", dealer_card1, "and", str(dealer_card2) + ".")
    print("Dealer's total is", str(total_value) + ".\n")

    while total_value <= DEALER_THRESHOLD:
        new_card = deal_card()
        total_value += get_card_value(new_card)

        print("Dealer drew", str(new_card) + ".")
        print("Dealer's total is", str(total_value) + ".\n")

    return total_value


def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.
    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """
    """if player_total < 21:
        dealer_total = deal_more_to_dealer(dealer_total)"""
    if dealer_total < player_total <= 21 or dealer_total > 21:
        print("YOU WIN!\n")
    else:
        print("YOU LOSE!\n")


def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome
    :return: None
    """
    print("Let's Play Blackjack!")

    play_again = 0

    while play_again != 'N':
        print()
        player = deal_cards_to_player()
        if player <= BLACKJACK:
            dealer = deal_cards_to_dealer()
            determine_outcome(player, dealer)
        else:
            print("\nYOU LOSE!")
            print()
        play_again = input("Play again (Y/N)? ")
        while play_again != 'Y' and play_again != 'N':
            play_again = input("\nPlay again (Y/N)? ")

    print("\nGoodbye.")


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below
    play_blackjack()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
