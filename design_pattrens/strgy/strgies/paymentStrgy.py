from abc import ABC


class PaymentStrategy(ABC):
    def pay(self, amount: float) -> str:
        """
        Process the payment of the given amount.

        :param amount: The amount to be paid.
        :return: A confirmation message.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")