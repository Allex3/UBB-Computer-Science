
class BoardException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

class OutOfBoundsException(BoardException):
    def __init__(self):
        super().__init__("Position out of bounds")

class AlreadyHitException(BoardException):
    def __init__(self):
        super().__init__("Position already hit")
        #BoardException.__init__("Position already hit")

class GameOver(Exception):
    pass