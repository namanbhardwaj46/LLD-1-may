from abc import ABC


class BankAdapterInterface(ABC):
    def get_balance(self):
        raise NotImplementedError("This method should be overridden by subclasses")