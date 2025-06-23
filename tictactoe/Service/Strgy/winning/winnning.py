from abc import ABC, abstractmethod


class Winning(ABC):

    @abstractmethod
    def check_winner(self, board, cell):
        pass

    @abstractmethod
    def undo_count(self, board, cell):
        pass