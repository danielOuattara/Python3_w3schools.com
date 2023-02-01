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

# Tuples literal: ()
# ===================
first_tuple = ("apple", "banana", "cherry")
print('first_tuple =', first_tuple)
print(70 * "-", '1')


# The tuple() Constructor: tuple(( ))
# ====================================
this_tuple = tuple(('oeuf', 'ail', 'aubergine'))
print('this_tuple = ', this_tuple)


# Access Tuple Items.
# ===================
print('first_tuple[1] = ', first_tuple[1])
print(70 * "-", '2')


# Negative Indexing.
# ==================
print('first_tuple[-1] = ', first_tuple[-1])
second_tuple = ('Yamaha', 'Toyota', 'Honda', 'Nissan', 'Suzuki', 'Kawasaki')
print('second_tuple[2:5] = ', second_tuple[2:5])
print(70 * "-", '3')


# Range of Negative Indexes.
# ==========================
print('second_tuple[-5:-1] = ', second_tuple[-5:-1])
print(70 * "-", '4')


# Change Tuple Values.
# =====================
''' Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple. '''

tuple_1 = ('apple', 'mango', 'banana')
print('tuple_1 = ', tuple_1)

list_1 = list(tuple_1)

print('list_1 = ', list_1)
list_1[1] = 'kiwi'

tuple_1 = tuple(list_1)
print('tuple_1 = ', tuple_1)
print('type(tuple_1) =', type(tuple_1))
print(70 * "-", '5')


# Loop Through a Tuple
# ====================
for item in first_tuple:
    print(item)
print(70 * "-", '6')


# Check if Item Exists.
# =====================

def check_exist_1(item, tuple_name):
    """ To check repetitively (each element) if 'item'
        is present in a tuple. Enter an item and a tuple"""
    for element in tuple_name:
        if item is element:
            print(item, 'present: ', True)
        else:
            print(item, ' not present: ', False)


check_exist_1("Ninja", first_tuple)
check_exist_1("apple", first_tuple)

print(20 * '-')


def check_exist_2(item, tuple_name):
    """To check if an item is present in a tuple
       Enter an item name and a Valid tuple name"""
    if item in tuple_name:
        print(item, 'present: ', True)
    else:
        print(item, 'present: ', False)


check_exist_2("Ninja", first_tuple)

print(70 * "-", '7')


# Tuple Length.
# ==============
print('first_tuple_length = ', len(first_tuple))
print('second_tuple_length = ', len(second_tuple))

print(70 * "-", '8')


# Add Items.
# ==========
""" Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
    But there is a workaround. You can convert the tuple into a list, 
    change the list, and convert the list back into a tuple. """

tuple_1 = ('apple', 'mango', 'banana')
print('tuple_1 = ', tuple_1)

list_1 = list(tuple_1)
print('list_1 = ', list_1)

list_1.append('orange')
list_1.insert(0, 'melon')

tuple_1 = tuple(list_1)
print('tuple_1 = ', tuple_1)
print('type(tuple_1) =', type(tuple_1))
print(70 * "-", '9')


# Create Tuple With One Item.
# ===========================
'''To create a tuple with only one item, you have to add a comma after the item, 
    unless Python will not recognize the variable as a tuple.'''

solo_tuple = ('apple',)
print('solo_tuple = ', solo_tuple)
print('type(solo_tuple) = ', type(solo_tuple))

# Not a tuple
not_tuple = ('apple')
print('not_tuple = ', not_tuple)
print('type(not_tuple) = ', type(not_tuple))

print(70 * "-", '10')


# type(solo_tuple).
# =================

''' Tuples are unchangeable, so you cannot remove items from it, 
    but you can delete the tuple completely:'''

tuple_to_delete = ('zero', 'one', 'two', 'three')
del tuple_to_delete  # this command delete the tuple
# print(tuple_to_delete)  # this will cause a NameError: name 'tuple_to_delete' is not defined

print(70 * "-", '11')

# Join Two tuples.
# ================

tuple_one = (1, 2, 3)
tuple_two = ('a', 'b', 'c')

tuple_three = tuple_one + tuple_two

print('tuple_three = ', tuple_three)

tuple_four = tuple_two + tuple_one
print('tuple_four = ', tuple_four)



