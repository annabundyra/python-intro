# import abc
"""
EXERCISE 1  --> CREATE & INSTANTIATE A CLASS
"""


# class Cat:

#     def __init__(self):
#         pass


# jake = Cat()
# print(jake)

# Add Attrubutes to a class
# class Cat:

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed


# jake = Cat(name="Jake", age=2, breed="Persian")
# print(f"{jake.name}, is {jake.age} years old, and is a {jake.breed} breed.")

#  Add a method to a class
# class Cat:

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def meow(self):
#         print("Meow")

#     def get_info(self):
#         print(f"{self.name}, is {self.age} years old, and is a {self.breed} breed.")


# jake = Cat(name="Jake", age=2, breed="Persian")
# # print(f"{jake.name}, is {jake.age} years old, and is a {jake.breed} breed.")
# jake.meow()
# jake.get_info()

# # # create more new objects
# pippa = Cat('Pippa', 3, 'Bengal')
# snowy = Cat('Snowy', 8, 'Siamese')
# sparky = Cat('Sparky', 2, 'Ragdoll')

# pippa.get_info()
# snowy.get_info()
# sparky.get_info()

#  Assign new value to the attribute in a class

# class Cat:

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def meow(self):
#         print("Meow")

#     def get_info(self):
#         print(f"{self.name}, is {self.age} years old, and is a {self.breed} breed.")

#     def birthday(self):
#         self.age += 1


# jake = Cat(name="Jake", age=2, breed="Persian")
# jake.get_info()
# jake.birthday()
# jake.get_info()

#  passing arguments to a method
# class Cat:

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def meow(self):
#         print("Meow")

#     def get_info(self):
#         print(f"{self.name}, is {self.age} years old, and is a {self.breed} breed.")

#     def birthday(self):
#         self.age = self.age + 1

#     def set_friend(self, friend):
#         """
#         link a friend to this cat and the cat to its friend
#         """
#         self.friend = friend
#         friend.friend = self


# snowy = Cat(name="Snowy", age=8, breed="Siamese")
# sparky = Cat(name="Sparky", age=2, breed="Ragdoll")
# jake = Cat(name="jake", age=2, breed="tabby")

# snowy.set_friend(sparky)

# print(snowy.friend.name)
# print(sparky.friend.name)

# snowy.set_friend(jake)
# print(snowy.friend.name)

"""
EXERCISE 2  --> INHERIT FROM A CLASS
"""


# class Vehicle:
#     def vehicle_method(self):
#         print("This is parent Vehicle class method")

# # create a child class that inherits from the parent class Vehicle


# class Car(Vehicle):
#     def car_method(self):
#         print("This is child Car class method")


# # car_a = Car()
# # car_a.vehicle_method()

# #  multiple children of one parent class
# class Cycle(Vehicle):
#     def cycle_method(self):
#         print("This is child Cycle class method")


# car_b = Cycle()
# car_b.cycle_method()

# #  multiple parents
# class Camera:
#     def camera_method(self):
#         print("This is parent Camera class")


# class Radio:
#     def radio_method(self):
#         print("This is parent Radio class method")


# class MobilePhone(Camera, Radio):
#     def mobile_phone_method(self):
#         print("This is child MobilePhone class method")


# cell_phone_a = MobilePhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()
# cell_phone_a.mobile_phone_method()
"""
POLYMORPHISM

In OOP polymorphism refers to the ability of an object to behave in multiple ways.
It is implemented via method-overloading and method overriding.

"""

# METHOD OVERRIDING - a method with the same name in the child class as in the parent class.
# The definition of the method differs in parent and child classes but the name remains the same.


# class Vehicle:
#     def print_details(self):
#         print("This is parent Vehicle class method")


# class Car(Vehicle):
#     def print_details(self):
#         print("This is child Car class method")


# class Cycle(Vehicle):
#     def print_details(self):
#         print("This is child Cycle class method")


# car_a = Vehicle()
# car_a. print_details()

# car_b = Car()
# car_b.print_details()

# car_c = Cycle()
# car_c.print_details()


# # METHOD OVERLOADING - the property of a method to behave in different ways,
# # depending upon the number or types of the parameters.
#

# class Car:

#     def start(self, a, b=None):
#         if b is not None:
#             print(a + b)
#         else:
#             print(a)


# car_x = Car()
# car_x.start(10)

"""
class OverloadingExample{  
static int add(int a,int b){return a+b;}  
static int add(int a,int b,int c){return a+b+c;}  
}  
"""


"""
ENCAPSULATION

It refers to data hiding. In OOP one class should not have direct access to the data of the other class.
"""


# class Car:

#     def __init__(self, model):
#         # initialize instance variables
#         self.model = model

#     # creats a model property
#     @property
#     def model(self):
#         return self._model

#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self._model = 2000
#         elif model > 2021 and model < 2030:
#             self._model = 2021
#         else:
#             self._model = model

#     def getCarModel(self):
#         return f"The car model is {self.model}"


# mycar = Car(2033)
# print(mycar.getCarModel())


"""
ABSTRACTION
"""

"""
STATIC & CLASS METHODS

Class methods are used for factory purposes, in the below code @classmethod details() is used to create a class object from a birth year instead of age. 
Static methods are utility functions and work on data provided to them in arguments (NOTE: no 'self' passed in).
"""

#  OLD WAY
# class Shape(object):
#     def calc_perimeter(self):
#         raise NotImplementedError("Please Implement this method!")


# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def calc_perimeter(self):
#         return self.a + self.b + self.c


# t = Triangle(2, 4, 6)
# print(t.calc_perimeter())

#  NEW WAY


# import abc
# class Shape1(object):
#     __metaclass__ = abc.ABCMeta

#     @abc.abstractmethod
#     def calc_perimeter(self, input):
#         """method documentaiton"""
#         return


# class Triangle1(Shape1):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def calc_perimeter(self):
#         return self.a + self.b + self.c


# t1 = Triangle1(2, 4, 6)
# print(t1.calc_perimeter())


"""
STATIC & CLASS METHODS

Class methods are used for factory purposes, in the below code @classmethod details() is used to create a class object from a birth year instead of age. 
Static methods are utility functions and work on data provided to them in arguments (NOTE: no 'self' passed in).
"""




from datetime import date
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def details(cls, first_name, last_name, year):
        return cls(first_name, last_name, date.today().year - year)

    @staticmethod
    def check_age(age):
        return age > 18


person1 = Person("John", "Doe", 30)
person2 = Person.details("Jane", "Doe",  1992)

print(person1.first_name, person1.age)
print(person2.first_name, person2.age)

print(Person.check_age(33))
