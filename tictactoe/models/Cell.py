from tictactoe.models.CellStatus import CellStatus


class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.player = None
        self.status = CellStatus.EMPTY



    def print_cell(self):
        if self.status == CellStatus.EMPTY:
            print("| |", end="")
        else:
            print(f"|{self.player.symbol.symbol}|", end="")
