# bin/bash !
# Daniel OUATTARA
# 13 03 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
Python Variables
================

Creating Variables
------------------
Variables are containers for storing data values.
Python has no command for declaring a variable.
A variable is created the moment you first assign
a value to it.
"""

x = 5
first_name = "John"
last_name = 'Johnson'

"""
Variables do not need to be declared with any particular 
type and can even change type after they have been set.
"""

x = 4  # x is of type 'int'
x = "Sally"  # x is now of type 'str'
print(x)

""" 
String variables can be declared either by using single or double 
quotes: 
"""

x = "John"
# is the same as
x = 'John'

"""
Casting
-------
If you want to specify the data type of a variable, this can be 
done with casting.
"""
x = str(3)  # --> x = "3"
y = int(3)  # --> y = 3
z = float(3)  # --> z = 3.0

"""
Get the Type
-------------
You can get the data type of a variable with the type() function.
"""

x = 5
y = "John"
print(type(x))  # 'int'
print(type(y))  # 'str'

"""
Variable Names
==================

A variable can have a short name (like x and y) or a more descriptive 
name (age, carName, total_volume). Rules for Python variables:

    A variable name :
        >  must start with a letter or the underscore character
        >  cannot start with a number nor contain space
        >  can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        >  are case-sensitive (age, Age and AGE are three different variables)
"""

#  Legal variable names:

myvar = "John"
myVariable = "John"  # Camel Case
MyVariable = "John"  # Pascal Case
my_variables_name = "John"  # Snake Case
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
#Illegal variable names:
"""

#  2myvar = "John"
#  my-var = "John"
#  my var = "John"

"""
Note: Remember that variable names are case-sensitive
-----


Assign Value to Multiple Variables
------------------------------------
Python allows you to assign values to multiple variables 
in one line:
"""

x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry

"""
And you can assign the same value to multiple variables 
in one line:
"""

x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange

"""
Unpack a collection (destructuring like in JavaScript)
------------------------------------------------------
If you have a collection of values in a list, tuple etc..., 
Python allows you extract the values into variables. 
This is called unpacking.

"""

fruits = ["apple", "banana", "melon"]

x, y, z = fruits

print(x)
print(y)
print(z)

vegetables = ("tomato", "onion", "eggplants", "radish")

#  x, y, z = vegetables #  ValueError : too many values to unpack

"""
Output Variables
-----------------
The Python 'print' statement is often used to output variables.
To combine both text and a variable, Python uses the '+' or  ',' 
character:
"""

x = "awesome"
print("Python is " + x)  # Python is awesome

y = "super"
print(x, y)  # awesome super

"""
You can also use the + character to add a variable to another variable:
"""

x = "Python is "
y = "awesome"
z = x + y
print(z)  # Python is awesome

"""
For numbers, the + character works as a mathematical operator:
"""

x = 5
y = 10
print(x + y)  # 15

"""
If you try to combine a string and a number, Python will raise an error:
"""

x = 5
y = "John"
#  print(x + y)  # Will raise an error
#  print(x, y)  # OK

# solution =
print(x, y)

"""
Global Variables
------------------
Variables that are created outside of a function are known as 
'global variables'.

Global variables can be used by everyone, both inside of functions 
and outside.

Create a variable outside of a function, and use it inside that function
"""

x = "great and easy to learn"


def my_func():
    print("Python is " + x)


my_func()  # Python is great and easy to learn

"""
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 

The global variable with the same name will remain as it was. 
(global and with the original value)

Create a variable inside a function, with the same name as the global 
variable
"""

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()  # Python is fantastic

print("Python is " + x)  # Python is awesome

"""
The global Keyword
-------------------

Normally, when you create a variable inside a function, that variable 
is local, and can only be used inside that function.

To create a global variable inside a function, you can use the 'global' 
keyword. Now that variable belongs to the global scope:
"""


def myfunc():
    global name
    name = " is sweety !"
    print(name)


myfunc()

print("Python is " + name)

"""
Also, use the "global" keyword if you want to change a global variable 
inside a function.

To change the value of a global variable inside a function, refer to 
the variable by using the global keyword:
"""

y = "awesome"


def myfunc():
    global y
    y = "fantastic"


myfunc()

print("Python is " + y)

#  =================================================

'''Creating Variables
----------------------'''
x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#  Assign Value to Multiple Variables
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)
print(x, y, y)

#  Assign the same value to Multiple Variables
a = b = c = "orange"

print(a, b, c)

# Output Variables
x = 'awesome'
print('Python is', x)
print('Python is' + x)

z = 5
k = 2
print("z + k =", z + k)

z, k = 5, 2
print("z + k =", z + k)

# Global Variables

x = "awesome"  # Global variable


def myfunc():
    print("Python is", x)
    print("Python is " + x)


myfunc()

x = "awesome"


def myfunc2():
    x = "fantastic"
    print("Python is", x)
    print("Python is " + x)


myfunc2()


# The global Keyword

def myfunc3():
    global middle_name  # creates a variable accessible outside its native function
    middle_name = "Pierre"


myfunc3()

print("Python is", middle_name)

x = " genial"


def myfunc4():
    global x
    x = "superette"


myfunc4()

print("python is", x)
