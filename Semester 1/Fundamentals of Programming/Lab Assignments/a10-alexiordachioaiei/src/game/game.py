from copy import deepcopy

from src.board.grid import DiscsGrid, DiscException, GridException


class ComputerStrategy:
    """
    Class used for the computer strategy algorithm
    Uses the minimax algorithm to compute the best move that the computer can make
    The depth (complexity and efficiency) of the algorithm is given at init time

    Fields: Infinity to use in computations, the turn the AI has in the game, the depth of the algorithm, the columns we will search in order
    Transposition table: A dictionary storing the evaluation for a specific bitmask to optimize computations where we get to the same position later

    Functions:
        - The minimax function that is the actual backtracking algorithm that gets all the possible positions until depth 0 is reached
        - A function that gets the evaluation of a function if game is won or not
        - A function used in storing a position that is NOT won
        - A function that combines all of the above, to return the best move the computer can make at the initial position
    """
    def __init__(self, ai_turn: bool, depth: int = 10):
        """
        Function to initialize the computer's strategy using minimax algorithm with alpha-beta pruning
        :param ai_turn: True if AI is playing first, False if the AI is playing second.
        """
        self.__INF = int(1e308)
        self.__AI_TURN = ai_turn
        self.__DEPTH = depth
        self.__COLUMNS = [3, 2, 4, 1, 5, 0, 6]  # Heuristics: Search columns starting from the middle
        self.__TRANSPOSITION_TABLE: dict[
            int, int] = {}  # Stores the boards we already explored and their scores, in bitboard format

    def __score_position(self, position: DiscsGrid) -> int:
        """
        Function used to compute and get the score of a given non-winning position heuristic
        :param position: The position's board
        :return: The score of the given position
        """
        number_of_2_connections_1, number_of_3_connections_1 = position.count_discs_connected_of(1)
        number_of_2_connections_2, number_of_3_connections_2 = position.count_discs_connected_of(2)
        if self.__AI_TURN:
            return (number_of_3_connections_1*3 + number_of_2_connections_1*2) - (
                        number_of_3_connections_2*3 + number_of_2_connections_2*2)
        else:  # AI is player 2
            return (number_of_3_connections_2*3 + number_of_2_connections_2*2) - (
                    number_of_3_connections_1*3 + number_of_2_connections_1*2)

    def __get_evaluation_of_position(self, position: DiscsGrid) -> int:
        """
        Get the score of a current position.
        :param position: The current position
        :return: The score of the current position
        """
        # The board is either full or a win, if it is a win
        """
        A position has:
            > 0 score if the first player (True) wins; 1 if they win with the last disc, 2 with the second to last, etc.
            null score if draw (board full or maximum depth with no winning..)
            < 0 score if the second player (False) wins; -1 if they win with the last disc, -2 with the second to last, etc.
            
            Basically a winning position's score is 22 - the number of discs p1 or p2 placed, but p2 is inverted
            Both players can place AT MOST 21 (42/2) discs, so it makes sense to be 22 - the number of discs placed until the win, for the requirements I stated above.
        """

        match position.check_win():
            case 0:  # No one won, the board is either full or the max depth is reached, so we will score the lengths of partially built rows of 4 and subtract that from our opponent's partially built lines
                if position.check_full():
                    return 0
                return self.__score_position(position)
            case 1:  # First turn player won
                if self.__AI_TURN:
                    return 22 - position.count_discs(1)
                else:
                    return -(22 - position.count_discs(1))
            case 2:  # Second turn player won
                if not self.__AI_TURN:
                    return 22 - position.count_discs(2)
                else:
                    return -(22 - position.count_discs(2))

    def __minimax(self, position: DiscsGrid, depth: int, alpha: int, beta: int, maximizing_player: bool) -> int:
        """
        Minimax algorithm with alpha-beta pruning
        We begin the algorithm with a specific position that IS in the game, getting all the children positions from there.
        :param position: The board we are running minimax on, first call it is the true board the player is on.
        :param depth: How deep we go in the tree, basically each depth represents all the ways to place a disc from a specific position.
        :param alpha: The minimum value of player 1's (True) position value at a higher depth in the tree, successfully seeing if it's redundant to go down a branch, as if the maximum value of player 2 (beta) is lower than or equal to the minimum value of player 1 (alpha), then we cannot get a higher value for maxeval of player 2 no matter how much we go down that branch, on which player 2 is playing, so ignore it and use the alpha value.
        :param beta: The maximum value of player 2's (False) position value at a higher depth in the tree, successfully seeing if it's redundant to go down a branch, as if the minimum value of player 1 (alpha) is higher than the maximum value of player 2 (beta), then we cannot get a lower value for maxeval of player1 no matter how much we go down that branch on which player 1 is playing, so ignore it and use the beta value.
        :param maximizing_player:
        :return:
        """
        if depth == 0 or position.game_over():
            return self.__get_evaluation_of_position(position)

        if maximizing_player == self.__AI_TURN:
            maximum_evaluation = -self.__INF
            for column in self.__COLUMNS:
                if not position.check_column_full(column):
                    position.place_disc(column + 1, maximizing_player)
                    position_bitmask = position.get_bitboard()
                    if position_bitmask in self.__TRANSPOSITION_TABLE:
                        evaluation = self.__TRANSPOSITION_TABLE[position_bitmask]
                    else:
                        evaluation = self.__minimax(position, depth - 1, alpha, beta, not maximizing_player)
                        self.__TRANSPOSITION_TABLE[position_bitmask] = evaluation
                    if evaluation > maximum_evaluation:
                        maximum_evaluation = evaluation

                        # IF we are at the depth we started at, basically the root of the tree, and we finished
                        # Then it means the algorithm is done, so ALSO return the BEST MOVE, along with the best evaluation
                        if depth == self.__DEPTH:
                            self.__best_move = column + 1

                    # we are DONE with the current column addition, remove the disc we placed on that column
                    position.remove_disc(column)

                    alpha = max(alpha, maximum_evaluation)
                    if beta <= alpha:
                        break  # No use to check the positions down that branch's positions (the tree lives in my head rent-free)

            return maximum_evaluation

        else:
            minimum_evaluation = self.__INF
            for column in self.__COLUMNS:
                if not position.check_column_full(column):
                    position.place_disc(column + 1, maximizing_player)
                    position_bitmask = position.get_bitboard()
                    if position_bitmask in self.__TRANSPOSITION_TABLE:
                        evaluation = self.__TRANSPOSITION_TABLE[position_bitmask]
                    else:
                        evaluation = self.__minimax(position, depth - 1, alpha, beta, not maximizing_player)
                        self.__TRANSPOSITION_TABLE[position_bitmask] = evaluation
                    if evaluation < minimum_evaluation:
                        minimum_evaluation = evaluation

                        if depth == self.__DEPTH:
                            self.__best_move = column + 1

                    position.remove_disc(column)

                    beta = min(beta, minimum_evaluation)
                    if alpha >= beta:
                        break

            return minimum_evaluation

    def place_disc(self, position: DiscsGrid):
        """
        Function to "place" the disc for the computer, just computes the minimax alpha-beta pruning algorithm
        :param position: The position at which we start the algorithm
        :return: The best move (column) where the computer can move
        """
        self.__minimax(position, self.__DEPTH, -self.__INF, +self.__INF, self.__AI_TURN)
        return self.__best_move


