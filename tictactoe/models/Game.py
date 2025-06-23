from tictactoe.models.GameStatus import GameStatus


class Game:
    def __init__(self, board, players, winning_strgy):
        self.board = board
        self.players = players
        self.winning_strgy = winning_strgy
        self.current_player_index = 0
        self.winner = None
        self.game_status = GameStatus.IN_PROGRESS
        self.moves = []