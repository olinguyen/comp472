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
            try:
                src_coordinates, dst_coordinates = self.readCommand()
            except:
                print "Invalid input\n", "Please try again"
                continue
            if self.validateMove(src_coordinates, dst_coordinates):
                print "Valid move made"
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
        if not (agent.isLarva and self.larvaTurn or \
            not agent.isLarva == Bird and not self.larvaTurn):
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
        print "Thank you for playing!"

    def isNoRemainingMoves(self, isLarva):
        noMoreMoves = True
        for agent in self.board.agents:
            if agent.isLarva == isLarva:
                possible_moves = []
                valid_moves = agent.getValidMoves()
                for move in valid_moves:
                    if self.board.isPositionAvailable(move):
                        possible_moves.append(move)
                if possible_moves:
                    noMoreMoves = False
        return noMoreMoves

    def isOver(self):
        """
        Method to determine if game is over
        """
        # Larva wins if Larva is found on the bottom rank
        x, y = self.currentAgent.getPosition()
        if self.currentAgent.isLarva and x == 7:
            print "Game Over! Larva wins"
            return True

        # Larva wins if Birds cannot move
        if self.isNoRemainingMoves(False):
            print 'Game Over! Larva wins'
            return True

        # Birds win if Larva cannot move
        if self.isNoRemainingMoves(True):
            print "Game Over! Bird wins"
            return True

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
            if agent.isLarva:
                board[x][y] = 'L'
            elif not agent.isLarva:
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
    def __init__(self, x, y, name, isLarva):
        self.coordinates = Coordinates(x, y)
        self.name = name
        self.isLarva = isLarva

    def move(self, coordinates):
        self.coordinates = coordinates

    def getPosition(self):
        return self.coordinates.x, self.coordinates.y

class Larva(Agent):
    """
    Class for the larva agent
    """
    def __init__(self, x, y):
        Agent.__init__(self, x, y, "Larva", True)

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
        Agent.__init__(self, x, y, "Bird", False)

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
