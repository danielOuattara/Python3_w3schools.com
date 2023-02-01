# bin/bash !
# Daniel OUATTARA
# 24 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

""" Python Functions
=========================

A function is a block of code which only runs when it is called.
You can pass data, known as arguments, into a function.
A function can return data as a result."""

""" Creating a Function 
========================"""


def my_function():
    print("Hello from a function")


""" Calling a Function 
======================="""


def my_function_2():
    print("Hello from a function")


my_function_2()
print(70 * '-')

""" Arguments
================
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside 
the parentheses. You can add as many arguments as you want, 
just separate them with a comma. 
Arguments are often shortened to args in Python documentations."""


def my_function_3(fname):
    print(fname + " Refsnes")


my_function_3("Emil")
my_function_3("Tobias")
my_function_3("Linus")
print(70 * '-')

""" Parameters or Arguments ?
===============================
- A parameter is the variable listed inside the parentheses in 
  the function definition.
- An argument is the value that is sent to the function when 
  it is called. """


""" Number of Arguments
===========================
By default, a function must be called with the correct number of arguments. """


def my_function_4(fname, lname):
    print(fname + " " + lname)


my_function_4("Emil", "Refsnes")
print(70 * '-')

""" If you try to call this function with 1 or 3 arguments, you will get an error:"""

""" Arbitrary Arguments, *args
===============================
If you do not know how many arguments will be passed into 
your function, add a * before the parameter name in the function 
definition. This way the function will receive a tuple of arguments, 
and can access the items accordingly: """


def my_function_5(*kids):
    print("The youngest child is " + kids[1], '\nThe older is', kids[2])


my_function_5("Emil", "Tobias", "Linus")

""" Arbitrary Arguments are often shortened to *args in Python documentations."""

""" Keyword Arguments
======================
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.  """


def my_function_6(child3, child2, child1):
    print("The youngest child is " + child3)


my_function_6(child1="Emil", child2="Tobias", child3="Linus")

"""
The phrase Keyword Arguments are often shortened to kwargs in Python documentations."""

""" Arbitrary Keyword Arguments, **kwargs
==========================================
If you do not know how many keyword arguments will be passed 
into your function, add two asterisk: ** before the parameter name
in the function definition.

This way the function will receive a dictionary of arguments, and 
can access the items accordingly:"""


def my_function_7(**kid):
    print("His last name is " + kid["lname"])


my_function_7(fname="Tobias", lname="Refsnes")

"""
Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations."""

""" Default Parameter Value
============================
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:"""


def my_function_8(country="Norway"):
    print("I am from " + country)


my_function_8("India")
my_function_8()
my_function_8("Brazil")

""" Passing a List as an Argument
=====================================
You can send any data types as argument to a function 
(string, number, list, dictionary etc.), and it will 
be treated as the same data type inside the function. """


def my_function_9(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function_9(fruits)

""" Return Values
==================
To let a function return a value, use the return statement: """


def my_function_10(x):
    return 5 * x


print(my_function_10(3))
print(my_function_10(5))
print(my_function_10(9))

""" The pass Statement
=========================
function definitions cannot be empty, but if you for some 
reason have a function definition with no content, put in 
the pass statement to avoid getting an error. """


def my_function_11():
    pass


""" Recursion
===============
Python also accepts function recursion, which means 
a defined function can call itself. Recursion is a 
common mathematical and programming concept. It means 
that a function calls itself. This has the benefit of 
meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as 
it can be quite easy to slip into writing a function 
which never terminates, or one that uses excess amounts 
of memory or processor power. However, when written correctly 
recursion can be a very efficient and mathematically-elegant 
approach to programming.

In this example, tri_recursion() is a function that we have 
defined to call itself ("recurse"). We use the k variable as 
the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 
(i.e. when it is 0).

To a new developer it can take some time to work out how exactly
this works, best way to find out is by testing and modifying it. """


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print("result = ", result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
