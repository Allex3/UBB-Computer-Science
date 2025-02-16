from seminar.group914.seminar_8.board import Board


class Game:
    def __init__(self):
        self.__board = Board()

    def get_board(self) -> Board:
        return self.__board

    def move_human(self, row: int, col: int) -> None:
        """
        Record the human player's move. The human player plays with the 'X'
        :param board: The board
        :param row: The row and column of the move
        :param col:
        """
        # Any exceptions raised in move_board will be raised from this method too
        self.__board.move('X', row, col)
        # move_board(board, 'X', row, col)

    def move_computer(self) -> None:
        if self.__board.is_full():
            raise ValueError('Computer cannot make a move on a full board')

        for row in (0, 1, 2):
            for col in (0, 1, 2):
                if self.__board.get_symbol(row, col) == '':
                    self.__board.move('O', row, col)
                    # TODO Return the move coordinates to show them to the user
                    return
