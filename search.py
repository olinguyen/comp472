from board import Board
from copy import copy

"""
All search algorithms.
"""
MAXDEPTH = 2

class Node:
    numberOfNodes = 0
    def __init__(self, board, parent, isMax, depth):
        self.score = None
        self.parent = parent
        self.children = []
        self.depth = depth
        self.isMax = isMax
        self.board = board
        self.score = Node.numberOfNodes
        Node.numberOfNodes += 1
        # print 'Depth with ' + str(self.depth) + ' created'
    def generateChildren(self, listOfValidMoves):
        for move in self.board.getPossibleMoves():
            board = Board()
            self.children.append(Node(board, self, not self.isMax, self.depth+1))
    def evaluateScore(self):
        self.score = board.getBasicHeuristic()
    def returnMinChildScore(self):
        mini = self.children[0].score
        for child in self.children:
            if child.score < mini:
                mini = child.score
        return mini
    def returnMaxChildScore(self):
        maxi = self.children[0].score
        for child in self.children:
            if child.score > maxi:
                maxi = child.score
        return maxi
        
    def getBestMove(self):
        for child in self.children:
            if child.score == self.score:
                for index, agent in enumerate(self.board.agents):
                    if self.board.agents[index].x != child.agents[index].x:
                        src_coordinates = self.board.agents[index].coordinates
                        dst_coordinates = child.agents[index].coordinates
                        break

        return src_coordinates, dst_coordinates


def MiniMax(node):
	"""
	Implementation of the minimax algorithm
	"""
    # print '\nGenerating children...'
    node.generateChildren()
    # print node.children[0].depth

    if node.depth != MAXDEPTH - 1:
        for child in node.children:
            MiniMax(child)
    else:
        for child in node.children:
            child.evaluateScore()
            # print 'Child score is: ' + str(child.score)

    if node.children[0].score:
        if node.isMax:
            node.score = node.returnMaxChildScore()
            # print 'MaxChildScore is ' + str(node.score)
        else:
            node.score = node.returnMinChildScore()
            # print 'MinChildScore is ' + str(node.score)
