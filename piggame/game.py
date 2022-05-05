#!/usr/bin/env python3
# Pedro Morales
# CPSC 386-03
# 2022-03-01
# pedrom2@csu.fullerton.edu
# @pedromorales451
#
# Lab 02-00
#
# This file contains and defines the PigGame class.
#

"""This module defines a PigGame class which is used to run Pig."""

import time
from .die import Die
from .player import Player, ComputerPlayer


class PigGame:
    """A PigGame class which runs an instance of a Pig game."""

    def __init__(self):
        """Constuctor for PigGame that creates an array of players."""
        self._players = []

    def opponent_score(self, myself):
        """Returns the score of the computer AI's opponent."""
        for player in self._players:
            if myself != player:
                return player.score

        # If opponent's score is not found, return 0.
        return 0

    @staticmethod
    def display_player_stats(myself, current_score):
        """Displays player's total score, current turn score, roll count."""
        print(
            "\n{}'s Total Score =".format(myself.name),
            myself.score,
            "  Current Score = ",
            current_score,
            "  # of Times Rolled = ",
            myself.times_rolled(),
        )
        time.sleep(2)

    @staticmethod
    def is_winner(myself):
        """Determines if the current player is the winner."""
        if myself.score >= 30:
            print("{} is the winner!".format(myself.name))
            print("Final Score: ", myself.score)
            return True

        return False

    def initialize_players(self, num_players):
        """For each human or computer player, a Player object is created."""
        # For each player...
        for i in range(num_players):
            # Create a die object.
            die = Die()

            # ask the user for their name.
            name = input("\nWhat is your name Player {}? ".format(i + 1))

            # Roll a die to determine who goes first.
            order = die.roll()
            die.print_roll(order)
            self._players.append(Player(name, order))

        # If num_players = 1, then computer AI is used as a player.
        if num_players == 1:
            order = die.roll()
            self._players.append(ComputerPlayer(order, self))
            print(self._players[1].name, " is rolling...")
            die.print_roll(order)

        print("\nBefore sorting ", self._players)
        time.sleep(2)

        # Players are sorted in ascending order, ties are handled.
        self._players.sort(key=lambda p: p.order, reverse=True)

        # Display the order of each player in ascending order.
        print("\nAfter sorting ", self._players)
        time.sleep(2)

    @staticmethod
    def first_roll(myself, rolled_number):
        """Determines if the player should roll again after 1st roll."""
        answer = ""

        if rolled_number == 1:
            print("Sorry, rolled a 1!")
            return ""

        if rolled_number + myself.score >= 30:
            myself.add_score(rolled_number)
            return ""

        if myself.am_i_human():
            answer = input("Do you wish to roll again? [Y/N] ")
        else:
            answer = myself.does_roll(rolled_number)

        return answer

    def run(self):
        """Runs an instance of PigGame."""
        # Create a Die object.
        die = Die()

        # Prompt user for the number of players.
        num_players = int(input("\nHow many players? [1-4] "))

        # While user enters an invalid number of players...
        while num_players <= 0 or num_players > 4:
            # prompt the user to re-enter the number of players.
            print("Number of players entered was not valid. Try Again.")
            num_players = int(input("\nHow many players? [1-4] "))

        self.initialize_players(num_players)

        player_index = 0

        # Circular Queue
        while True:
            # current player rolls a die
            rolled_number = die.roll()
            current_player = self._players[player_index]

            print("\n\nPlayer {} is up!".format(current_player))
            time.sleep(2)
            self.display_player_stats(current_player, 0)

            die.print_roll(rolled_number)
            current_player.increment_roll()

            current_score = rolled_number

            # Determines if player should decide to get a 2nd roll.
            answer = self.first_roll(current_player, rolled_number)

            if answer in ("N", "n"):
                print("{} skipped their turn.".format(current_player))
                current_player.add_score(current_score)
                time.sleep(2)

            while answer in ("Y", "y"):
                rolled_number = die.roll()
                self.display_player_stats(current_player, current_score)
                die.print_roll(rolled_number)
                current_player.increment_roll()

                if rolled_number != 1:
                    current_score += rolled_number
                    if current_score + current_player.score < 30:
                        if current_player.am_i_human():
                            answer = input("Do you wish to roll again? [Y/N] ")
                        else:
                            answer = current_player.does_roll(current_score)
                    elif current_score + current_player.score >= 30:
                        current_player.add_score(current_score)
                        break

                    if answer in ("N", "n"):
                        print("{} skipped their turn.".format(current_player))
                        current_player.add_score(current_score)
                        time.sleep(2)
                else:
                    print("Sorry, rolled a 1!")
                    break

            if self.is_winner(current_player):
                break

            current_player.reset_rolls()

            player_index = (player_index + 1) % len(self._players)
