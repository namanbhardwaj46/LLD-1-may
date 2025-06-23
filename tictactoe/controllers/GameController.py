from tictactoe.Service.GameService import GameService


class GameController:

    def __init__(self):
        self.gameService = GameService()

    def start_game(self, size_board, players, winning_strgy):
        return self.gameService.start_game(size_board, players, winning_strgy)

    def display_game(self, game):
        self.gameService.display_game(game)

    def take_input(self,game):
        return self.gameService.take_input(game)

    def undo_input(self, game):
        return self.gameService.undo_input(game)


# Start a new game
#  initilize status of game to inprogress
# IN LOOP:
#     display board
#     take input from player
#       check if valid move
#       play the move
#       check if player has won
#       if not won, check if draw
#       else switch player
#       GO back to LOOP