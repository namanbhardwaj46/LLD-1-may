from tictactoe.models.CellStatus import CellStatus
from tictactoe.models.Symbol import Symbol


class Player:
    def __init__(self, name: str, symbol: Symbol, type, id):
        self.name = name
        self.symbol = symbol
        self.type = type
        self.id = id


    def decide_cell(self, board):

        while True:
            row = int(input(f"Enter row (0 to {board.board_size - 1}): "))
            col = int(input(f"Enter column (0 to {board.board_size - 1}): "))
            if 0<= row < board.board_size and 0<= col < board.board_size:
                if board.grid[row][col].status == CellStatus.EMPTY:
                    return board.grid[row][col]

            print("Invalid input. Please try again.")