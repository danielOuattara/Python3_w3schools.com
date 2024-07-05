# !bin/bash
# Daniel OUATTARA
# 27 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

print(70 * '-')

""" 
Python Scope
====================

A variable is only available from inside the region
it is created: this region is called a scope.

Local Scope
============

A variable created inside a function belongs to the 
local scope of that function, and can only be used 
inside that function.

Example: A variable created inside a function is 
         available inside that function:
         
"""


def my_func():
    x = 300
    print(x)


my_func()

print(70 * '-')


""" 

Function Inside Function
==============================

As explained in the example above, the variable x is not 
available outside the function, but it is available for 
any function inside the function:

Example: The local variable can be accessed from a function 
        within the function: 

"""


def my_func():
    x = 400

    def my_inner_func():
        print(x)

    my_inner_func()


my_func()

print(70 * '-')


""" 

Global Scope
==================

A variable created in the main body of the Python code 
is a global variable and belongs to the global scope.

Global variables are available from within any scope, 
global and local.

Example: A variable created outside of a function is 
         global and can be used by anyone: 
         
"""

x = 500


def my_func():
    print(x)


my_func()

print(x)

print(70 * '-')


""" 

Naming Variables
==================

If you operate with the same variable name inside 
and outside of a function, Python will treat them 
as two separate variables, one available in the 
global scope (outside the function) and one 
available in the local scope (inside the function):

Example: The function will print the local x, and 
         then the code will print the global x: 

"""

x = 600


def my_func():
    x = 700
    print(x)


my_func()

print(x)

print(70 * '-')


""" 

Global Keyword
=====================

If you need to create a global variable, but you
are stuck in the local scope, you can use the global 
keyword. The global keyword makes the variable global.

Example: If you use the global keyword, the variable 
         belongs to the global scope: 

"""


def my_func():
    global x
    x = 800


my_func()

print(x)

print(70 * '-')

"""
Also, use the global keyword if you want to make a 
change to a global variable inside a function.

Example: To change the value of a global variable inside 
         a function, refer to the variable by using the 
         global keyword: 
"""

x = 900


def my_func():
    global x
    x += 200


my_func()
print(x)

my_func()
print(x)

print(70 * '-')

