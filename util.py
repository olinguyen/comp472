"""
Useful data structures for implementing search algorithms.
"""

def CoorToIndex(coordinates):
    """For converting coordinate notation into array index."""
    rowSize = 8
    coordinates.lower()
    print coordinates[0] + " " + str(ord(coordinates[0]))
    if not(97 <= ord(coordinates[0]) <= 104 \
    and 1 <= int(coordinates[1]) <= 8):
        raise Exception("Out of Bounds")
    rankNumber = int(coordinates[1]) - 1
    fileLetterValue = ord(coordinates[0]) - 97
    return rowSize * rankNumber + fileLetterValue
