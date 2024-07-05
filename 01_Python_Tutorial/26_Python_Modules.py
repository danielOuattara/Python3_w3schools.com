# !bin/bash
# Daniel OUATTARA
# 27 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

import my_module
import my_module2 as my_mod2
import platform
from my_module3 import person1


print(70 * '-')

""" 
Python Modules
===============

Consider a module to be the same as a code library:
a file containing a set of class(es), function(s) 
or property(ies) you want to include in your application.


Create a Module
================

To create a module just save the code you want in a 
file with the file extension .py:

Example: Save this code in a file named my_module.py
 
"""

# def greeting(name):
#     print("Hello, " + name)


""" 
Use a Module
==============

Now we can use the module we just created, by using 
the import statement:

Example: Import the module named my_module, and call 
         the greeting function:
         
"""

# import my_module

my_module.greeting("Jonathan")

""" 

Note: When using a function from a module, use the 
syntax: module_name.function_name.


Variables in Module
=====================

The module can contain functions, as already described, 
but also variables of all types (arrays, dictionaries, 
objects etc):

Example: 
1)  Save this code in the file my_module.py 
"""
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

"""
2) Import the module named my_module, and access 
the person1 dictionary:"""

# import my_module

a = my_module.person1["age"]
print(a)

print(70 * '-')

""" 

Naming a Module
=================

You can name the module file whatever you like, but it 
must have the file extension .py


Re-naming a Module
====================

You can create an alias when you import a module, by 
using the 'as' keyword:

Example: Create an alias for my_module called my_mod: 

"""

#  import my_module as my_mod

a = my_mod2.person1["age"]
print(a)

print(70 * '-')


""" 
Built-in Modules
==================

There are several built-in modules in Python that you 
can import whenever you need.

Example: Import and use the platform module:"""

# import platform

x = platform.system()
print(x)

print(70 * '-')


"""
Using the dir() Function
==========================

There is a built-in function to list all the function names, 
or variable names in a module: the dir() function:

Example: List all the defined names belonging to the 
         platform module:
"""

#  import platform

x = dir(platform)
print(x)

print(70 * '-')


""" 
Note: The dir() function can be used on all modules, also 
the ones you create yourself.


Import From Module
====================

You can choose to import only parts from a module, by using 
the from keyword.

Example: The module named my_module has one function and one 
         dictionary: 

"""

# def greeting(name):
#   print("Hello, " + name)
#
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

""" 
Import only the person1 dictionary from the module:
"""

#  from my_module import person1

print(person1["age"])

print(70 * '-')

"""

Note: When importing using the from keyword, do not use 
the module name when referring to elements in the module.
 
Example: person1["age"], not my_module.person1["age"]

"""
