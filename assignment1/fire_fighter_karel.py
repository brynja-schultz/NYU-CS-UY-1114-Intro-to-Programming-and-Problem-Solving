from karel.stanfordkarel import * 

# Author: Brynja Schultz
# Assignment #1 - fire_fighter_karel.py
# Date due: 2021-09-30
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

"""
File: fire_fighter_karel.py
--------------------------------
When you finish writing this file, fire_fighter_karel.py should be
able to extinguish the fires in all three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
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

def find_building():
    """
    Karel moves from a building that has been extinguished to the next building that is currently on fire

    pre-condition: All 3 of Karel's sides are clear and Karel is not on a beeper
    post-condition: Karel is on a beeper and its right side is blocked
    """

    move()
    turn_right()
    move()

def extinguish_building():
    """
    Karel extinguishes all of the fire/picks up all of the beepers within a house

    pre-condition:Karel right side is blocked and is on a beeper
    post-condition: Karel is not on a beeper and all 3 sides are clear
    """

    while not right_is_clear():

        # Karel extinguishes the fire at the interval
        while on_beeper():
            pick_beeper()

        # if there is no wall, karel moves forward
        if front_is_clear():
            move()

        # Karel turns the corner if she hits a wall
        while not front_is_clear():
            turn_left()

def main():
    """
    Karel travels through 3 house and extinguishes all of the fires within them/picks
    up all of the beepers within the houses

    pre-condition: Karel is facing south next to the left-most house
    post-condition: Karel is facing east with front, left, right, and backside clear
    and having picked up all of the beepers/extinguished all of the fires
    """

    # extinguish building 1
    turn_right()
    move()
    extinguish_building()

    # extinguish building 2
    find_building()
    extinguish_building()

    # extinguish building
    find_building()
    extinguish_building()




####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
