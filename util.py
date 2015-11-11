"""
Useful data structures for implementing search algorithms.
"""
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ConvertToIndex(stringCoodinates):
    """For converting coordinate notation into array index."""
    stringCoodinates = stringCoodinates.lower()
    if not(97 <= ord(stringCoodinates[0]) <= 104 \
    and 1 <= int(stringCoodinates[1]) <= 8):
        raise Exception("Out of Bounds")
    y = ord(stringCoodinates[0]) - 97
    x = 7 - (int(stringCoodinates[1]) - 1)
    return Coordinates(x, y)

def getValue(x, y):
    """
    Returns the value for a given position
    """
    return (y + 1) + (8 * x)
