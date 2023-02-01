# bin/bash !
# Daniel OUATTARA
# 12 04 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


""" Python While Loops
=======================

Python has two primitive loop commands:

   > while loops
   > for loops

The while Loop
===============

With the while loop we can execute a set of statements
as long as a condition is true.
"""

print(50 * "-")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\nfinal i = ", i)

"""
Note: remember to increment 'i', or else the loop will continue  
      forever.

The 'while' loop requires relevant variables to be ready, in this 
example we need to define an indexing variable, i, which we set to 1.



The break Statement
=====================

With the 'break' statement we can stop the loop even if the while 
condition is true:
"""
print(50 * "-")
i = 1
while i <= 10:
    print(i)
    if i == 4:
        break
    i += 1

print("\nfinal i = ", i)

"""
The continue Statement
=======================

With the 'continue' statement we can stop the current iteration, 
and continue with the next:
"""
print(50 * "-")
i = 0
while i <= 10:
    i += 1
    if i == 4:
        continue
    print(i)

print("\nfinal i = ", i)

"""
The else Statement
===================

With the 'else' statement we can run a block of code once 
when the condition no longer is true:
"""

print(50 * "-")
i = 1
while i <= 10:
    i += 1
    print(i)
else:
    print("i > 10: while loop stopped !")

print("\nfinal i = ", i)
