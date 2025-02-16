from seminar.group914.seminar_7.board import move_board, get_symbol_board, is_full_board


def move_human(board, row: int, col: int) -> None:
    """
    Record the human player's move. The human player plays with the 'X'
    :param board: The board
    :param row: The row and column of the move
    :param col:
    """
    # Any exceptions raised in move_board will be raised from this method too
    move_board(board, 'X', row, col)


def move_computer(board) -> None:
    if is_full_board(board):
        raise ValueError('Computer cannot make a move on a full board')

    for row in (0, 1, 2):
        for col in (0, 1, 2):
            if get_symbol_board(board, row, col) == '':
                move_board(board, 'O', row, col)
                # TODO Return the move coordinates to show them to the user
                return
