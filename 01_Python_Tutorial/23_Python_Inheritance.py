# bin/bash !
# Daniel OUATTARA
# 25 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

print(70 * '-', "1")

"""
Python Inheritance
====================

Inheritance allows us to define a class that inherits
all the methods and properties from another class.

Parent class is the class being inherited from, also
called 'base class'.

Child class is the class that inherits from another
class, also called 'derived class'.


Create a Parent Class
========================

Any class can be a parent class, so the syntax is the
same as creating any other class:

Example: Create a class named Person, with f_name and
         l_name properties, and a print_name method:

"""


class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def print_name(self):
        print(f'{self.f_name} {self.l_name}')


""" 
Use the Person class to create an object, and then execute 
the print_name method:
"""

john = Person("John", "Doe")
john.print_name()

print(70 * '-', "2")

""" 
Create a Child Class
=========================

To create a class that inherits the functionalities from 
another class, send the parent class as a parameter when 
creating the child class:

Example: Create a class named Student, which will inherit 
         the properties and methods from the Person class: 
"""


class Student(Person):
    pass


""" 
Note: Use the 'pass' keyword when you do not want to add 
      any other properties or methods to the class.

Now the Student class has the same properties and methods 
as the Person class.

Example: Use the Student class to create an object, and 
         then execute the print_name method: 
"""

anna = Student("Anna", "Olsen")
anna.print_name()

print(70 * '-', "3")

""" 
Add the __init__() Function
================================

So far we have created a child class that inherits the 
properties and methods from its parent.

We want to add the __init__() function to the child class, 
instead of the pass keyword.

Note: The __init__() function is called automatically every 
      time the class is being used to create a new object.

Example: Add the __init__() function to the Student class: 
"""


class Student(Person):
    def __init__(self, f_name, l_name):
        pass


""" 
When you add the __init__() function, the child class will 
no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance
      of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, 
add a call to the parent's __init__() function:

Example 
"""


class Student(Person):
    def __init__(self, f_name, l_name, age, country):
        Person.__init__(self, f_name, l_name)
        self.age = age
        self.country = country

    def country_name(self):
        print(self.country)


john = Student('John', 'Doe', 35, 'Norway')
print(john.l_name)
print(john.age)
print(john.country)
john.country_name()  # self method
john.print_name()  # parent's method

print(70 * '-', "4")

""" 
We successfully added the __init__() function in the child 
class and also kept the inheritance from the parent class. 
Now, we are ready to add functionality in the __init__() 
function.


Use the super() Function
===============================

Python also has a super() function that will make the child 
class inherit all the methods and properties from its parent:
Example:"""


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


""" 
By using the super() function, you do not have to use the name 
of the parent element: it will automatically inherit the methods 
and properties from its parent.


Add Properties
===================

Example : Add a property called 'graduation_year' to the 
Student class: 
"""


class Student(Person):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.graduation_year = 2019


""" 
In the example above, the year 2019 should be a variable, and 
be passed into the Student class when creating student objects. 

To do so, add another parameter in the __init__() function:

Example: Add a year parameter, and pass the correct year when 
         creating objects:
"""


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year


x = Student("Mike", "Olsen", 2019)
print("graduation_year = ", x.year)
print(70 * '-', "5")

""" 
Add Methods
================

Example: Add a method called 'welcome' to the Student class:
"""


class Student(Person):
    def __init__(self, f_name, l_name, year):
        super().__init__(f_name, l_name)
        self.graduation_year = year

    def welcome(self):
        print(f'Welcome {self.f_name} {self.l_name} to the class of {self.graduation_year}')


john = Student('John', 'Doe', 2009)
print(john.welcome())

print(70 * '-', "6")

""" 
NOTE: If you add a method in the child class with the same name 
      as a method in the parent class, the inheritance from the 
      parent method will be overridden (lost).  
"""
