from tictactoe.models.BotDificulty import BotDificulty
from tictactoe.models.Player import Player
from tictactoe.models.PlayerType import PlayerType


class Bot(Player):
    def __init__(self, name: str, symbol: str, id: int, dificulty: BotDificulty):
        super().__init__(name, symbol, PlayerType.BOT, id)
        self.dificulty = dificulty
        self.strategy = None