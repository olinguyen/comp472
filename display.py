"""
ASCII graphics for game
"""
import string


def print_board(board):
    """
    Prints the game board
    """

    print "The board look like this: \n"

    #print the horizontal numbers
    print " ",
    for i in range(8):
        #print "  " + str(i+1) + "  ",
        print "  " + string.ascii_uppercase[i] + "  ",
    print "\n"
    s = "u"
    for i in range(8):

        #print the vertical line number
        if i != 9:
            print str(i+1) + "  ",
        else:
            print str(i+1) + " ",

        #print the board values, and cell dividers
        for j in range(8):
            if board[i][j] == -1:
                print ' ',
            else:
                print board[i][j],

            if j != 8:
                print " | ",
        print str(i+1) + " ",
        print

        #print a horizontal line
        if i != 8:
            print "  -----------------------------------------------"
        else:
            print
