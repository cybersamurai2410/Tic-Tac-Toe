"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    Xnum = 0
    Onum = 0

    for row in board:
        Xnum += row.count(X)
        Onum += row.count(O)

    if Xnum > Onum:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action = set()
    board_len = len(board)

    for row in range(board_len):
        for col in range(board_len):
            if board[row][col] == EMPTY:
                action.add((row, col))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_result = deepcopy(board)
    (i, j) = action

    if board[i][j] is not EMPTY:
        raise Exception("Position already taken")
    else:
        board_result[i][j] = player(board)

    return board_result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for m in [X, O]:

        # Horizontal
        for row in board:
            if row == [m] * 3:
                return m

        # Vertical
        for col in range(len(board)):
            column = []
            for row in range(len(board)):
                column.append(board[row][col])
            if column == [m] * 3:
                return m

        # Diagonal
        if [board[index][index] for index in range(len(board))] == [m] * 3 \
                or [board[index][~index] for index in range(len(board))] == [m] * 3:
            return m

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for index in board:
        if EMPTY in index:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        val = -math.inf

        for action in actions(board):
            maxVal = minValue(result(board, action))
            if maxVal > val:
                val = maxVal
                optimumVal = action

    if player(board) == O:
        val = math.inf

        for action in actions(board):
            minVal = maxValue(result(board, action))
            if minVal < val:
                val = minVal
                optimumVal = action

    return optimumVal


def minValue(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v

def maxValue(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v
