class BoardException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message

class InvalidFire(BoardException):
    def __init__(self):
        super().__init__("Invalid fire")

class NiceHitBro(BoardException):
    def __init__(self):
        super().__init__("Nice hit bro, you found an alien ship")

class YouWon(BoardException):
    def __init__(self):
        super().__init__("GGWP, you won")

class YouLost(BoardException):
    def __init__(self):
        super().__init__("You lost, get better next time")

class CloseOne(BoardException):
    def __init__(self):
        super().__init__("You hit nothing")