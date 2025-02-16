class BoardExceptions(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class OutOfBoundsExceptions(BoardExceptions):
    def __init__(self):
        super().__init__("Position is out of bounds")


class AlreadyHitExceptions(BoardExceptions):
    def __init__(self):
        super().__init__("Position was already hit")

class GameOverException(Exception):
    pass