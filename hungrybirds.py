"""
The main file that runs the Hungry Birds game.
hungrybirds.py holds the logic for the game along with the main code run a game.
"""

import sys
import types
import time
import random
import os
from game import Game
import argparse


def runGame(ai):
	newGame = Game(ai)
	newGame.start()

if __name__ == '__main__':
	"""
	The main function called when the game is runs
	from the command line:

	> python hungrybirds.py

	See the usage string for more details
	> python hungrybirds.py --help
	"""
	parser = argparse.ArgumentParser(description="Run the Hungry Birds game")
	parser.add_argument('-ai', action='store_true', help='Set AI player. e.g. -ai bird')

	args = parser.parse_args()
	ai = args.ai

	runGame(ai)
