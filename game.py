"""
The logic behind how the Hungry Birds world works.
"""
import string
from util import ConvertToIndex


class Game:
    def __init__(self):
        self.board = Board()
        self.larvaTurn = True

    def start(self):
        while not self.isOver():
            self.board.display()
            self.playRound()
            self.larvaTurn = not self.larvaTurn
        self.end()

    def playRound(self):
        if self.larvaTurn:
            print "Larva turn"
        else:
            print "Bird Turn"

        src_coordinates, dst_coordinates = self.readCommand()
        agent = self.board.findAgent(src_coordinates)
        print agent
        #self.board.validateMove(self.larvaTurn, src_coordinates, dst_coordinates)
        agent.move(dst_coordinates)

    def readCommand(self):
    	"""
    	Processes the command used to run the game from command line
    	"""
        cmd = raw_input("Enter move")
        src, dst = cmd.split(' ')
        src_coordinates = ConvertToIndex(src)
        dst_coordinates = ConvertToIndex(dst)
        return src_coordinates, dst_coordinates

    def end(self):
        pass

    def isOver(self):
        return False

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

    def validateMove():
        pass

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
            if agent.__class__ == Larva:
                board[x][y] = 'L'
            elif agent.__class__ == Bird:
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


class Agent(object):
    """
    Class for the larva player
    """
    def __init__(self, x, y):
        coordinates = Coordinates(x, y)
        self.coordinates = coordinates

    def move(self, coordinates):
        self.coordinates = coordinates

    def getPosition(self):
        return self.coordinates.x, self.coordinates.y

class Larva(Agent):
    """
    Class for the larva player
    """
    def __init__(self, x, y):
        Agent.__init__(self, x, y)

class Bird(Agent):
    """
    Class for bird player
    """
    def __init__(self, x, y):
        Agent.__init__(self, x, y)

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
