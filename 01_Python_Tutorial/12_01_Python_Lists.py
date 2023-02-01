# bin/bash !
# Daniel OUATTARA
# 14 03 2021
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
There are four collections data types in the Python
programming language:
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

When choosing a collection type, it is useful to understand
the properties of that type. Choosing the right type for a
particular data set could mean retention of meaning, and,
it could mean an increase in efficiency or security.


List Methods
==============

A list is a collection which is ordered and changeable. 
In Python lists are written with square brackets.

Python has a set of built-in methods that you can use on
'lists'.

Method 	    Description
--------    -----------
append()    Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements from a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

print(70 * '-')

""" Lists """

first_list = ["apple", "banana", "cherry"]
print('first_list =', first_list)
print(70 * '-')

#  Allow duplicate
#  ================
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print("this_list = ", this_list)
print(70 * '-')

#  list length
#  ================
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print("len(this_list) = ", len(this_list))
print(70 * '-')

#  Access Items
# ==============
print(first_list[0])
print(first_list[1])
print(first_list[2])

print(70 * '-')

#  Negative Indexing
# ===================
print(first_list[-1])  # refers to the last index
print(first_list[-2])  # refers to the second last...etc..
print(first_list[-3])
print(70 * '-')

#  Range of Indexes
# ==================
second_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('second_list =', second_list)
print(second_list[2:5])  # starts at index 2 (third element) ends at index 5 excluded (sixth element)!
print(second_list[:4])  # starts at index 0 ends at index 4 excluded (fifth element)!
print(second_list[2:])  # starts at index 2 ends at last index included!
print(70 * '-')

#  Range of Negative Indexes
# ===========================
third_list = ["pineapple", "strawberry", "blackberry", "melon", "tomato", "papaya", "lemon"]
print(third_list[-4:-1])
print(70 * '-')

#  Change Item Value
# ===================
third_list[0] = "komkut"
print(third_list)
print(70 * "-")

# Loop Through a List
# ====================
for item in third_list:
    print(item)
print(70 * "-")


#  Check if Item Exists
# ======================
def items_exist(item, list_ident):
    if item in list_ident:
        print(True, ": ", item, "in", list_ident, ': ')
    else:
        print(False, ": ", item, "not in", list_ident, ': ')


items_exist("apple", third_list)
items_exist("apple", first_list)
items_exist("apple", second_list)
print(70 * "-")

#  List Length
# =============
print("first_list length =", len(first_list))  # 3
print("second_list length =", len(second_list))  # 7
print("third_list length =", len(third_list))  # 7
print(70 * "~-")


# capitalize list item
# ======================

def list_capital(list_id):  # OK
    list_id_2 = []
    for element in list_id:
        list_id_2.append(element.capitalize())
    return list_id_2


print(first_list)
print(list_capital(first_list))


def list_capitalizer(list_item):  # OK
    for i in range(len(list_item)):
        list_item[i] = list_item[i].capitalize()
    return list_item


print(list_capitalizer(first_list))

print(70 * '-')

# Add Items.
# ===========

print("first_list = ", first_list)  # first_list =  ['apple', 'banana', 'cherry']

first_list.append("orange")  # append()
print("first_list = ", first_list)  # first_list =  ['apple', 'banana', 'cherry', 'orange']

first_list.insert(1, "melon")  # insert()
print("first_list", first_list)  # ['Apple', 'Melon', 'Banana', 'Cherry', 'orange']
print(70 * "-")


#  Remove Item
# =============
print("first_list", first_list)

first_list.remove("banana")  # remove()
print("first_list", first_list)

print("second_list", second_list)
second_list.pop()  # pop()
print("second_list", second_list)

del first_list[2]  # remove index 2 element
print("first_list =", first_list)

fourth_list = first_list
print("fourth_list =", fourth_list)
del fourth_list  # this command will delete all the fourth_list
print(70 * "-")

# print(fourth_list)  # this command will cause NameError: fourth_list no more defined

# Clear
# ============
first_list.clear()  # clear()
print("first_list =", first_list)
print(70 * "-")

#  Copy a List.
# ==============
five_list = second_list.copy()  # copy()
print("second_list =", second_list)
print("five_list =", five_list)

list_sixth = list(second_list)  # list()
print("list_sixth =", list_sixth)
print(70 * "-")

# Join Two Lists.
# ===============
list_one = ["a", "b", "c"]
list_two = ["d", "e", "f"]
list_three = list_one + list_two
print("list_three = ", list_three)

for item in list_one:
    list_two.append(item)
print("list_two =", list_two)

list_one.extend(list_three)
print("list_one =", list_one)  # Notice: Lists accept duplicated element
print(70 * "-")

#  List constructor: list().
# ==========================
fruits_list = list(("orange", "mango", "passion"))
print("fruits_list = ", fruits_list)
print(70 * "-")

# count().
# ========
print("second_list=", second_list)
print(second_list.count("tomato"))  # return 0: zero occurrence for 'tomato' in second_list
print(second_list.count("kiwi"))  # return 1:  one occurrence for 'kiwi' in second_list
print(70 * "-")

# sort().
# =======
second_list.sort()
print("second_list.sort= ", second_list)
print(70 * "-")

# reverse().
# ==========
second_list.reverse()
print("second_list.reversed = ", second_list)
print(70 * "-")

print("second_list", second_list)

# --- Program End !
