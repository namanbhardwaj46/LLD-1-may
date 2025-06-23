from tictactoe.models.Cell import Cell


class Board:
    def __init__(self, board_size: int = 3):
       self.board_size = board_size
       self.grid = [[Cell(row, col) for col in range(board_size)] for row in range(board_size)]


    def display_game(self):
        for row in self.grid:
            for cell in row:
                cell.print_cell()
            print()
