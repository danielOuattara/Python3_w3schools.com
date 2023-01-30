# bin/bash !
# Daniel OUATTARA
# 13 03 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

""" Python Number 
==================
There are three (03) numeric types in Python:
   > int
   > float
   > complex
"""

import random
import cmath

# Python Numbers

x = 1
y = 2.8
z = 1j
print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex"

# int: (integer) , is a whole number, positive or negative,
# ===  without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# float:   float or 'floating point number', positive or negative,
# =======  containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# complex: Complex numbers are written with a "j" as the imaginary part:
# ========
x = 3 + 5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
print(x + y)

# Type Conversion
# =================
x = 1  # int
y = 2.8  # float
z = 1j  # complex

"""convert from int to float: """
a = float(x)
print('a = ', a)  # 1.0
print(type(a))

"""convert from float to int:"""
b = int(y)
print('b =', b)  # 2
print(type(b))

"""convert from int to complex:"""
c = complex(x)
print(c)
print(type(c))  # (1 + 0j)

imaginary = z.imag
real = z.real

# Random Number

""" Use of Python's module 'random' is required """


def random_massive_display():
    """This function displays 20 times a random number
       in the range of (1, 10) """
    for i in range(20):
        print('random n°', i, ' = ', random.randrange(1, 11))


random_massive_display()
