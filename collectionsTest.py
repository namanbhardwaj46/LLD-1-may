

a = [0]
a[0] = 1

a[0] = 2


import copy

b = copy.copy(a)

a[0] = 3
print(b[0])  # Output: 2


class Attendance:
    def __init__(self):
        self.Present = True

    def __str__(self):
        return f"Attendance: {self.Present}"

class person:
    def __init__(self, name):
        self.name = name
        self.Attendance = Attendance()
        self.age = 1
    def __str__(self):
        return f"Person: {self.name}"



p1 = person("John")

p2 = copy.deepcopy(p1)

print(p1.Attendance.Present)
print(p1.age)


print(p2.Attendance.Present)
print(p2.age)
p1.Attendance.Present = False

print(p1.Attendance.Present)

print(p2.Attendance.Present)

p1.age = 2
print(p1.age)
print(p2.age)


arr = [1, 2, 3, 4, 5]

arr2 = arr[:]
arr2[0] = 10

print(arr)
print(arr2)


arr = [[1, 2], [3, 4], [5, 6]]
arr2 = copy.deepcopy(arr)
arr2[0][0] = 10
print(arr)
print(arr2)

s1 = set()
s3 = {1, 2, 3, 4, 5, 5}

print(s3)

#  dict

d1 = {"a": 1, "b": 2, "c": 3}

#  tuple: immutable
t1 = (1, 2, 3, 4, 5)

# t1[0] = 10


d1 = {}
# print(d1["a"])

from collections import defaultdict

dd = defaultdict(int)
print(dd[122])

from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)

d.appendleft(0)
print(d)

print(d.pop())
print(d.popleft())


# counter

from collections import Counter
c = Counter("hello world")
print(c)

print(c.most_common())

#  NamedTuple

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)

print(p.x)
print(p.y)

print(p)






fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits, 2):
    print(i, fruit)


i = 2
for fruit in fruits:
    print(i, fruit)
    i += 1


print(list(enumerate(fruits)))