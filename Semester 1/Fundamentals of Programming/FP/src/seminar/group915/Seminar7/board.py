# Board will a list of size 9
# 0 - the cell is empty
# -1 - the cell contains an 'O'
# 1 - the cell contains 'X'

""""
x = 1
y = 1

0 0 0
0 0 0
0 0 0
"""
from texttable import Texttable

def createBoard():
    """
    Creates an empty board
    :return: The new board
    """
    return [0] * 9

def getBoard(board, x : int, y : int) -> int:
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Position is outside the board")
    return board[3 * x + y]

def moveBoard(board, x: int, y: int, symbol: str):
    """
    Move item on board
    :param board: the board
    :param x: the row on which we want to place the current element
    :param y: the column on which we want to place the current element
    :param symbol: The current element, either 'X' or 'O'
    :return: None
    """
    if symbol.upper() not in ['X', 'O']:
        raise ValueError("Invalid symbol")
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Position is outside the board")
    if getBoard(board, x, y) != 0:
        raise ValueError("Position is already occupied")
    if symbol.upper() == "X":
        board[3 * x + y] = 1
    else:
        board[3 * x + y] = -1


def toString(board) -> str:
    """
    Represent the board as a 3x3 grid using Texttable
    :param board: The board
    :return: The string representation of the board
    """

    table = Texttable()
    table.set_cols_align(["c", "c", "c"])

    formattedTable = []
    for i in range(3):
        row = []
        for j in range (3):
            cell = board[3 * i + j]
            if cell == -1:
                row.append('O')
            elif cell == 1:
                row.append('X')
            else:
                row.append(' ')
        formattedTable.append(row)

    table.add_rows(formattedTable, header=False)
    return table.draw()

#Mintar Dinu Dragos
def isBoardWon(board) -> bool:
    for x in range (0, 3):
        s = 0
        for y in range (0, 3):
            s += getBoard(board, x, y)
        if abs(s) == 3:
            return True

    for i in range(0, 3):
        if abs(sum(board[i::3])) == 3:
            return True
    """
    for y in range (0, 3):
        s = 0
        for x in range (0, 3):
            s += getBoard(board, y, x)
        if abs(s) == 3:
            return True
    """

    if abs(board[0] + board[4] + board[8]) == 3:
        return True

    if abs(board[2] + board[4] + board[6]) == 3:
        return True

    return False


def isBoardDraw(board):
    found = True
    for i in range(9):
        if board[i] == 0:
            found = False
            break

    return found


if __name__=="__main__":
    board = createBoard()
    print(toString(board))
