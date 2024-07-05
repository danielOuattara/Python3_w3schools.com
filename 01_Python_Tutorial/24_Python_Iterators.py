# bin/bash !
# Daniel OUATTARA
# 25 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
Python Iterators
=================

An iterator is an object that contains a countable
number of values and can be iterated upon, meaning
that you can traverse through all the values.

Technically, in Python, an iterator is an object
which implements the iterator protocol, which consist
of the methods __iter__() and __next__().


Iterator vs Iterable
=====================

Lists, tuples, dictionaries, and sets are all iterable
objects. They are iterable containers which you can get
an iterator from. All these objects have an iter() method
which is used to get an iterator:

Example: Return an iterator from a tuple, and print each
value:
"""

my_tuple = ("apple", "banana", "cherry")
my_iterator = iter(my_tuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print(70 * '-')

""" 
Even strings are iterable objects, and can return 
an iterator:

Example: Strings are also iterable objects, containing 
a sequence of characters:
"""

my_str = "banana"
my_it = iter(my_str)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))

print(70 * '-')

""" 
Looping Through an Iterator
===================================

We can also use a 'for' loop to iterate through an 
iterable object:

Example: Iterate the values of a tuple:
"""

my_tuple = ("apple", "banana", "cherry")

for x in my_tuple:
    print(x)

print(70 * '-')

""" 
Example: Iterate the characters of a string: 
"""

my_str = "banana"

for x in my_str:
    print(x)

print(70 * '-')

"""
The 'for' loop actually creates an iterator object and 
executes the next() method for each loop.


Create an Iterator
===================

To create an object/class as an iterator you have to 
implement the methods __iter__() and __next__() to your 
object.

As you have learned in the Python Classes/Objects chapter, 
all classes have a function called __init__(), which allows 
you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations 
(initializing, etc...), but must always return the iterator 
object itself.

The __next__() method also allows you to do operations, and 
must return the next item in the sequence.

Example: Create an iterator that returns numbers, starting 
         with 1, and each sequence will increase by one 
        (returning 1,2,3,4,5 etc.): """


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print(70 * '-')

"""
StopIteration
=================

The example above would continue forever if you had 
enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the 
StopIteration statement.

In the __next__() method, we can add a terminating condition 
to raise an error if the iteration is done a specified number 
of times:

Example: Stop after 20 iterations: 

"""


class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)

print(70 * '-')
