from tictactoe.models.Symbol import Symbol


class Player:
    def __init__(self, name: str, symbol: Symbol, type, id):
        self.name = name
        self.symbol = symbol
        self.type = type
        self.id = id