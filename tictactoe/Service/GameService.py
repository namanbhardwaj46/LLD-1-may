from tictactoe.models.CellStatus import CellStatus
from tictactoe.models.GameStatus import GameStatus


class GameService:

    def start_game(self, size_board, players, winning_strgy):
        from tictactoe.models.Game import Game
        from tictactoe.models.Board import Board

        board = Board(size_board)
        game = Game(board, players, winning_strgy)

        return game


    def display_game(self, game):
        game.board.display_game()


    def take_input(self, game):
        curr_player = game.players[game.current_player_index]
        print(f"Player {curr_player.name}'s turn")

        cell = curr_player.decide_cell(game.board)
        cell.player = curr_player
        cell.status = CellStatus.FILLED
        game.moves.append(cell)

        if self.check_winner(game, cell):
            game.winner = curr_player
            game.game_status = GameStatus.COMPLETED
        elif len(game.moves) == game.board.board_size * game.board.board_size:
            game.game_status = GameStatus.DRAW

        game.current_player_index +=1
        game.current_player_index %= len(game.players)


    def check_winner(self, game, cell):
        for win in game.winning_strgy:
            if win.check_winner(game.board, cell):
              return True
        return False



    def undo_input(self, game):
        if not game.moves:
            print("No moves to undo.")
            return
        cell = game.moves.pop()

        for win in game.winning_strgy:
            win.undo_count( cell, game.board)

        cell.status = CellStatus.EMPTY
        cell.player = None
        game.current_player_index -=1
        game.current_player_index %= len(game.players)