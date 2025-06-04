# single inheritance

class Parent:
    def __init__(self):
        print("Parent Constructor")
        self.eyes = 2

    def speak(self):
        print("Parent Speak")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
        self.age = 10

    def speak(self):
        print("Child Speak")


# c = Child()
# print(c.eyes)
# c.speak()


# Multiple inheritance


class Parent1:
    def __init__(self):
        print("Parent1 Constructor")
        super().__init__()
        self.eyes = 2

    def func1(self):
        print("Parent1 Func1")

    def func2(self):
        print("Parent1 Func2")


class Parent2:
    def __init__(self):
        print("Parent2 Constructor")
        self.name = "parent2"

    def func2(self):
        print("Parent2 Func2")

    def a(self):
        print("Parent2 A")


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child Constructor")


c = Child()


print(Child.mro())
Parent2.func2(c)

# Hirarchy

class parent:
    def __init__(self):
        pass

    def p1(self):
        print("Parent 1")


class child1(parent):
    def __init__(self):
        super().__init__()

    def func1_child1(self):
        print("Parent1 Func1")


class child2(parent):
    def __init__(self):
        super().__init__()

        print("Child2 Constructor")


c = child1()
c.p1()
c.func1_child1()

c2 = child2()
c2.p1()
# c2.func1_child1()

# TODO: HW:  hydbird... multilevel...


