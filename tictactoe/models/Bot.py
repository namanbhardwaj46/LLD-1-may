from tictactoe.Service.Strgy.BotFactory import BotFactory
from tictactoe.models.BotDificulty import BotDificulty
from tictactoe.models.Player import Player
from tictactoe.models.PlayerType import PlayerType
from tictactoe.models.Symbol import Symbol


class Bot(Player):
    def __init__(self, name: str, symbol: Symbol, id: int, dificulty: BotDificulty):
        super().__init__(name, symbol, PlayerType.BOT, id)
        self.dificulty = dificulty
        self.strategy = BotFactory.createBot(dificulty)


    def decide_cell(self, board):
        return self.strategy.decide_move(board)
