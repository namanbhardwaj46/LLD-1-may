import collections

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#
# def sort_students(students):
#     # TODO: Implement the sorting logic here
#     # You need to sort the students list based on the requirements:
#     # 1. Sort by marks in ascending order
#     # 2. If marks are the same, sort by name in alphabetical order
#     return sorted(students, key=lambda x: (x.marks, x.name))
#
#
# # Example usage:
# student1 = Student("Alice", 85)
# student2 = Student("Bob", 75)
# student3 = Student("Charlie", 85)
# student4 = Student("David", 90)
#
# students = [student1, student2, student3, student4]
#
# sorted_students = sort_students(students)
# for student in sorted_students:
#     print(f"Name: {student.name}, Marks: {student.marks}")




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def find_unique_persons(people):
#     # TODO: Implement the logic to find unique persons based on their names.
#     # If there are multiple persons with the same name, only include the first
#     # person encountered with that name in the returned list.
#     seen_names = {}
#     unique_persons = []
#     for person in people:
#         if person.name not in seen_names:
#             seen_names[person.name] = True
#             unique_persons.append(person)
#     return unique_persons
#
# # Example usage:
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)
# person3 = Person("Alice", 35)
# person4 = Person("Charlie", 40)
#
# people = [person1, person2, person3, person4]
#
# unique_persons = find_unique_persons(people)
# for person in unique_persons:
#     print(f"Name: {person.name}, Age: {person.age}")


# # TODO: Implement the function below to count the frequency of each integer
# def count_frequency(arr):
#     dict = {}
#     for i in arr:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#     return dict
#
#
# # Example usage:
# arr = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
# frequency = count_frequency(arr)
# print(frequency) # Output: {1: 4, 2: 3, 3: 2, 4: 1}



from collections import defaultdict

# TODO: Complete the given function
def group_anagrams(strs):
    anagrams = defaultdict(list)
    # Complete the code
    for s in strs:
        # Sort each string to create a key - anagrams will have the same sorted string
        sorted_s = ''.join(sorted(s))
        # Add the original string to the list for this key
        anagrams[sorted_s].append(s)

    # Return the values (lists of anagrams)
    return list(anagrams.values())

# Example usage
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strings))