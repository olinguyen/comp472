"""
The logic behind how the Hungry Birds world works.
TODO: Create board class?
"""

def create_board():
    N = 8;
    board = []

    for i in range(N):
        board_row = []
        for j in range(N):
            board_row.append(' ')
        board.append(board_row)
    return board
