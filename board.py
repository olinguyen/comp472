from util import Coordinates
from util import getValue
from agent import *
import string

class Board:
    """
    Board class
    """
    def __init__(self):
        self.N = 8;
        self.agents = []
        self.agents.append(Larva(6, 3))
        for i in range(0, 8, 2):
            self.agents.append(Bird(7, i))

    def getLarva(self):
        return self.agents[0]

    def getBasicHeuristic(self):
        value = 0
        for agent in self.agents:
            x, y = agent.getPosition()
            if isinstance(agent, Larva):
                value += getValue(x, y)
            elif isinstance(agent, Bird):
                value -= getValue(x, y)
            else:
                raise Exception('Invalid agent type')
        return value

    def getPossibleMoves(self, agent):
        """
        Returns list of moves that are valid and available
        """
        possible_moves = []
        valid_moves = agent.getValidMoves()
        for move in valid_moves:
            if self.isPositionAvailable(move):
                possible_moves.append(move)
        return possible_moves

    def isPositionAvailable(self, coordinates):
        """
        Check if theres not already an agent there
        """
        for agent in self.agents:
            x, y = agent.getPosition()
            if x == coordinates.x and y == coordinates.y:
                return False
        return True

    def findAgent(self, coordinates):
        """
        Returns the Agent object given coordinates
        """
        for agent in self.agents:
            x, y = agent.getPosition()
            if x == coordinates.x and y == coordinates.y:
                return agent
        return None

    def display(self):
        """
        Prints the game board
        """
        board = []
        for i in range(self.N):
            board_row = []
            for j in range(self.N):
                board_row.append(' ')
            board.append(board_row)

        for agent in self.agents:
            x, y = agent.getPosition()
            if isinstance(agent, Larva):
                board[x][y] = 'L'
            elif isinstance(agent, Bird):
                board[x][y] = 'B'
            else:
                raise Exception('Invalid agent type')

        #print the horizontal numbers
        print " ",
        for i in range(self.N):
            #print "  " + str(i+1) + "  ",
            print "  " + string.ascii_uppercase[i] + "  ",
        print "\n"
        s = "u"
        for i in range(self.N):

            #print the vertical line number
            if i != 9:
                print str(self.N-i) + "  ",
            else:
                print str(self.N-i) + " ",

            #print the board values, and cell dividers
            for j in range(self.N):
                if board[i][j] == '':
                    print ' ',
                else:
                    print board[i][j],

                if j != self.N:
                    print " | ",
            print str(self.N-i) + " ",
            print

            #print a horizontal line
            if i != self.N:
                print "  -----------------------------------------------"
            else:
                print
