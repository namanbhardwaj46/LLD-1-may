from tictactoe.Service.Strgy.botStrrgy.EasyBot import EasyBot
from tictactoe.models.BotDificulty import BotDificulty


class BotFactory:

    @staticmethod
    def createBot(dificulty):
        if dificulty == BotDificulty.EASY:
            return EasyBot()
        return None
