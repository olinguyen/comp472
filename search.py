from board import Board
from copy import copy
from copy import deepcopy
from agent import *
from util import getValue

"""
All search algorithms.
"""

class Node:
    numberOfNodes = 0
    def __init__(self, agents, parent, isMax, depth, isLarva):
        self.score = None
        self.parent = parent
        self.children = []
        self.depth = depth
        self.isMax = isMax
        self.agents = agents
        self.isLarva = isLarva
        Node.numberOfNodes += 1

    def generateChildren(self):
        if self.isMax:
            agents = [self.agents[0]]
        else:
            agents = self.agents[1:]

        validMoves = self.GetValidMovesForAll(agents)

        if self.isMax:
            for move in validMoves[0]:
                copyAgent = self.agents[:]
                copyAgent[0] = move
                self.children.append(Node(copyAgent, self, not self.isMax, self.depth+1,self.isLarva))
        else:
            for i in range(4):
                for move in validMoves[i]:
                    copyAgent = self.agents[:]
                    copyAgent[i+1] = move
                    self.children.append(Node(copyAgent, self, not self.isMax, self.depth+1,self.isLarva))

    def GetValidMovesForAll(self, agents):
        """ Returns all valid moves for Larva or for each Bird """
        if len(agents) == 1:
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
        # if self.isLarva:
        #     self.score = self.naiveHeuristic()
        # else:
        #     self.score = self.masterHeuristic()
        self.score = self.masterHeuristic()

    def naiveHeuristic(self):
        value = 0
        for i, agent in enumerate(self.agents):
            x, y = agent[0], agent[1]
            if i == 0:
                value += getValue(x, y)
            else:
                value -= getValue(x, y)
        return value

    def maxPositionHeuristic(self):
        value = 0
        x = self.agents[0][0]
        y = self.agents[0][1]
        if not [x - 1, y + 1] in self.agents and 0 <= x - 1 <= 7 and  0 <= y + 1 <= 7:
            value += 10
        if not [x - 1, y - 1] in self.agents and 0 <= x - 1 <= 7 and  0 <= y - 1 <= 7:
            value += 10
        if not [x + 1, y + 1] in self.agents and 0 <= x + 1 <= 7 and  0 <= y + 1 <= 7:
            value += 10
        if not [x + 1, y - 1] in self.agents and 0 <= x + 1 <= 7 and  0 <= y - 1 <= 7:
            value += 10
        return value

    def smallestDistanceHeuristic(self):
        return self.agents[0][0]

    def masterHeuristic(self):
        xlarva = self.agents[0][0]
        ylarva = self.agents[0][1]
        xBirds = []
        w1 = 1
        w2 = 3
        w3 = 1
        # Keep all birds above larva
        v1 = 0
        for i in range(1, len(self.agents) - 1):
            v1 += xlarva - self.agents[i][0]
            xBirds.append(self.agents[i][0])
        # big variance on x axis beneficial for larva
        v2 = self.calculateVariance(xBirds)
        # Larva is as close as possible to rank 1
        v3 = xlarva
        # print v1, v2, v3
        return w1*v1 + w2*v2 + w2*v3

    def calculateVariance(self, values):
        # Find mean
        count = len(values)
        mean = sum(values)/float(count)
        # Compute variance
        variance = 0.0
        for x in values:
            variance += (x - mean) * (x - mean)
        variance = variance / float(count)
        return variance

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
        childNumber = 1
        for child in self.children:
            """
            print "For child ", childNumber, ": "
            print self.agents
            print child.agents
            print
            """
            childNumber += 1
            if child.score == self.score:
                for i in range(5):
                    if self.agents[i] != child.agents[i]:
                        src_coordinates = Coordinates(self.agents[i][0], self.agents[i][1])
                        dst_coordinates = Coordinates(child.agents[i][0], child.agents[i][1])
                        return src_coordinates, dst_coordinates
        raise Exception("Children with appropriate score not found")

    def allChildrenScored(self):
        for child in self.children:
            if not child.score:
                return False
        return True

    def getUnofficialNodeScore(self):
        return self.masterHeuristic()


def MiniMax(node, maxDepth):
    """
    Implementation of the minimax algorithm
    """
    node.generateChildren()

    if not node.children:
        node.evaluateScore()
        return

    if node.depth != maxDepth - 1:
        for child in node.children:
            MiniMax(child)
    else:
        for child in node.children:
            child.evaluateScore()

    if node.children and node.allChildrenScored():
        if node.isMax:
            node.score = node.returnMaxChildScore()
        else:
            node.score = node.returnMinChildScore()
    else:
        node.score = node.evaluateScore()

def AlphaBetaPruning(node, depth, alpha, beta, maxDepth):

    if node.agents[0][0] == 7:
        node.score = 999999 - node.depth
        return node.score

    if depth == maxDepth:
        node.evaluateScore()
        return node.score

    node.generateChildren()
    children = node.children

    if not children:
        node.evaluateScore()
        return node.score

    children.sort( key=lambda x: x.getUnofficialNodeScore(), reverse=node.isMax)

    if node.isMax:
        value = -999999
        for child in children:
            value = max(value, AlphaBetaPruning(child, depth + 1, alpha, beta, maxDepth))
            beta = max(value, beta)
            if beta >= alpha:
                break
        node.score = value
        return value
    else:
        value = 999999
        for child in children:
            value = min(value, AlphaBetaPruning(child, depth + 1, alpha, beta, maxDepth))
            alpha = min(value, alpha)
            if beta >= alpha:
                break
        node.score = value
        return value
