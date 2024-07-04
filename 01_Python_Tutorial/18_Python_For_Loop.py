# bin/bash !
# Daniel OUATTARA
# 12 04 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


""" Python For Loops
======================

A 'for' loop is used for iterating over a sequence (that is either a list,
a tuple, a dictionary, a set, or a string).
"""

print(50 * '-')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

"""Looping Through a String
===========================
Even strings are iterable objects, they contain a sequence of characters:"""

print(50 * '-')
for x in "banana":
    print(x)

""" The break Statement
=======================
With the 'break' statement we can stop the loop before it has looped through 
all the items:"""

print(50 * '-')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print(10 * '-')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

""" The continue Statement
===========================
With the 'continue' statement we can stop the current iteration of the loop, 
and continue with the next: """

print(50 * '-')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


""" The range() Function 
========================= """

print(50 * '-')
for x in range(6):
    print(x)

print(10 * '-')
for x in range(2, 10):
    print(x)

print(10 * '-')

for x in range(1, 15, 3):
    print(x)

""" Else in For Loop
=====================
The 'else' keyword in a 'for' loop specifies a block of code to be executed 
when the loop is finished: """

print(50 * '-')

for x in range(6):
    print(x)
else:
    print("Finally finished!")

""" Nested For Loops 
====================="""

print(50 * '-')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print(10 * '-')

for x in range(4):
    for y in range(4):
        if x != y:
            continue
        print(x, y)

""" The pass Statement
======================

'for' loops cannot be empty, but if you for some reason have 
a 'for' loop with no content, put in the 'pass' statement to 
avoid getting an error."""

for x in [0, 1, 2]:
    pass
