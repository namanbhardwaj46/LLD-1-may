from tictactoe.models.Board import Board
from tictactoe.models.CellStatus import CellStatus


class EasyBot:

    def decide_move(self, board: Board):
        # Find the first empty cell and place the player's mark there
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None