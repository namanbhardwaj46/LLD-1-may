# from typing import Any, Union, Optional
# from typing import Generic, TypeVar
#
# # a: int = 5
#
# # print(a+10)
# #
# # a = "abc"
# # print(a+9)
#
# # Method
#
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# add(5,10)
#
#
# class Person:
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name}"
#
#
# def print_name(p:Person) -> str:
#     return p.name
#
#
# p = Person("John", 30)
# p2 = Person("Naman", 10)
# # print(print_name(p2))
#
#
# def abc(a: list[list[int]]):
#         print(a)
#
# # abc([1, 2, "3"])
# # abc([[1, 2], [3], [4]])
#
#
# def print_dict(dict_val):
#     for key, value in dict_val.items():
#         print(f"{key}: {value}")
#
# dect_val: dict[int, str] = {1: "a", 2: "hello", 3: "hi"}
#
#
# set_val: set[int] = {1, 2, 3, 4, 5}
#
#
#
#
# # inheritance..
#
# class Shape:
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def area(self) -> float:
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height
#
#     def area(self) -> float:
#         return self.width * self.height
#
# def print_area(shape: Union[Circle, Rectangle]):    # We can pass parameter as shape: Shape or Union[Circle, Rectangle]
#                                                     # In python3.10 they introduced pipe operator to represent union type.
#                                                     # Like Circle | Rectangle
#     print(f"Area: {shape.area()}")
#
# # circle = Circle(5)
# # rectangle = Rectangle(4, 5)
# # print_area(circle)
# # print_area(rectangle)
#
#
# def test(a: int, b: Optional[int]=None):
#     print(a)
#     if b is not None:
#         print(b)
#
# # test(1, 2)
#
#
# T = TypeVar('T')
#
# class Stack(Generic[T]):
#     def __init__(self, list_values: Optional[list[T]] = None):
#         self.items: list[T] = list_values if list_values is not None else []
#
#     def push(self, item: T) -> None:
#         self.items.append(item)
#
# stackInt = Stack[str](["1", "2"])
#
# stackInt.push("2")


# from typing import TypeVar, Callable
#
# T = TypeVar('T')
#
# def compare(x: T, y: T, key: Callable[[T], any] = None) -> int:
#     """
#     Compare two objects of the same type.
#
#     Args:
#         x (T): The first object to compare.
#         y (T): The second object to compare.
#         key (Callable[[T], any], optional): A function to extract a key from each object for comparison.
#             Defaults to None, which means direct comparison of objects.
#
#     Returns:
#         int: -1 if x < y, 0 if x == y, 1 if x > y.
#     """
#     if key is not None:
#         # todo
#         if key(x) < key(y):
#             return -1
#         elif key(x) == key(y):
#             return 0
#         elif key(x) > key(y):
#             return 1
#
#     else:
#         #todo
#         if x < y:
#             return -1
#         elif x == y:
#             return 0
#         elif x > y:
#             return 1
#
#
# # Example usage:
#
# # Direct comparison
# print(compare(5, 10))  # Output: -1
# print(compare("abc", "abc"))  # Output: 0
# print(compare(20, 10))  # Output: 1
#
#
# # Comparison with key function
# students = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 20}
# ]
#
# # print(compare(students[0], students[1], key=lambda student: student['age']))
# # print(compare(students[0], students[2], key=lambda student: student['age']))
#
# # Sort students by age
# sorted_students = sorted(students, key=lambda x: x['age'])
# print(sorted_students)  # Output: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]


# from typing import TypeVar, Generic
#
# T = TypeVar('T')
#
# class Node(Generic[T]):
#     def __init__(self, data: T):
#         #todo
#         self.data: T = data # the value stored in this node
#         self.next = None    # link to next node (None if last)
#
# class LinkedList(Generic[T]):
#     def __init__(self):
#         #todo
#         self.head = None    # start of the list
#         self.tail = None    # end of the list
#
#     def append(self, data: T):
#         #todo
#         """
#         Add a new node with the given data to the end of the list.
#         """
#         new_node = Node(data)
#         if not self.head:
#             # If list is empty, new node is both head and tail
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # Otherwise, link it after tail and update tail
#             self.tail.next = new_node
#             self.tail = new_node
#
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")
#
# # Example usage:
#
# # Create a linked list of integers
# ll_int = LinkedList[int]()
# ll_int.append(1)
# ll_int.append(2)
# ll_int.append(3)
# ll_int.print_list()  # Output: 1 -> 2 -> 3 -> None
#
# # Create a linked list of strings
# ll_str = LinkedList[str]()
# ll_str.append("a")
# ll_str.append("b")
# ll_str.append("c")
# ll_str.print_list()  # Output: a -> b -> c -> None

from typing import TypeVar

# TODO: Declare two type variables `T` and `U`.
T = TypeVar('T')
U = TypeVar('U')

class Pair:
    #TODO: Implement the constructor to initialize the two pair values
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    # TODO: Implement this method to return the string representation of the pair as shown in the readme
    def __repr__(self):
        return f"Pair({self.first}, {self.second})"


# Example usage:

# Create a pair of integers and strings
pair1 = Pair(1, "apple")
print(pair1)  # Output: Pair(1, apple)

# Create a pair of float and list
pair2 = Pair(3.14, [1, 2, 3])
print(pair2)  # Output: Pair(3.14, [1, 2, 3])

# Create a pair of tuple and dictionary
pair3 = Pair((1, 2), {"a": 1, "b": 2})
print(pair3)  # Output: Pair((1, 2), {'a': 1, 'b': 2})
