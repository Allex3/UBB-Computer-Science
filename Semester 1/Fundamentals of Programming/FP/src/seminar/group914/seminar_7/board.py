from texttable import Texttable
from pdoc import pdoc


def create_board() -> list:
    """
    Create an empty Tic Tac Toe board
    :return: The board representation
    """
    b = []
    for row in range(0, 3):
        b.append([0, 0, 0])
    return b


def move_board(board, symbol: str, x: int, y: int) -> None:
    """
    Record a move on the given board
    :param board: The board
    :param symbol: The move. Must be one of 'X' or 'O'
    :param x: The row (integer between 0 and 2)
    :param y: The column (integer between 0 and 2)
    :raises ValueError: If the board is invalid (move is not 'X' or 'O', move is outside the board or would overwrite a
    previous move)
    :return:
    """
    if symbol not in ['X', 'O']:
        raise ValueError(f'Invalid move symbol {symbol}')
    if x not in (0, 1, 2) or y not in (0, 1, 2):
        raise ValueError(f'Invalid move x {x} and y {y}')
    if get_symbol_board(board, x, y) != '':
        raise ValueError(f'Cannot overwrite board position {x},{y}')
    board[x][y] = 1 if symbol == 'X' else -1


def is_won_board(board: list) -> bool:
    """
    Check that the board is won
    :param board: The board
    :return: True if and only if the board is won
    """
    for row in (0, 1, 2):
        if abs(sum(board[row])) == 3:
            return True
    for col in (0, 1, 2):
        if abs(board[0][col] + board[1][col] + board[2][col]) == 3:
            return True

    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return True
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return True


def is_full_board(board: list) -> bool:
    """
    Check that the board is full
    :param board: The board
    :return: True if and only if the board is full
    """
    for row in range(0, 3):
        for col in range(0, 3):
            if get_symbol_board(board, row, col) == '':
                return False
    # TODO Increment a counter when a move is made and check its value => O(1)
    return True


def get_symbol_board(board: list, x: int, y: int) -> str:
    """
    Get the symbol at coordinates (x, y)
    :param board:The board
    :return: 'X' or 'O', or '' if the square has not been played yet
    """
    # return 'X' if board[x][y] == 1 else 'O' if board[x][y] == -1 else ''

    if board[x][y] == 1:
        return 'X'
    elif board[x][y] == -1:
        return 'O'
    return ''


def to_str(board: list) -> str:
    """
    Represent the board as a string
    :param board: The board
    :return: The str representation of the board
    """
    t = Texttable()  # Texttable is a Python class
    for i in (0, 1, 2):
        current_row = board[i][:]  # create a copy of the current row

        for col in range(0, 3):
            if current_row[col] == -1:
                current_row[col] = 'O'
            elif current_row[col] == 1:
                current_row[col] = 'X'
            else:
                current_row[col] = ' '
        t.add_row(current_row)
    return t.draw()


if __name__ == '__main__':
    """
    To generate HTML documentation for this module
    """
    f = open("doc.html", "wt")
    f.write(pdoc("board.py", ""))
    f.close()

    # board = create_board()
    # print(to_str(board))
    # move_board(board, 'X', 1, 1)
    # move_board(board, 'O', 0, 1)
    # move_board(board, 'X', 2, 2)
    # print(to_str(board))
