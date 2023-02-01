# bin/bash !
# Daniel OUATTARA
# 10 04 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
There are four collection data types (Arrays) in the Python programming language:

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

A set is a collection which is unordered and non indexed.
In Python sets are written with curly brackets.

Set Methods.
===============

Python has a set of built-in methods that you can use on sets.

Method 	  Description
-------   ------------
add()	                        Adds an element to the set.
clear()	                        Removes all the elements from the set.
copy()	                        Returns a copy of the set.
difference()	                Returns a set containing the difference between two or more sets.
difference_update()	            Removes the items in this set that are also included in another, 
                                specified set.
discard()	                    Remove the specified item.
intersection()	                Returns a set, that is the intersection of two other sets.
intersection_update()	        Removes the items in this set that are not present in other, 
                                specified set(s).
isdisjoint()	                Returns whether two sets have a intersection or not.
issubset()	                    Returns whether another set contains this set or not.
issuperset()	                Returns whether this set contains another set or not.
pop()	                        Removes an element from the set.
remove()	                    Removes the specified element.
symmetric_difference()	        Returns a set with the symmetric differences of two sets.
symmetric_difference_update()	inserts the symmetric differences from this set and another.
union()	                        Return a set containing the union of sets.
update()	                    Update the set with the union of this set and others.

"""

print(70 * "-", "0")

# Set literal
# ============
first_set = {'apple', 'banana', 'cherry'}
print('first_set = ', first_set)

print(70 * "-", "1")

# The set() Constructor.
# =======================
constructed_set = set(('apple', 'banana', 'cherry'))
print('constructed_set = ', constructed_set)

print(70 * "-", "2")

# Duplicates Not Allowed
# ======================
this_set = {"apple", "banana", "cherry", "apple"}
print('this_set = ', this_set)

print(70 * "-", "3")

# type
# =====
print(type(this_set))

print(70 * "-", "4")

# Access Items.
# =============
for item in first_set:
    print(item)

print(70 * "-", "5")

# Check if Item Exists.
# =====================
print("'orange' in first_set = ", 'orange' in first_set)
print("'banana' in first_set = ", 'banana' in first_set)

print(70 * "-", "6")

# Change Items.
# =============
'''Once a set is created, you cannot change its items, but you can add new items.'''

# Add Items.
# ==========
first_set.add('melon')  # add an unique item
print('first_set = ', first_set)

first_set.update(['orange', 'grapes', 'mango'])
print('first_set = ', first_set)

print(70 * "-", "7")

# Get the Length of a Set.
# ========================
print('first_set_length = ', len(first_set))

print(70 * "-", "8")

# Remove Item.
# ============
first_set.remove('banana')  # raise Error if item to remove is not present
print('first_set = ', first_set)
print('first_set_length = ', len(first_set))

first_set.discard('orange')  # Does not raise Error if item to discard is not present
print('first_set = ', first_set)
print('first_set_length = ', len(first_set))

removed_by_pop = first_set.pop()  # pop() removes an arbitrary item form the set.
print('removed_by_pop =', removed_by_pop)
print('first_set = ', first_set)
print('first_set_length = ', len(first_set))

first_set.clear()  # clear() : empties the set
print('first_set = ', first_set)
print('first_set_length = ', len(first_set))

first_set = {'apple', 'banana', 'cherry'}
del first_set  # 'del' will delete the set completely
# print('first_set = ', first_set)  # NameError: name 'first_set' is not defined
# print('first_set_length = ', len(first_set))  # NameError: name 'first_set' is not defined

print(70 * "-", "9")

# Join Two Sets.
# ==============
alphabet_letters = {'a', 'b', 'c', 'd', 'e', 'f'}
even_number = {2, 4, 6, 8, 10}
prime_number = {2, 3, 5, 7, 11, 13, 17}
odd_number = {1, 3, 5, 7, 9, 11}

even_number.union(odd_number)
print('even_number.union(odd_number) = ', even_number)

even_number.update(prime_number)
print('even_number.update(prime_number) = ', even_number)

even_number.intersection(prime_number)
print('even_number.intersection(prime_number) = ', even_number)

print('odd_number.intersection(prime_number) =', odd_number.intersection(prime_number))
print('odd_number.intersection(prime_number) =', odd_number.intersection_update(prime_number))

print('odd_number.difference(prime_number) = ', odd_number.difference(prime_number))
print('odd_number.difference(prime_number) = ', odd_number.difference(prime_number))

print(70 * "-", "10")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print("x.intersection_update(y) = ", x.intersection_update(y))

print(70 * "-", "11")

# # print help
# print("dir(y) = ", dir(y))
#
# print(70 * "-", "12")
#
# # print help
# print(help(y))