class ConnectFour:
    """
    Class that stores the actual game functionalities combining all the classes
    Used to place the discs and setting the difficulty of the game, or turn of the AI, checking the win or if the game is full by using functions from the DiscsGrid class
    Uses a ComputerStrategy object to compute the best move for the AI given a position.
    """
    def __init__(self, grid: DiscsGrid):
        """
        Function to initialize an object of the main game
        :param grid: The grid object we use to play on, first has an empty board.
        """
        self.__grid: DiscsGrid = grid
        self.__strategy: ComputerStrategy = None
        self.__AI_TURN: bool = None
        self.__STRATEGY_DEPTH: int = None

    @property
    def grid(self):
        """
        I think this is unused?? Anyway returns the grid
        :return: None
        """
        return self.__grid

    def set_computer_strategy(self) -> None:
        """
        Sets the computer strategy using the depth and turn
        :return: None
        """
        self.__strategy = ComputerStrategy(self.__AI_TURN, self.__STRATEGY_DEPTH)

    def set_computer_turn(self, turn: bool) -> None:
        """
        Sets the computer turn to 1 or 2 (True/False)
        :param turn: The computer's turn
        :return: None
        """
        self.__AI_TURN = turn

    def set_difficulty(self, depth: int) -> None:
        """
        Sets the difficulty (depth) of the minimax algorithm
        :param depth: The depth
        :return: None
        """
        self.__STRATEGY_DEPTH = depth

    def place_player(self, column: int, player: bool) -> None:
        """
        Function to place a disc in a column for a given player
        :param column: The column (1<=column<=7) to place the disc in
        :param player: The player (True=1, False=2) that places the column
        :return: None
        """
        self.__grid.place_disc(column, player)

    def place_computer(self) -> int:
        """
        Function to place the best disc for the computer
        :return: The best move (column) in which the computer will move
        """
        best_move = self.__strategy.place_disc(self.__grid)
        self.__grid.place_disc(best_move, self.__AI_TURN)
        return best_move

    def check_win(self) -> int:
        """
        Check if the game is won and return the player who won if so (1/2/0)
        :return: The player who won or 0 if no one won
        """
        return self.__grid.check_win()

    def check_full(self) -> bool:
        """
        Check if the board is full
        :return: Returns True if board is full, False otherwise
        """
        return self.__grid.check_full()

    def __str__(self) -> str:
        # Returns the grid in string format
        return self.__grid.__str__()
