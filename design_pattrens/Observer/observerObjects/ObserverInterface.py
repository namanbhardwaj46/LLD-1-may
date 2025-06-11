from abc import ABC


class ObserverInterface(ABC):

    def update(self, temp, humidity):
        """
        Update the observer with new data.

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")
