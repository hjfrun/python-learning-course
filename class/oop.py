# Object Orientated Programming in Python

# x = 1
# print(type(x))


# str = "hello"

# print(str.upper())

# class Dog:
#     def bark(self):
#         print("bark")


# d = Dog()
# print(type(d))

# d.bark()


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old.")

#     def speak(self):
#         print("I don't know what I say.")


# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print("Meow")

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


# class Dog(Pet):
#     def speak(self):
#         print("Bark")


# class Fish(Pet):
#     pass


# p = Pet("Tim", 19)
# p.show()
# p.speak()
# c = Cat("Bill", 34, "green")
# c.show()

# d = Dog("Jill", 25)
# d.show()

# c.speak()
# d.speak()

# f = Fish("Bubble", 10)
# f.speak()


# class Person:
#     number_of_people = 0

#     def __init__(self, name):
#         self.name = name
#         # Person.number_of_people += 1
#         Person.add_person()

#     @classmethod
#     def number_of_person(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1


# p1 = Person("tim")
# print(Person.number_of_people)
# p2 = Person("jill")
# print(Person.number_of_people)
# print(Person.number_of_person())

# print(p1.number_of_people)
# print(Person.number_of_people)
# Person.number_of_people = 9
# print(p2.number_of_people)


class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def mul5(x):
        return x * 5

    @staticmethod
    def pr():
        print("run")


print(Math.add5(10))
print(Math.mul5(2))
Math.pr()
