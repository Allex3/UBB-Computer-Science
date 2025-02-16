from copy import deepcopy
from termcolor import colored
from texttable import Texttable


class DiscException(Exception):
    pass


class GridException(Exception):
    pass


class DiscsGrid:
    """
    Class storing the Grid with discs where the game will be played
    Uses bitboards for computation but arrays also for string formatting and storing the last disc on a column
    Functions:
        - A set of functions to check the win (row/column/diagonal, checking the win with all of these)
        - A set of functions to place and remove the disc and update the bitboards accordingly
        - A set of functions used in scoring a given positions: counting the discs, checking if the game is over (board is full/won)
        - A function to convert the grid to string format for the console application
    """

    def __init__(self):
        """
        Initialize the grid you play on
        A disc is 1 for player 1, 2 for player 2
        0 if there is no disc there on the grid
        6 rows, 7 columns grid
        """
        self.__data = []
        for i in range(6):
            self.__data.append([0] * 7)
        self.__last_disc_placed_row = [5] * 7  # row of a given column (0-6) of the last disc added
        # The disks are added from the 5th row to the 0 row.
        self.current_turn = True
        self.__COLUMNS = 7
        self.__ROWS = 6
        self.__bitboard = (1 | (1 << 7) | (1 << 14) | (1 << 21) | (1 << 28) | (1 << 35) | (
                    1 << 42))  # First row in bitboard is 1
        # The above bitboard has 1 for p1, 0 for p2, and the intermediary 1's to make it unique - it is used for identification of position.
        # The below bitboards only contain 1's on disc representing player 1 or player 2 to compute the wins
        self.__bitboard1 = 0  # Bitboard for player 1
        self.__bitboard2 = 0 # Bitboard for player 2

    def place_disc(self, column, disc: bool) -> None:
        """
        Place a disc on the bottom free row of a column.
        :param column: The column we place the disc on
        :param disc: The player who places the disc (1 = True, 2 = False)
        :return: None
        """
        if not (1 <= column <= 7):
            raise GridException("Invalid column to place disk in, columns are from 1 to 7")

        if self.__last_disc_placed_row[column - 1] == -1:
            raise DiscException("Last disk is already placed on this column.")

        if disc:
            self.__data[self.__last_disc_placed_row[column - 1]][column - 1] = 1
        else:
            self.__data[self.__last_disc_placed_row[column - 1]][column - 1] = 2

        self.__last_disc_placed_row[column - 1] -= 1

        self.__update_bitboard(column - 1, disc)

    def __update_bitboard(self, column: int, player: bool) -> None:
        """
        Function to update the bitboard of the grid when a disc is placed in a column
        :param column: The column the disc is placed in
        :param player: The player for which the disc is placed (True = 1, False = 2)
        :return: None
        """
        self.__bitboard = self.__bitboard ^ (
                1 << (column * 7 + 5 - (self.__last_disc_placed_row[column] + 1)))
        # Remove the 1 that represents the 1 above the last placed disc, which is on the bottom row now
        if player:
            self.__bitboard = self.__bitboard | (
                    1 << (column * 7 + 5 - (self.__last_disc_placed_row[column] + 1)))
            self.__bitboard1 = self.__bitboard1 | (
                    1 << (column * 7 + 5 - (self.__last_disc_placed_row[column] + 1)))
        if not player:  # Put 1 in bitboard for player 2
            self.__bitboard2 = self.__bitboard2 | (
                    1 << (column * 7 + 5 - (self.__last_disc_placed_row[column] + 1)))

        self.__bitboard = self.__bitboard | (1 << (column * 7 + 5 - (self.__last_disc_placed_row[column])))
        # Setting to 1 the bit where we placed the disc (column, row) if player is 1 in the bitmask
        # Setting to 1 the bit above the last disc placed on the column, which is in (self.__last_disc_placed_row[column - 1])
        # If player is 2 it remains 0 as if it was empty, but put a 1 above it

    def __check_column_win(self) -> int:
        """
        Checks if there are 4 discs connected on any column
        :return: The winner's number (1 or 2) or 0 if no one won yet.
        """
        # Since we have a bitboard, a vertical win (column) can be checked like this:
        # bits 0-5 are the first column, 7-12 the second and so on, so adjacent bits are column
        # If we have for example bits 1 2 3 4 to be 1 for the bitboard of p1, they win, or p2
        # And we check this with bitshift right operations, checking if 1 2 3 4 overlap
        # So bring the bit 2 to the right, overlapping with 1, then 3 overlapping with them, then 4
        # If all 4 bits are 1, then the result of the AND of those will be 1, atleast on ONE column

        if self.__bitboard1 & (self.__bitboard1 >> 1) & (self.__bitboard1 >> 2) & (self.__bitboard1 >> 3) > 0:
            return 1  # Player 1 won
        if self.__bitboard2 & (self.__bitboard2 >> 1) & (self.__bitboard2 >> 2) & (self.__bitboard2 >> 3) > 0:
            return 2  # Player 2 won

        return 0  # No one won

    def __check_row_win(self) -> int:
        """
        Checks if there are 4 discs connected on any row
        :return: The winner's number (1 or 2) or 0 if no one won yet.
        """
        # The horizontal (row) win should be the same, just that a disc adjacent in a row is on the same row but next column
        # So it will be on the +7 bit of the bitmask by how we defined it, then +14 then +21
        # This will shift ALL columns to the right checking if there is any overlap on any row of 4 adjacent bits.
        if self.__bitboard1 & (self.__bitboard1 >> 7) & (self.__bitboard1 >> 14) & (self.__bitboard1 >> 21) > 0:
            return 1  # Player 1 won
        if self.__bitboard2 & (self.__bitboard2 >> 7) & (self.__bitboard2 >> 14) & (self.__bitboard2 >> 21) > 0:
            return 2  # Player 2 won

        return 0  # No one won

    def __check_main_diagonal_win(self) -> int:
        """
        Check if 4 discs are connected on a main diagonal-like line
        Example:
        # . .
        . # .
        . . #
        or
        . . .
        # . .
        . # .
        or
        . # .
        . . #
        . . .
        :return: The winner's number (1 or 2) or 0 if no one won yet
        """
        # For the main diagonal win, we check the current bit and the bit that is adjacent on the same row but down one column, on ANY row or column this happens
        # So +7 to get to the adjacent column on the same row, then -1 to go DOWN one row, i+1 and j+1 basically
        # Because the rows are going from bottom to up in bits, so -1 is actually going down, not up

        if self.__bitboard1 & (self.__bitboard1 >> 6) & (self.__bitboard1 >> 12) & (self.__bitboard1 >> 18) > 0:
            return 1  # Player 1 won
        if self.__bitboard2 & (self.__bitboard2 >> 6) & (self.__bitboard2 >> 12) & (self.__bitboard2 >> 18) > 0:
            return 2  # Player 2 won

        return 0  # No one won

    def __check_secondary_diagonal_win(self) -> int:
        """
        Check if 4 discs are connected on a second diagonal-like line
        Example:
        . . #
        . # .
        # . .
        or
        . . .
        . . #
        . # .
        or
        . # .
        # . .
        . . .
        :return: The winner's number (1 or 2) or 0 if no one won yet
        """
        # Same as the main diagonal, just that we go up right, so +7 then +1 to go to the above row i-1, j+1 basically

        if self.__bitboard1 & (self.__bitboard1 >> 8) & (self.__bitboard1 >> 16) & (self.__bitboard1 >> 24) > 0:
            return 1  # Player 1 won
        if self.__bitboard2 & (self.__bitboard2 >> 8) & (self.__bitboard2 >> 16) & (self.__bitboard2 >> 24) > 0:
            return 2  # Player 2 won

        return 0  # No one won

    def check_win(self) -> int:
        """
        Check if a column has 4 discs connected on a column, row, or diagonal and if so, what player wins.
        :return: 0 If no one won yet, 1 if Player 1 won, 2 if Player 2 won (or the computer)
        """
        # Check on columns
        column_win_check = self.__check_column_win()
        if column_win_check:
            return column_win_check
        # Check on rows
        row_win_check = self.__check_row_win()
        if row_win_check:
            return row_win_check
        # Check main diagonal-oriented diagonals
        main_diagonal_win_check = self.__check_main_diagonal_win()
        if main_diagonal_win_check:
            return main_diagonal_win_check
        # Check secondary diagonal-oriented diagonals
        secondary_diagonal_win_check = self.__check_secondary_diagonal_win()
        if secondary_diagonal_win_check:
            return secondary_diagonal_win_check

        # No one won after all the checks
        return 0

    def check_full(self) -> bool:
        """
        Function to check if the grid is full (in the bitmask the bit representing to the 1 above all the rows are all 1's, so all the columns are full)
        :return: True if grid is full, False otherwise
        """
        full = False
        mask = 0b1000000100000010000001000000100000010000001000000
        if (self.__bitboard & (1<<6)) | (self.__bitboard & (1<<13)) | (self.__bitboard & (1<<20)) | (self.__bitboard & (1<<27)) | (self.__bitboard & (1<<34)) | (self.__bitboard & (1<<41)) | (self.__bitboard & (1<<48)) == mask: # If the bits representing that a column is full are full
            full = True

        return full

    def check_column_full(self, column: int) -> bool:
        if self.__last_disc_placed_row[column] == -1:
            return True

        return False

    def remove_disc(self, column):  # Remove last disc placed on a column
        self.__bitboard = self.__bitboard ^ (1 << (column * 7 + 5 - (self.__last_disc_placed_row[column])))
        # The bit at that position is 1, because it's above the last disc placed on that column, make it 0
        self.__last_disc_placed_row[column] += 1 # Removed one, so the position changed, now it represents the position of the last disc placed, and we REMOVE IT, and place a 1 in bitboard here

        # Remove the disc in the corresponding bitboard of p1 or p2, depending on whose disc it is
        if self.__data[self.__last_disc_placed_row[column]][column] == 1:
            self.__bitboard1 = self.__bitboard1 ^ (1 << (column * 7 + 5 - (self.__last_disc_placed_row[column])))
        elif self.__data[self.__last_disc_placed_row[column]][column] == 2:
            self.__bitboard2 = self.__bitboard2 ^ (1 << (column * 7 + 5 - (self.__last_disc_placed_row[column])))

        self.__data[self.__last_disc_placed_row[column]][column] = 0
        # Make the bit that represented the last placed disc on this column 1
        # Because it is now the last bit of the column above the last disc placed, where it was the last disc before removing it, now will be 1, it is above the second last disc placed, because the last one is removed
        # So before it was 0/1 with 1 above, now it is 1 to represent that it actually stops here, with 0 above.
        self.__bitboard = self.__bitboard | (1 << (column * 7 + 5 - (self.__last_disc_placed_row[column])))

    # Below function is unused
    """
    def create_bitmask(self) -> int:
        Each column is encoded by 6 bits consecutively from down to up, 7x6 = 42 bits needed
        P1's discs are bit 1, P2's discs are bit 0, but... 0 is also the empty cells soooo
        To identify the empty cells, an extra 1 is added on the lowest empty cell of each column, all other bits above it are set to 0. Note that we need the extra bit per column to encode full columns.
        So the bitboard is actually 7x7
        5 12 19 26 33 40 47
        4 11 18 25 32 39 46
        3 10 17 24 31 38 45
        2  9 16 23 30 37 44
        1  8 15 22 29 36 43
        0  7 14 21 28 35 42
        :return: Bitboard of the position
        bitboard = 0
        # So we go through the data array's columns and make 1 the bits of player 1, leave 0 the bits of player 2
        # And when we reach a row on the column that is 0, we encode it as 1
        # So basically we know that the last one bottom-up on a column in the bitmask is always the first empty row on that column, like self.__last_disc_placed_row[column]
        # This ensures each position as unique, as we have both player 1's and 2's discs as in a normal table
        # And a 1 above to always know that "the 0's above this 1 DO NOT MATTER, YOU CAN IGNORE THEM"
        # And when the table is full the top row of the bitboard will just be 1's

                  0000000
        .......   0001000
        ...o...   0010000
        ..xx...   0011000
        ..ox...   0001100
        ..oox..   0000110
        ..oxxo.   1101101
        
        special thanks to http://blog.gamesolver.org/solving-connect-four/06-bitboard/

        for column in range(self.__COLUMNS):
            for row in range(self.__ROWS - 1, -1, -1):
                if self.__data[row][column] == 1:
                    bitboard = bitboard | (1 << (column * 7 + (5 - row)))  # rows are also inverted bottom-up
                    # first 6 bits are for column 0 (0 to 5), 7-12 = 1*7 + 0 to 5 for column 1, 14-19 = 2*7+ 0 to 5 for column 2, etc.
                # player 2's bits remain 0, we don't check it
                if self.__data[row][
                    column] == 0:  # Reached the 0 in the column, encode it as 1 and go to next column, the bits "above" it will be 0
                    bitboard = bitboard | (1 << (column * 7 + (5 - row)))
                    break

                # The high most bit on a column (7, 13, 20, 27, 34, 41, 48) which we ignored until now
                # Will be 1 if that column is full, check if it is full
                if row == 0:  # reached the uppermost row of the column, and it's not 0, encode the bit that signifies that the column is full
                    bitboard = bitboard | (1 << (column * 7 + 6))

        return bitboard
    """
    def get_bitboard(self) -> int:
        """
        Function to return the bitboard representing the current game's grid.
        :return: The bitboard
        """
        return self.__bitboard

    def game_over(self) -> bool:
        """
        Checks if the game is over
        :return: True if game over, False if game is ongoing
        """
        if self.check_win() or self.check_full():
            return True

        return False

    def count_discs(self, player: int) -> int:
        """
        Function to count the total discs on the grid of a given player using the bitboard of that player
        :param player: The player (1 or 2) for which we count the discs
        :return: The number of discs
        """
        # In the bitboard of the player, 1's are only their discs, so count that
        if player !=1 and player !=2:
            raise GridException("Player should be 1 or 2.")

        if player == 1:
            return self.__bitboard1.bit_count()
        if player == 2:
            return self.__bitboard2.bit_count()

    def count_discs_connected_of(self, player: int) -> tuple:
        """
        Returns a tuple with the count of 2-connected and 3-connected discs of a given player on a grid, used in scoring a non-winning position.
        :param player: The player (1 or 2)
        :return: The count of 2-connected and 3-connected discs
        """
        # Use the logic as when checked for wins to count the discs in constant time
        number_of_connections3 = 0
        number_of_connections2 = 0

        if player == 1:
            a =  self.__bitboard1 & (self.__bitboard1 >> 1) & (self.__bitboard1 >> 2)
            if a:
                number_of_connections3 += a.bit_count()
            a = self.__bitboard1 & (self.__bitboard1 >> 7) & (self.__bitboard1 >> 14)
            if a:
                number_of_connections3 += a.bit_count()
            a = self.__bitboard1 & (self.__bitboard1 >> 6) & (self.__bitboard1 >> 12)
            if a:
                number_of_connections3 += a.bit_count()
            a =  self.__bitboard1 & (self.__bitboard1 >> 8) & (self.__bitboard1 >> 16)
            if a:
                number_of_connections3 += a.bit_count()

            a = self.__bitboard1 & (self.__bitboard1 >> 1)
            if a:
                number_of_connections2 += a.bit_count()
            a = self.__bitboard1 & (self.__bitboard1 >> 7)
            if a:
                number_of_connections2 += a.bit_count()
            a = self.__bitboard1 & (self.__bitboard1 >> 6)
            if a:
                number_of_connections2 += a.bit_count()
            a = self.__bitboard1 & (self.__bitboard1 >> 8)
            if a:
                number_of_connections2 += a.bit_count()

        else:
            b = self.__bitboard2 & (self.__bitboard2 >> 1) & (self.__bitboard2 >> 2)
            if b:
                number_of_connections3 += b.bit_count()
            b = self.__bitboard2 & (self.__bitboard2 >> 7) & (self.__bitboard2 >> 14)
            if b:
                number_of_connections3 += b.bit_count()
            b = self.__bitboard2 & (self.__bitboard2 >> 6) & (self.__bitboard2 >> 12)
            if b:
                number_of_connections3 += b.bit_count()
            b =  self.__bitboard2 & (self.__bitboard2 >> 8) & (self.__bitboard2 >> 16)
            if b:
                number_of_connections3 += b.bit_count()

            b = self.__bitboard2 & (self.__bitboard2 >> 1)
            if b:
                number_of_connections2 += b.bit_count()
            b = self.__bitboard2 & (self.__bitboard2 >> 7)
            if b:
                number_of_connections2 += b.bit_count()
            b = self.__bitboard2 & (self.__bitboard2 >> 6)
            if b:
                number_of_connections2 += b.bit_count()
            b = self.__bitboard2 & (self.__bitboard2 >> 8)
            if b:
                number_of_connections2 += b.bit_count()


        return (number_of_connections2, number_of_connections3)

    def __str__(self) -> str:
        """
        Returns the object in string format
        :return: The string format
        """
        t = Texttable()
        for row in range(6):
            row_data = [' ' for i in range(7)]
            for column in range(7):
                symbol = ' '
                if self.__data[row][column] == 1:
                    symbol = 'X'

                elif self.__data[row][column] == 2:
                    symbol = 'O'

                row_data[column] = symbol
            t.add_row(row_data)
        if self.current_turn:
            return colored(t.draw(), 'green')
        else:
            return colored(t.draw(), 'red')
