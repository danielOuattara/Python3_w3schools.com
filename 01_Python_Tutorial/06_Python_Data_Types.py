# bin/bash !
# Daniel OUATTARA
# 13 03 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


""" Python Data Types
---------------------

Variables can store data of different types that can do 
different things.

Python has the following data types built-ins by default,
in these categories:

Built-in Data Types
====================

Text Type:	      str
---------

Numeric Types:    int, float, complex
-------------

Sequence Types:   list, tuple, range
--------------

Mapping Type:     dict
------------

Set Types:        set, frozenset
---------

Boolean Type:     bool
------------

Binary Types:     bytes, bytearray, memoryview
------------
"""

# Getting the Data Type
x = 5
print("type of x =", type(x))  # x = <class 'int'>

"""
 Setting the Data Type
-----------------------
In Python, the data type of a variable is set automatically 
when you assign a value to a variable:

"""
x = "Hello World"  # str
x = 20  # int
x = 20.599  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = dict(name="John", age=36)  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview

"""
 Setting the Specific Data Type
--------------------------------
If you want to specify the data type, you can use the following 
constructor functions:

"""
x = str("Hello World")
print(x, ':', type(x))  # str

x = int(20)
print(x, ':', type(x))  # int

x = float(20.5)
print(x, ':', type(x))  # float

x = complex(1j)
print(x, ':', type(x))  # complex

x = list(("apple", "banana", "cherry"))
print(x, ':', type(x))  # list

x = tuple(("apple", "banana", "cherry"))
print(x, ':', type(x))  # tuple

x = range(6)
print(x, ':', type(x))  # range

x = dict(name="John", age=36)
print(x, ':', type(x))  # dict

x = set(("apple", "banana", "cherry"))
print(x, ':', type(x))  # set

x = frozenset(("apple", "banana", "cherry"))
print(x, ':', type(x))  # frozenset

x = bool(5)
print(x, ':', type(x))  # bool

x = bytes(5)
print(x, ':', type(x))  # bytes

x = bytearray(5)  # bytearray
print(x, ':', type(x))

x = memoryview(bytes(5))
print(x, ':', type(x))  # memoryview


#  Setting the Specific Data Type

x = str("Hello World")  # str
x = int(20)  # int
x = float(20.5)  # float
x = complex(1j)  # complex
x = list(("apple", "banana", "cherry"))  # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)  # range
x = dict(name="John", age=36)  # dict
x = set(("apple", "banana", "cherry"))  # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)  # bool
x = bytes(5)  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
