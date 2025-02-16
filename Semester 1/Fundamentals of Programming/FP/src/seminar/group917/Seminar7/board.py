"""
Board
- - -
- - -
- - -

0 1 2
2 4 5
6 7 8

List representation: list of length 9
0 - the cell is empty
1 - the cell contains a 'X'
-1 - the cell contains an 'O'
"""
from texttable import Texttable


def createBoard():
    return [0] * 9

def getBoardValue(board, x: int, y: int) -> int:
    """
    Gets the value from the board for the requested position
    :param board: the given board
    :param x: the row
    :param y: the column
    :return: an integer, the requested value
    """
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Position is not on the board")

    return board[3 * x + y]

def toString(board):
    """
    Represent the board as a string using Texttable
    :param board: the given board
    :return: the string representation of the board
    """

    table = Texttable()
    table.set_cols_align(["c", "c", "c"])

    formattedTable = []
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[3 * i + j]
            if cell == 1:
                row.append('X')
            elif cell == -1:
                row.append('O')
            else:
                row.append(' ')
        formattedTable.append(row)

    table.add_rows(formattedTable, header=False)
    return table.draw()

def moveBoard(board, x: int, y: int, symbol: str):
    """
    Makes a move on the board at the required position
    :param board: the given board
    :param x: the row on which we want to place the new item
    :param y: the column on which we want to place the new item
    :param symbol: the new item, either X or O
    :return: None
    :raises ValueError when: Symbol is not X or O
                             Position is not on the board
                             The requested cell is not empty
    """
    if symbol.upper() not in ['X', 'O']:
        raise ValueError("Symbol should be X or O")
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError("Position is not on the board")
    if getBoardValue(board, x, y) != 0:
        raise ValueError("The cell is already completed")
    if symbol.upper() == 'X':
        board[3 * x + y] = 1
    else:
        board[3 * x + y] = -1

def isBoardWon(board):
    # check the rows
    for i in range(0, 9, 3):
        if abs(sum(board[i:i+3])) == 3:
            return True

    # check the columns
    for i in range(3):
        if abs(sum(board[i::3])) == 3:
            return True

    # check the diagonals
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