from texttable import Texttable


class BoardError(Exception):
    """
    BoardError is an exception, so it has to be inherited from an Exception class (Python's Exception)
    """

    def __init__(self, message: str):
        self.__message = message


class Board:
    def __init__(self):
        # self.data is "public" => data is directly accessible from outside the class
        # self.data = [0] * 9

        # self.data is "protected" => data is directly accessible only from inside the class and the classes
        # inherited from Board
        # self._data = [0] * 9

        # self.data is "private" => data is directly accessible only from inside the class
        self.__data = [0] * 9
        self.__move_count = 0

    def move(self, symbol: str, row: int, col: int):
        """
        Make a move on the board
        :param symbol: Either an 'X' or 'O'
        :param row: The row (one of 0, 1 or 2)
        :param col: The col (one of 0, 1 or 2)
        :return: None
        :raises: ValueError In case the move is invalid
        """
        if symbol not in ['X', 'O']:
            raise ValueError("Invalid symbol")
        if row not in (0, 1, 2) or col not in (0, 1, 2):
            raise ValueError(f"Invalid coordinates for move - ({row},{col})")
        if self.__data[3 * row + col] != 0:
            raise BoardError(f"Square already taken - ({row},{col})")
        self.__data[3 * row + col] = 1 if symbol == 'X' else -1
        # increase the move counter only after the move is placed successfully
        self.__move_count += 1

    def get_free_squares(self):
        # TODO Precompute this list when the game starts
        result = []
        for i in range(9):
            if self.__data[i] == 0:
                result.append((i // 3, i % 3))
        return result

    def is_full(self):
        return self.__move_count == 9  # O(1)

    def is_won(self):
        if self.__move_count < 3:
            return False

        d = self.__data
        for row in (0, 3, 6):
            if abs(sum(d[row:row + 3])) == 3:
                return True

        for col in (0, 1, 2):
            if abs(sum(d[col::3])) == 3:  # data[<start_index> : <end_index> : <step>] ->
                # data[:5:2] -> (0,2,4) // data[:-2:2] ->
                return True

        if abs(d[0] + d[4] + d[8]) == 3:
            return True
        if abs(d[2] + d[4] + d[6]) == 3:
            return True
        return False

    def __str__(self) -> str:
        t = Texttable()  # Texttable is a Python class
        d = self.__data  # d is an alias of self.__data

        for row in (0, 3, 6):
            display_row = d[row:row + 3]
            for i in range(3):
                if display_row[i] == 0:
                    display_row[i] = ' '
                elif display_row[i] == 1:
                    display_row[i] = 'X'
                else:
                    display_row[i] = 'O'
            t.add_row(display_row)
        return t.draw()  # draw() converts the Texttable to an str


if __name__ == "__main__":
    board = Board()
    board.move("X", 1, 1)

    Board.move(board, "X", 1, 1)

    try:
        board = Board()
        board.move("X", 1, 1)
        board.move("O", 1, 2)
        print(board)
    except ValueError as ve:
        print(ve)
    except BoardError as be:
        print(be)

    # print(board.data)
    # print(board._data)
    # print(board.__data)
