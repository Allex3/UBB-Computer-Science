from texttable import Texttable

class Board:
    def __init__(self):
        self.__board = [0] * 9

    def __str__(self):
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
                cell = self.__board[3 * i + j]
                if cell == 1:
                    row.append('X')
                elif cell == -1:
                    row.append('O')
                else:
                    row.append(' ')
            formattedTable.append(row)

        table.add_rows(formattedTable, header=False)
        return table.draw()

    def getBoardValue(self, x: int, y: int) -> int:
        """
        Gets the value from the board for the requested position
        :param board: the given board
        :param x: the row
        :param y: the column
        :return: an integer, the requested value
        """
        if x not in (0, 1, 2) or y not in (0, 1, 2):
            raise ValueError("Position is not on the board")

        return self.__board[3 * x + y]

    def moveBoard(self, x: int, y: int, symbol: str):
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
        if self.getBoardValue(x, y) != 0:
            raise ValueError("The cell is already completed")
        if symbol.upper() == 'X':
            self.__board[3 * x + y] = 1
        else:
            self.__board[3 * x + y] = -1

    def isBoardWon(self):
        # check the rows
        for i in range(0, 9, 3):
            if abs(sum(self.__board[i:i + 3])) == 3:
                return True

        # check the columns
        for i in range(3):
            if abs(sum(self.__board[i::3])) == 3:
                return True

        # check the diagonals
        if abs(self.__board[0] + self.__board[4] + self.__board[8]) == 3:
            return True
        if abs(self.__board[2] + self.__board[4] + self.__board[6]) == 3:
            return True

        return False

    def isBoardDraw(self):
        found = True

        for i in range(9):
            if self.__board[i] == 0:
                found = False
                break

        return found

    """
    def __init__(self):
        self.i = 0
        self.__j = 0
        print("Hi there " + str(self.i))
        self.i += 1

    def getPrivateMember(self):
        return self.__j

    def setPrivateMember(self, newValue):
        self.__j = newValue
    """

if __name__=="__main__":
    """
    board = Board()
    print(board.i)
    print(board.getPrivateMember())
    board.setPrivateMember(199)
    print(board.getPrivateMember())
    print(board.i)
    board1 = Board()
    board2 = Board()
    board3 = Board()
    """
    board = Board()
    print(board)