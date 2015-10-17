"""
Useful data structures for implementing search algorithms.
"""
import game

def ConvertToIndex(stringCoodinates):
    """For converting coordinate notation into array index."""
    stringCoodinates.lower()
    if not(97 <= ord(stringCoodinates[0]) <= 104 \
    and 1 <= int(stringCoodinates[1]) <= 8):
        raise Exception("Out of Bounds")
    x = ord(stringCoodinates[0]) - 97
    y = 7 - (int(stringCoodinates[1]) - 1)
    return game.Coordinates(x, y)
