# bin/bash !
# Daniel OUATTARA
# 10 04 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
|-------------------------------------------------------------------------------------------|
|               |  literal /         | ordered  |  changeable/  |  duplicate  |    indexed  |
|               |  constructor       |          |  modifiable   |    member   |             |
|-------------------------------------------------------------------------------------------|
| > lists       |  [  ]              |   yes    |      yes      |      yes    |     yes     |
|               |  list((   ))       |          |               |             |             |
|-------------------------------------------------------------------------------------------|
| > tuples      |  (   )             |   yes    |      no       |      yes    |     yes     |
|               |  tuple((  ))       |          |               |             |             |
|-------------------------------------------------------------------------------------------|
| > sets        |  {   }             |    no    |      yes      |      no     |     no      |
|               |  set((   ))        |          |               |             |             |
|-------------------------------------------------------------------------------------------|
| > dictionary  |  {key: value}      |     no   |      yes      |      no     |     yes     |
|               |  dict(key:value)   |          |               |             |             |
|-------------------------------------------------------------------------------------------|

When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning, and,
it could mean an increase in efficiency or security."""

"""
Tuple Methods
================

A tuple is a collection which is ordered and unchangeable. 
In Python tuples are written with round brackets.

Python has two built-in methods that you can use on tuples.

Method  	Description
-------     -----------
count()	    Returns the number of times a specified
            value occurs in a tuple
            
index()	    Searches the tuple for a specified value and 
            returns the position of where it was found
"""

print(70 * "-", '0')

# Tuples.
first_tuple = ("apple", "banana", "cherry")
print('first_tuple =', first_tuple)
print(70 * "-", '1')

#  Allow duplicate
first_tuple = ("apple", "banana", "cherry", "apple")
print('first_tuple =', first_tuple)
print(70 * "-", '2')

#  Tuple Length
first_tuple = ("apple", "banana", "cherry", "apple")
print('first_tuple_length =', len(first_tuple))
print(70 * "-", '3')

#  Create Tuple With One Item
first_tuple = ("apple",)
print('first_tuple =', first_tuple)
print(type(first_tuple))

string_tuple = ("apple")
print('string_tuple =', string_tuple)
print(type(string_tuple))
print(70 * "-", '4')

#  Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print('tuple4 =', tuple4)
print(70 * "-", '5')

#  The tuple() Constructor
first_tuple = tuple(("apple", "banana", "cherry", "apple"))
print('first_tuple =', first_tuple)
print(70 * "-", '6')

#  Access Tuple Items
first_tuple = ("apple", "banana", "cherry")
print('first_tuple[1] =', first_tuple[1])
print(70 * "-", '7')

#  Negative Indexing
first_tuple = ("apple", "banana", "cherry")
print('first_tuple[-1] =', first_tuple[-1])
print(70 * "-", '8')

#  Range of Indexes

#  Range of Negative Indexes

#  Check if Item Exists

#  Change Tuple Values
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print(70 * "-", '9')

#  Add Items
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y.append("kiwi")
x = tuple(y)
print(x)
print(70 * "-", '10')

# Add tuple to a tuple
x = ("apple", "banana", "cherry")
print(x)
x += ('orange', "strawberry")
print(x)
print(70 * "-", '10-bis')

#  Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(70 * "-", '11')


#  Delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
#  print('thistuple = ', thistuple)
print(70 * "-", '11')


#  Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print(70 * "-", '12')

(green, green, red) = ("apple", "banana", "cherry")
print(green)
print(yellow)
print(red)

print(70 * "-", '13')


#  Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  # !!! notice the * in front of the red
print('green = ', green)  # apple
print('yellow = ', yellow)  # banana
print('red = ', red)  # ['cherry', 'strawberry', 'raspberry']
print(70 * "-", '14')

#  -------------------------------

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits  # !!! notice the * in front of the yellow
print('green = ', green)  # apple
print('yellow = ', yellow)  # ['banana', 'cherry', 'strawberry']
print('red = ', red)  # 'raspberry'
print(70 * "-", '15')

#  -------------------------------

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(*green, yellow, red) = fruits  # !!! notice the * in front of the green
print('green = ', green)  # apple
print('yellow = ', yellow)  # ['banana', 'cherry', 'strawberry']
print('red = ', red)  # 'raspberry'
print(70 * "-", '15')
