from util import Coordinates

class Agent(object):
    """
    Class for the agent
    """
    def __init__(self, x, y, name):
        self.coordinates = Coordinates(x, y)
        self.name = name

    def move(self, coordinates):
        self.coordinates = coordinates

    def getPosition(self):
        return self.coordinates.x, self.coordinates.y

class Larva(Agent):
    """
    Class for the larva agent
    """
    def __init__(self, x, y):
        Agent.__init__(self, x, y, "Larva")

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
        Agent.__init__(self, x, y, "Bird")

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
