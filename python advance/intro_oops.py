person_1_name = "karan"
person_1_age = 23
person_1_psp = 30


def print_person(name, age, sp):
    print("Hello " + name + "!")
    print("Your age is " + str(age) + "!")
    print("Your sp is " + str(sp) + "!")


person_2 = "abc"
person_2_age = 23
person_2_classes = 30


def print_instructor(name, age, classes):
    print("Hello " + name + "!")
    print("Your age is " + str(age) + "!")
    print("Your classes are " + str(classes) + "!")


print_person(person_2, person_2_age, person_1_psp)
print_instructor(person_2, person_1_age, person_2_classes)


class Student:
    def __init__(self, name, psp):
        self.name = name
        self.psp = psp
        self._email = "abc@gmail.com"
        self.__age = 30  #private

    def print_name(self):
        print("Hello " + self.name + "!")

    def print_age(self):
        print("Your age is " + str(self.__age) + "!")


karan = Student("karan", 30)
naman = Student("naman", 30)

karan.print_name()
naman.print_name()

# public access modifier

print(karan.name)
karan.print_age()
print(karan._email)
print(karan._Student__age) #name Mangling
