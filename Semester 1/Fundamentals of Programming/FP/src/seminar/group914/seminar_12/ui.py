from seminar.group914.seminar_12.board import ShipDirection, ShipWasSunkException
from seminar.group914.seminar_12.game import Battleships


class UI:
    __directions = {'LEFT': ShipDirection.LEFT, 'UP': ShipDirection.UP, 'RIGHT': ShipDirection.RIGHT,
                    'DOWN': ShipDirection.DOWN}

    def __init__(self):
        self.__game = Battleships()

    def __place_player_ships(self):
        ships_to_place = 2

        while ships_to_place > 0:
            ship_location = input("where to place ship (e.g., C3 left) >")
            ship_location = ship_location.upper().strip()
            tokens = ship_location.split(' ')

            try:
                column = ord(tokens[0][0]) - ord('A')  # ord('C') - ord('A') == 2
                row = int(tokens[0][1]) - 1
                direction = UI.__directions[tokens[1]]
                self.__game.player_board.place_ship(row, column, direction)
                ships_to_place -= 1
            except Exception as e:
                print("Problem with placing ships - " + str(e))

    def start(self):
        self.__place_player_ships()

        while True:
            print("My board")
            print(self.__game.player_board)
            print("Targeting board")
            print(self.__game.computer_board)
            fire_coordinates = input("fire>").strip()

            # TODO Checks here ...
            column = ord(fire_coordinates[0].upper()) - ord('A')  # 'B' - 'A' means column index 1
            row = int(fire_coordinates[1]) - 1

            try:
                # TODO Set a flag so we know when it's the human player and when the computer
                # TODO Have a game over exception that is raised when all ships are sunk
                self.__game.fire_human_player(row, column)
                self.__game.fire_computer_player()
            except ShipWasSunkException:
                print("A ship was sunk!")


ui = UI()
ui.start()
