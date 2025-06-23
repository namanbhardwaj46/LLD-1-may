from tictactoe.Service.Strgy.winning.DiagonalWs import DiagonalWs
from tictactoe.controllers.GameController import GameController
from tictactoe.models.Bot import Bot
from tictactoe.models.BotDificulty import BotDificulty
from tictactoe.models.GameStatus import GameStatus
from tictactoe.models.Player import Player
from tictactoe.models.PlayerType import PlayerType
from tictactoe.models.Symbol import Symbol

if __name__ == "__main__":
    gc = GameController()

    dimension = 3

    player = [
        Player("X", Symbol("X"), PlayerType.HUMAN, 0),
        Bot("O", Symbol("O"), 1,  BotDificulty.EASY)
    ]


    winningStrgy = [DiagonalWs()]

    game = gc.start_game(dimension, player, winningStrgy)

    while game.game_status == GameStatus.IN_PROGRESS:
        gc.display_game(game)
        cell = gc.take_input(game)
        if game.game_status == GameStatus.IN_PROGRESS:
            undoQues = input("Do you want to undo the last move? 1/0: ")
            if undoQues == "1":
                gc.undo_input(game)
                gc.display_game(game)

    if game.game_status == GameStatus.COMPLETED:
        print(f"Player {game.winner.name} wins!")

    else:
        print("It's a draw!")

