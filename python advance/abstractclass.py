from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, no_of_tiers):
        self.no_of_tiers = no_of_tiers

    @abstractmethod
    def start(self):
        raise NotImplementedError


class Car(Vehicle):

    def start(self):
        print("Car is starting with self start")

    @abstractmethod
    def stop(self):
        pass


class audiCar(Car):

    def stop(self):
        print("Car is stopping with self stop")


# c = Car(5)
# print(c.no_of_tiers)

a = audiCar(5)

print(a.no_of_tiers)


class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(10, 20))
