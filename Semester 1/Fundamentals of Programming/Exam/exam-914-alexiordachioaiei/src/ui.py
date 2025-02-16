from game import Game
from board import BoardError
from game import GameError


class UI:
    def __init__(self, game: Game):
        self.__game = game

        self.__OPTIONS = {"LOAD": "Type 0 if you choose to start a new game, or 1 if you wish to load the game from file",
                          "SELECT": "Type 1 if you wish to play first, 2 if you wish to play second.",
                          "PLACE_PLAYER": "The player is placing a piece.",
                          "PLACE_COMPUTER": "The computer is placing a piece.",
                          "PLACE_ROW": "Row: ",
                          "PLACE_COLUMN": "Column: ",
                          "MOVE_PLAYER": "The player is moving a piece.",
                          "MOVE_COMPUTER": "The computer is moving a piece",
                          "MOVE_ROW": "From row: ",
                          "MOVE_COLUMN": "From column: ",
                          "PLAYER_WIN": "The player won!",
                          "COMPUTER_WIN": "The computer won!",
                          "SAVE_CHOICE": "Type 1 if you want to save the game now, 0 if not"}

        self.__ERRORS = {"INT": "Your value is not an integer. Try again.",
                         "INPUT": "Your input is invalid. Try again."}

    def __display_board(self):
        print(self.__game)



    def run(self):
        self.__display_board()

        print(self.__OPTIONS["LOAD"])
        option = input("> ")
        match option:
            case "0":
                self.__start_new_game()
            case "1":
                self.__load_game()
            case _:
                print(self.__ERRORS["INPUT"])
                self.run()

    def __start_new_game(self):
        self.__turn = 1
        self.__game.save()
        print(self.__OPTIONS["SELECT"])
        option = input("> ")
        match option:
            case "1":
                self.__game.set_turns(1, 2)
                self.__player = 1
                self.__computer = 2
                self.__run_placement()
            case "2":
                self.__game.set_turns(2, 1)
                self.__player = 2
                self.__computer = 1
                self.__run_placement()
            case _:
                print(self.__ERRORS["INPUT"])
                self.__start_new_game()

    def __load_game(self):
        try:
            self.__game.load()
        except Exception as e: # No game to load (players not even selected)
            print(e)
            self.__start_new_game()
            return
        self.__display_board()
        self.__player = self.__game.get_player()
        self.__computer = self.__game.get_computer()
        self.__turn = self.__game.get_turn()
        if self.__game.get_phase():
            self.__run_movement()
        else:
            self.__run_placement()

    def __get_placement(self):
        try:
            row = int(input(self.__OPTIONS["PLACE_ROW"]))
            column = int(input(self.__OPTIONS["PLACE_COLUMN"]))
            return (row, column)
        except ValueError:
            print(self.__ERRORS["INT"])
            self.__get_placement()


    def __run_placement(self):
        while True:
            if self.__player == self.__turn:
                print(self.__OPTIONS["PLACE_PLAYER"])
                move = self.__get_placement()
                try:
                    self.__game.place_piece(self.__player, move[0], move[1])
                except BoardError as e:
                    print(e)
                    continue # Get the input of the player again
                self.__display_board()
                winner = self.__game.get_winner()
                if winner == self.__player:
                    print(self.__OPTIONS["PLAYER_WIN"])
                    return

            if self.__computer == self.__turn:
                print(self.__OPTIONS["PLACE_COMPUTER"])
                self.__game.place_computer()
                self.__display_board()
                winner = self.__game.get_winner()
                if winner ==  self.__computer:
                    print(self.__OPTIONS["COMPUTER_WIN"])
                    return

            self.__turn = self.__turn % 2 + 1
            self.__game.save()

            # No one won, check if we go to the movement phase
            if self.__game.get_phase(): # If True we are in the movement phase
                self.__run_movement()
                return

    def __get_movement(self):
        try:
            row = int(input(self.__OPTIONS["MOVE_ROW"]))
            column = int(input(self.__OPTIONS["MOVE_COLUMN"]))
            return (row, column)
        except ValueError:
            print(self.__ERRORS["INT"])
            self.__get_movement()

    def __run_movement(self):
        while True:
            if self.__player == self.__turn:
                print(self.__OPTIONS["MOVE_PLAYER"])
                move = self.__get_movement()
                try:
                    self.__game.move_piece(self.__player, move[0], move[1])
                except BoardError as e:
                    print(e)
                    continue
                self.__display_board()
                winner = self.__game.get_winner()
                if winner == self.__player:
                    print(self.__OPTIONS["PLAYER_WIN"])
                    return

            if self.__computer == self.__turn:
                print(self.__OPTIONS["MOVE_COMPUTER"])
                self.__game.move_computer()
                self.__display_board()
                winner = self.__game.get_winner()
                if winner == self.__computer:
                    print(self.__OPTIONS["COMPUTER_WIN"])
                    return

            self.__turn = self.__turn % 2 + 1
            self.__game.save()


