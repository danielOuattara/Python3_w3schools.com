# bin/bash !
# Daniel OUATTARA
# 25 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

""" Python Classes/Objects
=========================

Python is an object-oriented programming language.
Almost everything in Python is an object, with its
properties and methods.

A Class is an object constructor, a "blueprint"
for creating objects.


Create a Class
===================

To create a class, use the keyword 'class':

Example: Create a class named 'MyClass', with a
property named x and msg: """

print(70 * '-', "1")


class MyClass:
    x = 5
    msg = "Hello"


""" Create Object
=================

Now we can use the class named 'MyClass' to create 
objects:

Example: Create an object named 'object_1', and 
print the value of x: """

object_1 = MyClass()
print(object_1.x)
print(object_1.msg)

print(70 * '-', "2")

""" The __init__() Function
============================

The examples above are classes and objects in their simplest 
form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand 
the built-in __init__() function.

All classes have a function called __init__(), which is 
always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is 
being created:

Example: Create a class named Person, use the __init__() function 
to assign values for name and age: """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John Doe", 36)

print(john.name)
print(john.age)

print(70 * '-', "3")

"""
Note: The __init__() function is called automatically 
every time the class is being used to create a new object.

The __str__() Function
=======================

The __str__() function controls what should be returned 
when the class object is represented as a string.

If the __str__() function is not set, the memory address 
of the object is returned:

Example: The string representation of an object WITHOUT 
the __str__() function """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)
print(70 * '-', "3-BIS")

"""
Example: The string representation of an object WITH 
the __str__() function:"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'


p1 = Person("John", 36)

print(p1)
print(70 * '-', "3-TER")

""" Object Methods
===================

Objects can also contain methods. Methods in objects are 
functions that belong to the object.

Let us create a method in the Person class:

Example: Insert a function that prints a greeting, and execute 
it on the 'john' object: """


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self, country):
        print("Hello my name is " + self.name, "I have", self.age, "y.o \nI came from " + country)


john = Person("John", 36)
john.greetings("Philippines")

print(70 * '-', "4")

""" The self Parameter
=======================

The 'self' parameter is a reference to the current instance 
of the class, and is used to access variables that belongs 
to the class.

It does not have to be named self, you can call it whatever 
you like, but it has to be the first parameter of any function 
in the class.

Example: Use the words mysillyobject and abc instead of self:"""


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()

print(70 * '-', "5")

""" Modify Object Properties
===============================

You can modify properties on objects like this:

Example: Set the age of 'john' to 40:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print("Hello my name is " + self.name, "I have", self.age, "y.o")


john = Person("John", 36)
john.greetings()

john.age = 40
john.greetings()
print(70 * '-', "6")

""" Delete Object Properties
==============================

You can delete properties on objects by using the 'del' keyword:

Example: Delete the 'age' property from 'john' object: 
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print("Hello my name is " + self.name, "I have", self.age, "y.o")


john = Person("John", 36)
john.age = 40
john.greetings()

del john.age  # deleting 'age' property

try:
    john.greetings()
except:
    print("Caution: No property 'age' found with John ")

print(70 * '-', "7")


""" Delete Objects
=====================

You can delete objects by using the 'del' keyword:

Example: Delete 'john' object:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 36)
print('John Doe is', john, 'y.o')

del john  # deleting John instance

try:
    print('John Doe is', john, 'y.o')
except:
    print('Caution: \'john\' object does not exist ')

print(70 * '-', "8")


""" The pass Statement
========================

Class definitions cannot be empty, but if you for some reason 
have a class definition with no content, put in the 'pass' 
statement to avoid getting an error.

Example: 
"""


class Person:
    pass
