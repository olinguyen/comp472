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
from optparse import OptionParser


def runGame(ai, depth):
	newGame = Game(ai, depth)
	newGame.start()

if __name__ == '__main__':
	"""
	The main function called when the game is runs
	from the command line:

	> python hungrybirds.py

	See the usage string for more details
	> python hungrybirds.py --help
	"""
	parser = OptionParser()
	parser.add_option('-l', '--larva_ai', action='store_true', default=False,
						 help='Set AI player. e.g. -ai bird')
	parser.add_option('-d', '--depth', type="int", default=10,
						 help='Max depth that the minimax algorithm will go')
	(options, args) = parser.parse_args()
	depth = options.depth
	ai = options.larva_ai
	runGame(ai, depth)
