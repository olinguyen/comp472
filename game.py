"""
The logic behind how the Hungry Birds world works.
TODO: Create board class?
"""
import string


class Board:
    """
    Board class
    """
    def __init__(self):
        self.N = 8;
        self.players = []
        self.players.append(Larva(6, 3))
        for i in range(0, 8, 2):
            self.players.append(Bird(7, i))
        self.board = self.create(self.players)

    def create(self, players):
        board = []
        for i in range(self.N):
            board_row = []
            for j in range(self.N):
                board_row.append(' ')
            board.append(board_row)
        for player in self.players:
            x, y = player.get_position()
            if player.__class__ == Larva:
                board[x][y] = 'L'
            elif player.__class__ == Bird:
                board[x][y] = 'B'
            else:
                raise Exception('Invalid player type')
        return board

    def display(self):
        """
        Prints the game board
        """

        print "The board look like this: \n"

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
                if self.board[i][j] == '':
                    print ' ',
                else:
                    print self.board[i][j],

                if j != self.N:
                    print " | ",
            print str(self.N-i) + " ",
            print

            #print a horizontal line
            if i != self.N:
                print "  -----------------------------------------------"
            else:
                print

class Player(object):
    """
    Class for the larva player
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, pos):
        pass

    def get_position(self):
        return self.x, self.y

class Larva(Player):
    """
    Class for the larva player
    """
    def __init__(self, x, y):
        Player.__init__(self, x, y)

class Bird(Player):
    """
    Class for bird player
    """
    def __init__(self, x, y):
        Player.__init__(self, x, y)

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
