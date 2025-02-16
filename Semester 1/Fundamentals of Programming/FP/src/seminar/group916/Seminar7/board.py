"""
Board:
0 0 0
0 0 0
0 0 0

0 1 2
3 4 5
6 7 8


Representation: a list of length 9
0 - the cell is empty
1 - the cell contains a 'X'
-1 - the cell contains a 'O'
"""
from texttable import Texttable


def createBoard():
    return [0] * 9

def getBoardValue(board, x: int, y: int) -> int:
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Position is not on the board")

    return board[3 * x + y]

def toString(board) -> str:
    """
    Represents the board as a 3x3 grid using Texttables
    :param board: the board
    :return: the required string representation
    """

    table = Texttable()
    table.set_cols_align(["c", "c", "c"])

    formattedTable = []
    for i in range(3):
        row = []
        for j in range(3):
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

def moveBoard(board, x: int, y: int, symbol: str):
    """
    Makes a move on the board
    :param board: the given board
    :param x: the row on which we want to make the move
    :param y: the column on which we want to make the move
    :param symbol: the symbol we want to place at position (x, y) - should be either 'X' or 'O'
    :return: None
    """

    if symbol.upper() not in ['X', 'O']:
        raise ValueError("Symbol should be X or O")
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Position is not on the board")
    if getBoardValue(board, x, y) != 0:
        raise ValueError("Invalid position. We already have something there")

    if symbol.upper() == 'X':
        board[3 * x + y] = 1
    else:
        board[3 * x + y] = -1

def isBoardWon(board) -> bool:
    """
    Verifies if the board has been won
    :param board:
    :return:
    """

    #check the rows
    for i in range(0, 9, 3): # 0, 3, 6
        if abs(sum(board[i:i+3])) == 3:
            return True

    #check the columns
    for i in range(3):
        if abs(sum(board[i::3])) == 3:
            return True

    #check the diagonals
    if abs(board[0] + board[4] + board[8]) == 3:
        return True
    if abs(board[2] + board[4] + board[6]) == 3:
        return True

    return False


def isBoardDraw(board) -> bool:
    found = True
    for i in range(9):
        if board[i] == 0:
            found = False
            break

    return found

if __name__=="__main__":
    board = createBoard()
    print(toString(board))