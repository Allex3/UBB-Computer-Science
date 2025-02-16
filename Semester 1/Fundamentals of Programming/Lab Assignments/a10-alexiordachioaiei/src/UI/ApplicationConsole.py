from src.game.game import ConnectFour, GridException, DiscException


class Application:
    def __init__(self, game: ConnectFour):
        self.__game = game

        self.__UI = {"CHOOSE_GAMEMODE": "Type 'pvp' to play pvp, or 'computer' to play against a computer.",
                     "CHOOSE_PLAYER": "Type 1 to play first, or 2 to play second.",
                     "CHOOSE_COLUMN": "What column do you want to insert your disc in?",
                     "PLAYER_1": "Player 1 plays.",
                     "PLAYER_2": "Player 2 plays.",
                     "PLAYER": "Player plays.",
                     "COMPUTER": "Computer plays.",
                     "PLAYER_WIN": "Player wins! Game ends.",
                     "PLAYER_1_WIN": "Player 1 wins! Game ends.",
                     "PLAYER_2_WIN": "Player 2 wins! Game ends.",
                     "COMPUTER_WIN": "Computer wins! Game ends.",
                     "TIE": "No one won, good luck next time!",
                     "PLAYER_SELECT": "Do you want to play first (1) or let the computer play first (2): "}

        self.__ERRORS = {"INVALID_INPUT": "Your input is invalid. Try again.",
                         "INT": "Your input is not an integer. Try again"}

    def run(self):
        self.__PLAYER = self.__get_player()
        if self.__PLAYER == 1:
            self.__PLAYER = True
            self.__game.set_computer_turn(False) # Computer is player 2
        else:
            self.__PLAYER = False
            self.__game.set_computer_turn(True) # Computer is player 1

        self.__game.set_difficulty(11)
        self.__game.set_computer_strategy()
        self.__run_computer()

    def __place_player(self):
        print(self.__UI["PLAYER"])
        print(self.__UI["CHOOSE_COLUMN"])
        try:
            column = int(input("> "))
            self.__game.place_player(column, self.__PLAYER)
        except ValueError:
            print(self.__ERRORS["INT"])
            self.__place_player()
        except GridException as e:
            print(e)
            self.__place_player()
        except DiscException as e:
            print(e)
            self.__place_player()

    def __place_computer(self):
        print(self.__UI["COMPUTER"])
        self.__game.place_computer()

    def __get_player(self):
        try:
            player = int(input(self.__UI["PLAYER_SELECT"]))
            if not 1 <= player <= 2:
                print(self.__ERRORS["INVALID_INPUT"])
                return self.__get_player()
            return player
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_player()

    def __run_computer(self):
        turn = 1
        while (True):
            if turn % 2:
                if self.__PLAYER:
                    self.__place_player()
                else:
                    self.__place_computer()
            else:
                if not self.__PLAYER:
                    self.__place_player()
                else:
                    self.__place_computer()

            turn = (turn + 1) % 2

            print(self.__game)

            winner = self.__game.check_win()
            if winner == 1 and self.__PLAYER:
                print(self.__UI["PLAYER_WIN"])
                return
            elif winner == 1 and not self.__PLAYER:
                print(self.__UI["COMPUTER_WIN"])
                return
            elif winner == 2 and self.__PLAYER:
                print(self.__UI["COMPUTER_WIN"])
                return
            elif winner == 2 and not self.__PLAYER:
                print(self.__UI["PLAYER_WIN"])
                return

            if self.__game.check_full():
                print(self.__UI["TIE"])
                return
