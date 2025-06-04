from audioop import error
from typing import Any, Union, Optional
from typing import Generic, TypeVar


# a: int = 5
#
# print(a+10)
# #
# a= "abc"
# print(a+9)


# Method

def add(a: int, b: int) -> int:
    return a + b


# add("a=5", 10)
add(5, 10)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def print_name(p: Person):
    print(p.name)


p = Person("John", 30)
p2 = Person("abc", 10)
print(print_name(p2))


def abc(a: list[list[int]]):
    print(a)


# abc([1, 2, "3"])
abc([[1, 2], [3], [4]])


def print_dict(dict_val):
    for key, value in dict_val.items():
        print(f"{key}: {value}")


dect_val: dict[int, str] = {1: "hey", 2: "hello", 3: "hi"}

set_val: set[int] = {1, 2, 3, 4, 5}


#  inheritance..

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


def print_area(shape: Union[Circle, Rectangle]):
    print(f"Area: {shape.area()}")


circle = Circle(5)
rectangle_v = Rectangle(4, 5)
print_area(circle)
print_area(rectangle_v)


def test(a: int, b: Optional[int] = None):
    print(a)
    if b is not None:
        print(b)


test(1, 2)

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, list_values: Optional[list[T]] = None):
        self.items: list[T] = list_values if list_values is not None else []

    def push(self, item: T) -> None:
        self.items.append(item)


stackInt = Stack[str](["1", "2"])

stackInt.push("2")




class Animal:
    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says Meow!"

def animal_sound(animal):
    print(animal.speak())


class peacock(Animal):
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says xyz..!"


dog = Dog("Buddy")
print(dog.speak())

peacock = peacock("Buddy")

animal_sound(peacock)


def add(x):
    print(x+1)

add(1)
add(3.14)
add(True)

add("abc")