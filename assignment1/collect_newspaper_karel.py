from karel.stanfordkarel import *

# Author: Brynja Schultz
# Assignment #1 - collect_newspaper_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: collect_newspaper_karel.py
--------------------------------
At present, the collect_newspaper_karel.py file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up and 
drop off the newspaper (represented by a beeper, of course), and 
then return to the initial position in the upper left corner of 
the house.
"""

def turn_right():
    """
    Instructs Karel to perform a right turn.

    pre-condition:  Karel is be facing any of the four cardinal directions.
    post-condition: Karel will have performed a 45-degree turn in the RIGHT direction.
    """

    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """
    Karel turns around 180 degrees

    pre-condition:  none
    post-condition: Karel has turned left 180 degrees and is facing the opposite directing of starting position
    """

    turn_left()
    turn_left()

def move_to_newspaper():
    """
    Karel moves from starting point inside of the house to the newspaper outside of the house

    pre-condition: Karel is facing east at starting point
    post-condition: Karel is on the beeper that symbolizes the newspaper outside of the house
    """

    #move to wall
    while front_is_clear():
        move()

    #turn right at wall
    if not front_is_clear():
        turn_right()

    #exit the door
    move()
    turn_left()
    move()
    move()

    #turn to reach newspaper
    turn_left()
    move()

def move_newspaper():
    """
    Karel moves the newspaper from outside of the house to inside

    pre-condition: Karel is on the beeper that symbolizes the newspaper outside of the house
    post-condition: Karel is on the beeper that symbolizes the newspaper inside of the house
    """

    #pick up newspaper
    pick_beeper()

    #reenter through door
    turn_around()
    move()
    turn_right()

    #enter house
    move()

    #move to drop off point
    move()
    turn_left()
    move()

    #drop off newspaper
    put_beeper()


def return_to_start():
    """
    Karel returns to starting position after dropping off newspaper

    pre-condition: Karel is on the beeper that symbolizes the newspaper inside of the house
    post-condition: Karel is at starting position
    """

    turn_right()

    #move to wall
    while front_is_clear():
        move()

    #turn right
    turn_right()

    #move to wall
    while front_is_clear():
        move()

def main():
    """
    Karel exits the house, picks up the newspaper,
    drops it off at the bottom left corner of the house,
    and returns to the starting position in the top right corner

    pre-condition: karel is at north-western corner of the house facing east
    post-condition: karel is at north-western corner of the house having moved the newspaper
    """

    move_to_newspaper()
    move_newspaper()
    return_to_start()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
