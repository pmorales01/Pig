#!/usr/bin/env python3
# Pedro Morales
# CPSC 386-03
# 2022-03-01
# pedrom2@csu.fullerton.edu
# @pedromorales451
#
# Lab 02-00
#
# This file creates and runs a PigGame object.
#

"""This module is a toy module to demonstrate how to format a Python
    source file."""

from piggame import game

if __name__ == "__main__":
    GAME = game.PigGame()
    GAME.run()
