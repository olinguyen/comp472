from board import Board
from copy import copy
from copy import deepcopy
from agent import *
from util import getValue

"""
All search algorithms.
"""
MAXDEPTH = 6

class Node:
    numberOfNodes = 0
    def __init__(self, agents, parent, isMax, depth):
        self.score = None
        self.parent = parent
        self.children = []
        self.depth = depth
        self.isMax = isMax
        self.agents = agents
        Node.numberOfNodes += 1
        # print 'Depth with ' + str(self.depth) + ' created'
    def generateChildren(self):
        if self.isMax:
            agents = [self.agents[0]]
        else:
            agents = self.agents[1:]

        # For each agent get all their valid moves
        validMoves = self.GetValidMovesForAll(agents)

        if self.depth == 0:
            print validMoves

        # Create children based on valid moves
        if self.isMax:
            for move in validMoves[0]:
                copyAgent = self.agents[:]
                copyAgent[0] = move
                self.children.append(Node(copyAgent, self, not self.isMax, self.depth+1))
        else:
            for i in range(4):
                for move in validMoves[i]:
                    if self.depth == 0:
                        print move
                    copyAgent = self.agents[:]
                    copyAgent[i+1] = move
                    if not move:
                        print "noob mistake"
                    self.children.append(Node(copyAgent, self, not self.isMax, self.depth+1))

        #
        # for index in range(0,len(agents),2):
        #     for move in self.(agent):
        #         # board = deepcopy(self.board)
        #         board = Board()
        #         # board.agents = map(copy, self.board.agents)
        #         # board.agents = self.board.agents[:]
        #         if self.isMax:
        #             board.agents[i].move(move)
        #         else:
        #             board.agents[i+1].move(move)
        #         self.children.append(Node(board, self, not self.isMax, self.depth+1))

    def GetValidMovesForAll(self, agents):
        """ Returns all valid moves for Larva or for each Bird """
        # return list of lists containing valid moves for each agent
        if len(agents) == 1:
            # generate and return possible valid moves for larva
            moves = []
            x = agents[0][0]
            y = agents[0][1]
            if not [x - 1, y + 1] in self.agents and 0 <= x - 1 <= 7 and  0 <= y + 1 <= 7:
                moves.append([x - 1, y + 1])
            if not [x - 1, y - 1] in self.agents and 0 <= x - 1 <= 7 and  0 <= y - 1 <= 7:
                moves.append([x - 1, y - 1])
            if not [x + 1, y + 1] in self.agents and 0 <= x + 1 <= 7 and  0 <= y + 1 <= 7:
                moves.append([x + 1, y + 1])
            if not [x + 1, y - 1] in self.agents and 0 <= x + 1 <= 7 and  0 <= y - 1 <= 7:
                moves.append([x + 1, y - 1])
            return [moves]
        else:
            totalMoves = []
            for i in range(4):
                moves = []
                x = agents[i][0]
                y = agents[i][1]
                if not [x - 1, y + 1] in self.agents and 0 <= x - 1 <= 7 and  0 <= y + 1 <= 7:
                    moves.append([x - 1, y + 1])
                if not [x - 1, y - 1] in self.agents and 0 <= x - 1 <= 7 and  0 <= y - 1 <= 7:
                    moves.append([x - 1, y - 1])
                totalMoves.append(moves)
            return totalMoves
        raise Exception("Invalid execution!!!")

    def evaluateScore(self):
        self.score = self.naiveHeuristic()

    def naiveHeuristic(self):
        value = 0
        for i, agent in enumerate(self.agents):
            x, y = agent[0], agent[1]
            if i == 0:
                value += getValue(x, y)
            else:
                value -= getValue(x, y)
        return value

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
        # print [child.agents for child in self.children]
        childNumber = 1
        for child in self.children:
            print "For child ", childNumber, ": "
            print self.agents
            print child.agents
            childNumber+=1
            print
            if child.score == self.score:
                for i in range(5):
                    if self.agents[i] != child.agents[i]:
                        src_coordinates = Coordinates(self.agents[i][0], self.agents[i][1])
                        dst_coordinates = Coordinates(child.agents[i][0], child.agents[i][1])
                        return src_coordinates, dst_coordinates
                # for index, agent in enumerate(self.board.agents):
                #     if self.board.agents[index].coordinates.x \
                #             != child.board.agents[index].coordinates.x:
                #         src_coordinates = self.board.agents[index].coordinates
                #         dst_coordinates = child.board.agents[index].coordinates
                #         break
        raise Exception("Children with appropriate score not found")

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

    if node.children and node.children[0].score:
        if node.isMax:
            node.score = node.returnMaxChildScore()
            # print 'MaxChildScore is ' + str(node.score)
        else:
            node.score = node.returnMinChildScore()
            # print 'MinChildScore is ' + str(node.score)
    else:
        node.score = node.evaluateScore()

    # print "Depth: ", node.depth, ", Score: ", node.score

def AlphaBetaPruning(node, depth, alpha, beta):

    if depth == MAXDEPTH:
        node.evaluateScore()
        # print "Depth = ", depth, "Score = ", node.score
        return node.score

    node.generateChildren()
    children = node.children

    if not children:
        node.evaluateScore()
        return node.score

    if node.isMax:
        value = -999999
        for child in children:
            value = max(value, AlphaBetaPruning(child, depth + 1, alpha, beta))
            beta = max(value, beta)
            if beta >= alpha:
                break
        node.score = value
        return value
    else:
        value = 999999
        for child in children:
            value = min(value, AlphaBetaPruning(child, depth + 1, alpha, beta))
            alpha = min(value, alpha)
            if beta >= alpha:
                break
        node.score = value
        return value
