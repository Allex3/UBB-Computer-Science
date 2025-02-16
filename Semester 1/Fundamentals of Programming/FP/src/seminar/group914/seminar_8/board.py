from texttable import Texttable


class BoardError(Exception):
    """
    Class BoardError is a Python Exception, because it is inherited from Exception
    "inherited" = it has the same fiedls and methods, and behaves the same way
    """

    def __init__(self, message: str):
        self.__message = message


class Board:
    def __init__(self):
        # self.data means that data attribute is "public"
        # self.data = [0] * 9  # 3 x 3 board represented as a list

        # self._data means that data attribute is "protected"
        # "protected" - it should be changed only from inside the class or
        # from derived classes !?
        # protected is not enforced in Python, but it is in many other
        # languages
        # self._data = [0] * 9

        # self.__data means that data attribute is "private"
        # "private" - it can be changed only from inside the class
        self.__data = [0] * 9

        # count the number of valid moves on the board
        self.__move_count = 0

    def get_symbol(self, x: int, y: int) -> str:
        """
        Get the symbol at coordinates (x, y)
        :param board:The board
        :return: 'X' or 'O', or '' if the square has not been played yet
        """
        # return 'X' if board[x][y] == 1 else 'O' if board[x][y] == -1 else ''

        if self.__data[3 * x + y] == 1:
            return 'X'
        elif self.__data[3 * x + y] == -1:
            return 'O'
        return ''

    def move(self, symbol: str, x: int, y: int) -> None:
        """
        Record a move on the board
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
        if self.get_symbol(x, y) != '':
            raise BoardError(f'Cannot overwrite board position {x},{y}')
        self.__data[3 * x + y] = 1 if symbol == 'X' else -1
        self.__move_count += 1

    def is_full(self) -> bool:
        """
        Check that the board is full
        :param board: The board
        :return: True if and only if the board is full
        """
        return self.__move_count == 9

    def is_won(self) -> bool:
        """
        Check that the board is won
        :param board: The board
        :return: True if and only if the board is won
        """
        d = self.__data  # these have the same address & values
        for row in (0, 1, 2):
            if abs(sum(d[3 * row:3 * row + 3])) == 3:
                return True
        for col in (0, 1, 2):
            if abs(sum(d[col::3])) == 3:  # data[<begin> : <end> : <step>]  
                return True
        if abs(d[0] + d[4] + d[8]) == 3:
            return True
        if abs(d[2] + d[4] + d[6]) == 3:
            return True
        return False

    def __str__(self) -> str:  # you have to obey the signature of predefined methods
        """
        Represent the board as a string
        :param board: The board
        :return: The str representation of the board
        """
        t = Texttable()  # Texttable is a Python class
        for i in (0, 1, 2):
            # current_row = board[i][:]  # create a copy of the current row
            current_row = self.__data[3 * i:3 * i + 3]

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
    # my_other_list = list()  # call Python list class constructor
    # my_other_list.clear()  # call clear() method on Python list

    # board_one is a variable of type Board
    # it has an attribute variable named data of type list
    board_one = Board()  # this calls Board.__init__

    # board_two is another variable of type Board
    # it has its own attribute variable named data of type list
    board_two = Board()

    # board_one.data and board_two.data are different variables
    # board_one.data is self.data, but the interpreter sets self as board_one

    # board_one.__data[6] = 10  # this might not be a good idea !?
    # print(board_one.__data)
    # print(board_two.data)
    # print(dir(board_one))

    # the following two lines are <=>
    # board_one.move("X", 1, 2)
    # Board.move_board(board_one, "X", 1, 2)

    try:
        board_one.move("X", 1, 1)
        board_one.move("O", 1, 2)
        print(str(board_one))  # this is the Python way to print out an object
    except ValueError as ve:
        print(ve)
    except BoardError as be:
        print(be)
