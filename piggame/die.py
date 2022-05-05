#!/usr/bin/env python3
# Pedro Morales
# CPSC 386-03
# 2022-03-01
# pedrom2@csu.fullerton.edu
# @pedromorales451
#
# Lab 02-00
#
# This file contains and defines the class Die.
#

"""This module defines a Die class which is used to represent a 6-sided die."""

import time
from random import randrange


class Die:
    """A Die class to represent rolling a 6-sided die."""

    def __init__(self):
        """Constructor for Die."""

    @staticmethod
    def roll():
        """Rolls a 6-sided die."""
        return randrange(1, 7)

    @staticmethod
    def print_roll(rolled_number):
        """Prints out the number that was rolled using the die."""
        roll_msg = "You rolled {}\n".format(rolled_number)

        for char in roll_msg:
            print(char, end="", flush=True)
            time.sleep(0.1)
