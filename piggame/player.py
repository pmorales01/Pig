#!/usr/bin/env python3
# Pedro Morales
# CPSC 386-03
# 2022-03-01
# pedrom2@csu.fullerton.edu
# @pedromorales451
#
# Lab 02-00
#
# This file contains and defines the Player and ComputerPlayer classes.
#

"""This module defines the human player and computer player AI classes."""

import time


class Player:
    """A player class to represent human players."""

    def __init__(self, name, order):
        """Constructor for a Player."""
        self._name = name
        self._score = 0
        self._order = order
        self._rolls = 0

    @property
    def name(self):
        """Returns the name of a player."""
        return self._name

    @property
    def order(self):
        """Returns the order of a player."""
        return self._order

    @property
    def score(self):
        """Returns the score of a player."""
        return self._score

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Player("{}", {})'.format(self._name, self._order)

    def add_score(self, roll):
        """Adds the amount rolled to total score."""
        self._score += roll

    def increment_roll(self):
        """Tracks the number of times a die was rolled."""
        self._rolls += 1

    def times_rolled(self):
        """Returns the number of times a player has rolled a die in a turn."""
        return self._rolls

    def reset_rolls(self):
        """Resets the number of times a player rolled a die in a turn."""
        self._rolls = 0

    @staticmethod
    def am_i_human():
        """Returns True if the player is a human player."""
        return True


class ComputerPlayer(Player):
    """A ComputerPlayer class to represent a computer player AI."""

    def __init__(self, order, game):
        super().__init__("Tiny Tim", order)
        self._game = game

    def am_i_human(self):
        return False

    def does_roll(self, current_score):
        """Defines conditions in which computer AI will roll a die."""
        opponent_score = self._game.opponent_score(self)
        time.sleep(2)

        if opponent_score >= 24 or self._score >= 24:
            print("You took another turn.")
            return "Y"

        if current_score > 10:
            return "N"

        if current_score < 10:
            print("You took another turn.")
            return "Y"

        if opponent_score >= self._score:
            print("You took another turn.")
            return "Y"

        return "N"
