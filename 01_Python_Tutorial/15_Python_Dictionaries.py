# bin/bash !
# Daniel OUATTARA
# 14 03 2020
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
|               |  dict(key=value)   |          |               |             |             |
|-------------------------------------------------------------------------------------------|

When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning, and,
it could mean an increase in efficiency or security."""

'''

A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have 
keys and values.

Dictionary Methods.
===================

Python has a set of built-in methods that you can use on dictionaries.

Method 	        Description
--------        ------------
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: 
                insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary

'''

print(70 * "-", "1")

# dict
# ======

first_dict = {
    'brand': 'ford',
    'model': 'Mustang',
    'year': 1964
}

print('first_dict = ', first_dict)

# The dict() Constructor
# ======================

second_dict = dict(
    brand='Yamaha',
    version='ZMAX 750',
    cylinder=4,
    year=1999
)
print('second_dict =', second_dict)

print(70 * "-", "2")

my_dict = dict()
my_dict["firstName"] = "Daniel"
my_dict["lastName"] = "Ouattara"
print(my_dict)

print(70 * "-", "3")

# Accessing Items.
# ================
print('first_dict["brand"] = ', first_dict['brand'])

print(70 * "-", "4")

# get method.
# ============

print(first_dict.get("model"))  # returns Mustang / key= "model" is in first_dict
print(first_dict.get("title"))  # returns None    / key= "title" is not in first_dict
print(first_dict.get("amazon"))  # returns None    / key= "title" is not in first_dict

print(70 * "-", "5")

# Change Values.
# ==============

first_dict['year'] = 2018
print('first_dict =', first_dict)

print(70 * "-", "6")

# Loop Through a Dictionary
# ==========================

# print key:

for item in first_dict:
    print(item)  # print all key names in dictionary, one by one

print(20 * '-')

for key in second_dict:
    print(key)  # same here

print(20 * '-')

for item in second_dict.keys():
    print(item)  # same here

print(20 * '-')

for key in second_dict.keys():
    print(key)  # same here
print(20 * '-')
# --------------------------

# print Values

for item in first_dict:
    print(first_dict[item])  # print all values in dictionary, one by one
print(20 * '-')

for key in second_dict:
    print(second_dict[key])  # print all values in dictionary, one by one
print(20 * '-')

for item in second_dict.values():
    print(item)  # print values of dictionary

for value in second_dict.values():
    print(value)  # print values of dictionary

# print key/value pairs

print(70 * "-", "7")

for key, value in second_dict.items():
    print(key, '=', value)
print(20 * '-', "8")

for key in first_dict.keys():
    value = first_dict[key]
    print(key, '=', value)

print(70 * '-', "9")

# Check if Key Exists.
# ====================

third_dict = {'fruits': 'banana', 'vegetable': 'eggplant', 'energy': 'coal'}
print('third_dict =', third_dict)

if 'fruits' in third_dict:
    print("'fruits' in third_dict: ", True)

if 'fruits' in third_dict.keys():
    print("'fruits' in third_dict: ", True)

if 'banana' in third_dict.values():
    print("'banana' in third_dict: ", True)


def check_if_key_in(key, dict_name):
    if key in dict_name:
        print(key, "in", dict_name, True)
    else:
        print(key, "in", dict_name, False)


check_if_key_in('animal', third_dict)

# Dictionary Length.
# ===================
print('len(first_dict) =', len(first_dict))
print('len(second_dict) = ', len(second_dict))
print('len(third_dict) =', len(third_dict))

# Adding Items.
# =============

print('first_dict =', first_dict)

first_dict['price'] = 150000
first_dict["warranty Length"] = 5

print('first_dict =', first_dict)
print('len(first_dict) =', len(first_dict))

print(20 * '-')

print('third_dict =', third_dict)

third_dict["animal"] = "donkey"
third_dict['crops'] = "quakers"

print('third_dict =', third_dict)

print('len(third_dict) =', len(third_dict))

# Old version below

print('================================================================')

# dict
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(this_dict)

print(70 * '-', "10")

# dict items
print(this_dict["brand"])

print(70 * '-', "11")

# Duplicates Not Allowed
# =======================
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,  # this last element is kept
}

print("this_dict === ", this_dict)
print(70 * '-', "12")

# Dictionary Length
# ==================
print(len(this_dict))  # 3
print(70 * '-', "13")

# Dictionary Items - Data Types
# =============================
this_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(this_dict)

print(70 * '-', "14")

# type()
# ========
print(type(this_dict))

print(70 * '-', "15")

# Accessing Items
# ===================
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = this_dict["model"]
print(x)

y = this_dict.get("model")
print(y)

print(70 * '-', "16")

# Get Keys
# =========
list_of_all_keys = this_dict.keys()
print(list_of_all_keys)
print(70 * '-', "17")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

list_all_car_key = car.keys()

print(list_all_car_key)  # before the change

car["color"] = "white"

print(list_all_car_key)  # after the change
print(70 * '-', "18")

# Get Values
# ===========

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
list_all_values = this_dict.values()
print(list_all_values)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

list_all_car_values = car.values()

print(list_all_car_values)  # before the change

car["year"] = 2020

print(list_all_car_values)  # after the change

car2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

list_all_car2_values = car2.values()

print(list_all_car2_values)  # before the change

car2["color"] = "Orange"

print(list_all_car2_values)  # after the change

print(70 * '-')

# Get Items
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

all_car_items = car.items()

print(all_car_items)  # before the change

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# ---

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

print(70 * '-')

# Check if Key Exists
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in this_dict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(70 * '-')

# Change Values

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#
this_dict["year"] = 2018

print(this_dict)
print(70 * '-')

# Update Dictionary
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.update({"year": 2020})
print(this_dict)
print(70 * '-')

# Add items

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict["color"] = "red"
print(this_dict)
print(70 * '-')

# Remove Items

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.pop("model")
print(this_dict)
this_dict.pop("chat", None)
#       D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      If the key is not found, return the default if given; otherwise,
#  |      raise a KeyError.
# ---------

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.popitem()
print(this_dict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
#  |  popitem(self, /)
#  |  Remove and return a (key, value) pair as a 2-tuple.

# ---------

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del this_dict
# print(this_dict)  # raise Error

# ---------

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.clear()
print("this_dict ", this_dict)
#  D.clear() -> None.  Remove all items from D.

print(70 * '-')
# Loop Through
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for key in this_dict:
    print(key)

print('===')

for key in this_dict.keys():
    print(key)

print('===')

for key in this_dict:
    print(this_dict[key])

print('===')

for value in this_dict.values():
    print(value)

print('===')

for key, value in this_dict.items():
    print(key, ":", value)

print(70 * '-')
# Copy

"""
You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, and changes 
made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in 
Dictionary method copy().
"""

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
my_dict = this_dict.copy()
print(my_dict)

""" Make a copy of a dictionary with the dict() function:"""

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
my_dict = dict(this_dict)
print(my_dict)

print(70 * '-')

# Nested Dictionaries : A dictionary can contain dictionaries, this is called nested dictionaries.

my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(my_family)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(my_family)
