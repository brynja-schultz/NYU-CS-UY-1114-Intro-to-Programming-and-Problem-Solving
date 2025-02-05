from karel.stanfordkarel import *

# Author: Brynja Schultz
# Assignment #1 - construction_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: construction_karel.py
--------------------------------
At present, the construction_karel.py file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to inspect the street corners in front of 
its starting position, and build a building (a vertical structure
that is 3 beepers tall) in each avenue that has been marked 
with a beeper, as described in the Assignment 1 instructions. Karel 
should end on the 5th avenue, facing east. 
"""

def turn_around():
    """
    Karel turns around 180 degrees

    pre-condition:  none
    post-condition: Karel has turned left 180 degrees and is facing the opposite directing of starting position
    """

    turn_left()
    turn_left()

def move_to_beeper():
    """
    Karel moves along the ground in order to find a partially constructed building to finish

    pre-condition: Karel is facing east and not on a beeper
    post-condition: Karel has moved forward one
    """

    # if partially constructed building NOT found, proceed forward in search
    if not on_beeper():
        move()

    # if partially constructed building IS found, begin building the building
    elif on_beeper():
        build_building()

def build_building():
    """
    Karel finishes the construction of the building by adding 2 beepers
    to its height

    pre-condition: Karel is on a beeper
    post-condition: Karel is not on a beeper, facing east
    """

    # moves upward to build building
    turn_left()
    move()

    # put beepers at each intersection to make building 3 beepers tall
    put_beeper()
    move()
    put_beeper()

    # karel has finished making building and descends
    turn_around()
    move()
    move()

    #karel has reached the ground and proceeds along the ground in search of more to build
    turn_left()
    move()

def main():
    """
    Karel searches for partially constructed buildings (a beeper) in
    order to complete the building to be 3 beepers tall

    pre-condition: Karel is facing east at (1,1)
    post-condition: Karel is facing east at (5,1)
    """

    #moves across 5 rows in search of buildings to build
    move_to_beeper()
    move_to_beeper()
    move_to_beeper()
    move_to_beeper()



####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
