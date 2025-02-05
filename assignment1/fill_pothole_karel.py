from karel.stanfordkarel import *

# Author: Brynja Schultz
# Assignment #1 - fill_pothole_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: fill_pothole_karel.py
--------------------------------
When you finish writing the fill_pothole_karel.py file, Karel
should be able to fill the potholes of an arbitrary length
world, with potholes on assorted avenues of the first street.
A more in depth description of the problem can be found in the 
Assignment 1 instructions.  You should make sure that your 
program works for all of the sample worlds listed in the 
instructions for this problem.
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

def move_along_road():
    """
    Karel moves east along the road in search of potholes to fill

    pre-condition:  Karel is facing east
    post-condition: Karel is facing east and has filled the pothole with beepers
    """

    # move to next pothole
    while facing_east() and front_is_clear() and left_is_clear() and not right_is_clear():
        move()

    # fixes pothole
    if front_is_clear() and left_is_clear() and right_is_clear():
        turn_right()
        fill_pothole()

    # fixes pothole at end of the road
    elif not front_is_clear() and left_is_clear() and right_is_clear():
        turn_right()
        fill_pothole()

def exit_pothole():
    """
    Karel moves out of a filled pothole and returns to the street

    pre-condition:  Karel is facing south with front, left, and right sides blocked
    post-condition: Karel is facing east with its right slide blocked
    """

    #karel exits pothole
    turn_around()

    if front_is_clear() and not left_is_clear() and not right_is_clear():
        move()

    if front_is_clear() and not left_is_clear() and not right_is_clear():
        move()

    # karel goes back on the road
    if front_is_clear and right_is_clear():
        turn_right()
        move()

def fill_pothole():
    """
    Karel fills a pot hole with beepers

    pre-condition:  Karel is facing south with no wall in front of it
    post-condition: Karel is facing east with a wall beside it, having filled the pothole
    """

    # karel fills pothole with beepers if there are no beepers already there
    if front_is_clear():
        move()

        if not on_beeper():
            put_beeper()

    if front_is_clear():
        move()

        if not on_beeper():
            put_beeper()

    #karel exits the pothole
    exit_pothole()

    #karel goes back on the road in search for another pothole
    move_along_road()

def main():
    """
    karel fills any pothole it finds with 1 or 2 beepers depending on the depth

    pre-condition:  Karel if facing east
    post-condition: Karel is at farthest avenue west
    """

    move_along_road()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
