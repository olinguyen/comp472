"""
Useful data structures for implementing search algorithms.
"""

import game

# def CoorToIndex(coordinates):
#     """For converting coordinate notation into array index."""
#     rowSize = 8
#     coordinates.lower()
#     if not(97 <= ord(coordinates[0]) <= 104 \
#     and 1 <= int(coordinates[1]) <= 8):
#         raise Exception("Out of Bounds")
#     rankNumber = int(coordinates[1]) - 1
#     fileLetterValue = ord(coordinates[0]) - 97
#     return rowSize * rankNumber + fileLetterValue

def ConvertToIndex(stringCoodinates):
    """For converting coordinate notation into array index."""
    stringCoodinates.lower()
    if not(97 <= ord(stringCoodinates[0]) <= 104 \
    and 1 <= int(stringCoodinates[1]) <= 8):
        raise Exception("Out of Bounds")
    x = ord(stringCoodinates[0]) - 97
    y = 7 - (int(stringCoodinates[1]) - 1)
    return game.Coordinates(x, y)
