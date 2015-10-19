"""
The logic behind how the Hungry Birds world works.
"""
import string
from util import ConvertToIndex


class Game:
    def __init__(self):
        self.board = Board()
        self.larvaTurn = True
        self.currentAgent = None

    def start(self):
        while True:
            self.board.display()
            self.playRound()
            if self.isOver():
                break
            self.larvaTurn = not self.larvaTurn

        self.end()

    def playRound(self):
        if self.larvaTurn:
            print "Larva turn"
        else:
            print "Bird Turn"

        while True:  # Loop until valid move
            src_coordinates, dst_coordinates = self.readCommand()
            if src_coordinates and self.validateMove(src_coordinates, dst_coordinates):
                print 'Valid move made'
                break
            print 'Invalid move made'

        self.currentAgent.move(dst_coordinates)

    def readCommand(self):
    	"""
    	Processes the command used to run the game from command line
    	"""
        cmd = raw_input("Enter move >> ")

        if cmd is None or not ' ' in cmd:
            return None, None

        command_string = cmd.split(' ')
        src = command_string[0]
        dst = command_string[1]
        try:
            src_coordinates = ConvertToIndex(src)
            dst_coordinates = ConvertToIndex(dst)
        except:
            return None, None
        return src_coordinates, dst_coordinates

    def isPositionAvailable(self, coordinates):
        """
        Check if theres not already an agent there
        """
        for agent in self.board.agents:
            x, y = agent.getPosition()
            if x == coordinates.x and y == coordinates.y:
                return False
        return True

    def validateMove(self, src_coordinates, dst_coordinates):
        """
        Verify correct player's turn, and valid moves
        """
        agent = self.board.findAgent(src_coordinates)

        if agent is None:
            print "Could not find agent at given coordinates"
            return False
        self.currentAgent = agent
        valid_moves = agent.getValidMoves()

        if not (agent.__class__ == Larva and self.larvaTurn or \
            agent.__class__ == Bird and not self.larvaTurn):
            print "Wrong turn!"
            return False
        else:
            for move in valid_moves:
                # If valid move == desired location
                if move.x == dst_coordinates.x and move.y == dst_coordinates.y:
                    return self.isPositionAvailable(move)
        return False

    def end(self):
        self.board.display()

    def isOver(self):
        x, y = self.currentAgent.getPosition()
        if self.currentAgent.__class__ == Larva and x == 7:
            print "Game Over! Larva wins"
            return True

        noMoreMoves = True
        for agent in self.board.agents:
            valid_moves = agent.getValidMoves()

            if agent.getValidMoves() and agent.__class__ == Bird:
                noMoreMoves = False
            if valid_moves and agent.__class__ == Larva:
                for move in valid_moves:
                    if self.isPositionAvailable(move):
                        return False
                print "Game Over! Bird wins"
                return True

        if noMoreMoves:
            print 'Game Over! Larva wins'
        return noMoreMoves

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
    Class for the agent
    """
    def __init__(self, x, y):
        self.coordinates = Coordinates(x, y)

    def move(self, coordinates):
        self.coordinates = coordinates

    def getPosition(self):
        return self.coordinates.x, self.coordinates.y

class Larva(Agent):
    """
    Class for the larva agent
    """
    def __init__(self, x, y):
        self.name = "Larva"
        Agent.__init__(self, x, y)

    def getValidMoves(self):
        x, y = self.getPosition()
        up_right = Coordinates(x - 1, y + 1)
        up_left = Coordinates(x - 1, y - 1)
        down_right = Coordinates(x + 1, y + 1)
        down_left = Coordinates(x + 1, y - 1)
        moves = [up_right, up_left, down_right, down_left]
        validMoves = []
        for move in moves:
            if 0 <= move.x < 8 and 0 <= move.y < 8:
                validMoves.append(move)
        return validMoves

class Bird(Agent):
    """
    Class for bird agent
    """
    def __init__(self, x, y):
        self.name = "Bird"
        Agent.__init__(self, x, y)

    def getValidMoves(self):
        x, y = self.getPosition()
        up_right = Coordinates(x - 1, y + 1)
        up_left = Coordinates(x - 1, y - 1)
        moves = [up_right, up_left]
        validMoves = []
        for move in moves:
            if 0 <= move.x < 8 and 0 <= move.y < 8:
                validMoves.append(move)
        return validMoves

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
