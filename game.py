"""
The logic behind how the Hungry Birds world works.
"""
from util import *
from agent import *
from board import Board
from copy import deepcopy
from search import *
import time

class Game:
    def __init__(self, turnAI=True):
        self.board = Board()
        self.larvaTurn = True
        self.currentAgent = self.board.getLarva()
        self.turnAI = turnAI

    def start(self):
        while True:
            self.board.display()
            self.playRound()

            self.larvaTurn = not self.larvaTurn
            if self.isOver():
                break

        self.end()

    def playRound(self):
        if self.larvaTurn:
            print "Larva turn"
        else:
            print "Bird Turn"

        if self.turnAI:
            """
            AI makes a move
            """
            t1 = time.time()
            tmp = deepcopy(self.board)
            root = Node(tmp, None, self.larvaTurn, 0)
            MiniMax(root)
            src_coordinates, dst_coordinates = root.getBestMove()
            t2 = time.time()

            print "AI made a move in", t2 - t1, "seconds"

            printIndex(src_coordinates)
            print '->',
            printIndex(dst_coordinates)
            print

            print "Root node score:", root.score
            self.currentAgent = self.board.findAgent(src_coordinates)
            self.currentAgent.move(dst_coordinates)
            self.turnAI = False
        else:
            while True:  # Loop until valid move
                try:
                    src_coordinates, dst_coordinates = self.readCommand()
                except:
                    print "Invalid input\n", "Please try again"
                    continue
                if self.validateMove(src_coordinates, dst_coordinates):
                    print "Valid move made"
                    self.turnAI = True
                    self.currentAgent.move(dst_coordinates)
                    break
                else:
                    print "Please try again"


    def readCommand(self):
    	"""
    	Processes the command used to run the game from command line
    	"""
        cmd = raw_input("Enter move >> ")

        if cmd is None or not ' ' in cmd:
            raise Exception("Improper format")

        command_string = cmd.split(' ')
        src = command_string[0]
        dst = command_string[1]
        src_coordinates = ConvertToIndex(src)
        dst_coordinates = ConvertToIndex(dst)

        return src_coordinates, dst_coordinates

    def validateMove(self, src_coordinates, dst_coordinates):
        """
        Verify correct player's turn, and valid moves
        """
        # Ensure coordinates are not null
        if src_coordinates == None or dst_coordinates == None:
            print "Invalid coordinates"
            return False

        # Ensure source coordinates are non-empty
        agent = self.board.findAgent(src_coordinates)
        if agent is None:
            print "Could not find agent at given coordinates"
            return False

        # Ensure that turns are respected
        if not (isinstance(agent, Larva) and self.larvaTurn or \
            isinstance(agent, Bird) and not self.larvaTurn):
            print "Wrong turn!"
            return False

        # Ensure that destination is valid
        self.currentAgent = agent
        valid_moves = agent.getValidMoves()
        isValid = False
        for move in valid_moves:
            if move.x == dst_coordinates.x and move.y == dst_coordinates.y:
                isValid = True
        if not isValid:
            print "Destination is not valid"
            return False

        # Ensure that the destination is non-empty
        move = Coordinates(dst_coordinates.x, dst_coordinates.y)
        if not self.board.isPositionAvailable(move):
            print "Destination is a non-empty position"
            return False

        return True

    def end(self):
        self.board.display()
        if self.larvaTurn:
            print "Game Over! Bird wins"
        else:
            print "Game Over! Larva wins"
        print "Thank you for playing!"

    def isNoRemainingMoves(self, isLarvaTurn):
        noMoreMoves = True
        for agent in self.board.agents:
            if isinstance(agent, Larva) and isLarvaTurn:
                if self.board.getPossibleMoves(agent):
                    noMoreMoves = False
            elif isinstance(agent, Bird) and not isLarvaTurn:
                if self.board.getPossibleMoves(agent):
                    noMoreMoves = False
        return noMoreMoves

    def isOver(self):
        """
        Method to determine if game is over
        """
        # Larva wins if Larva is found on the bottom rank
        x, y = self.currentAgent.getPosition()
        if isinstance(self.currentAgent, Larva) and x == 7:
            return True

        # Check if the current player still has moves
        return self.isNoRemainingMoves(self.larvaTurn)
