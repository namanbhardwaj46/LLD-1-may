

class GameService:

    def start_game(self, size_board, players, winning_strgy):
        from tictactoe.models.Game import Game
        from tictactoe.models.Board import Board

        board = Board(size_board)
        game = Game(board, players, winning_strgy)

        return game


    def display_game(self, game):
        game.board.display_game()
