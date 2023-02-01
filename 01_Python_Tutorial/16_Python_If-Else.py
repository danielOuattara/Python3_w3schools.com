# bin/bash !
# Daniel OUATTARA
# 12 04 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


"""  Python  If...Else """

# Python Conditions and If statements
# ===================================
'''
Python supports the usual logical conditions from mathematics:

    > Equals: a == b
    > Not Equals: a != b
    > Less than: a < b
    > Less than or equal to: a <= b
    > Greater than: a > b
    > Greater than or equal to: a >= b            '''

""" If """

a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


def integer_comparison1():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    if a > b:
        print(a, " > ", b)
    if a < b:
        print(a, " < ", b)


# short hand if

a = 200
b = 33
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested If

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# The pass Statement
a = 33
b = 200

if b > a:
  pass

# integer_comparison2()


"""If... Elif """


def integer_comparison2():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    if a > b:
        print(a, " > ", b)
    elif a < b:
        print(a, " < ", b)


# integer_comparison2()


""" If ... Else"""


def integer_comparison3():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    if a > b:
        print(a, " > ", b)
    else:
        print(a, " < ", b)


#  integer_comparison3()


"""If... Elif... Else"""


def integer_comparison4():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    if a > b:
        print(a, " > ", b)
    elif a < b:
        print(a, " < ", b)
    else:
        print(a, "=", b)


#  integer_comparison4()


""" Short Hand If """


def integer_comparison6():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    if a > b:
        print(a, " > ", b)


#  integer_comparison6()


""" Short Hand If..Else """


def integer_comparison7():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    print(a, " > ", b) if a > b else print(a, "<=", b)


#  integer_comparison7()


""" Short If... Elif... Else """


def integer_comparison8():
    a = int(input("enter the integer 'a' : "))
    b = int(input("enter the integer 'b' : "))
    print(a, " > ", b) if a > b else print(a, " < ", b) if a < b else print(a, "=", b)


#  integer_comparison8()


""" And """


def integer_comparison9():
    a = int(input("enter the integer 'a' : "))
    if 4 < a < 10:
        print(4, " < ", 10)


#  integer_comparison9()


""" Or """


def integer_comparison10():
    a = int(input("enter the integer 'a' : "))
    if a > 4 or a < 10:
        print(4, "< ", a, "< ", 10)


#  integer_comparison10()


""" If not """

a = int(input("enter the integer 'a' : "))
if not a > 4:
    print("a is not greater than 4 or ")

""" Nested If """

""" The pass Statement
----------------------

if statements cannot be empty, but if for some reason, 
you have an if statement with no content, put in the 'pass' 
statement to avoid getting an error."""
