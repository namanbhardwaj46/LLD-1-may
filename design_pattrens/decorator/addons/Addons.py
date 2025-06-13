from abc import ABC


class Addons(ABC):

    def __init__(self, pizza):
        self.pizza = pizza

    @staticmethod
    def get_price():
        pass
