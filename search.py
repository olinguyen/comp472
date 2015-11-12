"""
All search algorithms.
"""
MAXDEPTH = 2

class Node:
    numberOfNodes = 0
    def __init__(self, parent, isMax, depth):
        self.score = None
        self.parent = parent
        self.children = []
        self.depth = depth
        self.isMax = isMax
        Node.numberOfNodes += 1
        print 'Depth with ' + str(self.depth) + ' created'
        self.score = Node.numberOfNodes
    def generateChildren(self):
        self.children.append(Node(self, not self.isMax, self.depth + 1))
        self.children.append(Node(self, not self.isMax, self.depth + 1))
    def evaluateScore(self):
        #self.score = Node.numberOfNodes
        return
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

def MiniMax(node):
	"""
	Implementation of the minimax algorithm
	"""
    print '\nGenerating children...'
    node.generateChildren()
    print node.children[0].depth

    if node.depth != MAXDEPTH - 1:
        for child in node.children:
            MiniMax(child)
    else:
        for child in node.children:
            child.evaluateScore()
            print 'Child score is: ' + str(child.score)

    if node.children[0].score:
        if node.isMax:
            node.score = node.returnMaxChildScore()
            print 'MaxChildScore is ' + str(node.score)
        else:
            node.score = node.returnMinChildScore()
            print 'MinChildScore is ' + str(node.score)

    return
