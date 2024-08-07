# bin/bash !
# Daniel OUATTARA
# 15 09 2021
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
There are four collections data types (Arrays) in the Python programming language:
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
it could mean an increase in efficiency or security.

List Methods
==============

A list is a collection which is ordered and changeable. 
In Python lists are written with square brackets.

Python has a set of built-in methods that you can use on 'lists'.

Method 	    Description
--------    -----------
append()    Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

print(70 * '-', '0')

""" Lists """

# list literal definition
# ========================

first_list = ["apple", "banana", "cherry"]
print('first_list =', first_list)
print(70 * '-', '1')

#  Allow duplicate
#  ================
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)
print(70 * '-', '2')

#  list length
#  ================
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print("len(this_list) = ", len(this_list))
print(70 * '-', '3')

#  List Items - Data Types
#  ========================
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print('list1 =', list1)
print('list2 =', list2)
print('list3 = ', list3)

list_mixed = ["abc", 34, True, 40, "male"]

print('list_mixed = ', list_mixed)

#  type()
#  ========
print(type(this_list)) # <class 'list'>

#  The list() Constructor
#  =======================

this_list = list(("apple", "banana", "cherry"))  # note the double round-brackets
print('this_list = ', this_list)

print(70 * '-', '4')
#  Access Items
# ==============
print(first_list[0])
print(first_list[1])
print(first_list[2])
print(70 * '-', '4bis')

#  Negative Indexing
# ===================
print(first_list[-1])  # refers to the last index
print(first_list[-2])  # refers to the second last...etc..
print(first_list[-3])

print(70 * '-', '5')

#  Range of Indexes
# ==================
second_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('second_list =', second_list)
print(second_list[2:5])  # starts at index 2 (third element) ends at index 5 excluded (sixth element)!
print(second_list[:4])  # starts at index 0 ends at index 4 excluded (fifth element)!
print(second_list[2:])  # starts at index 2 ends at last index included!

print(70 * '-', '6')

#  Range of Negative Indexes
# ===========================
third_list = ["pineapple", "strawberry", "blackberry", "melon", "tomato", "papaya", "lemon"]
print(third_list[-4:-1])
print(70 * '-', '7')

#  Change Item Value
# ===================
third_list[0] = "komkut"
print(third_list)
print(70 * '-', '8')

# Loop Through a List
# ====================
for item in third_list:
    print(item)
print(70 * '-', '9')

#  Check if Item Exists
# ======================

this_list = ["apple", "banana", "cherry"]
if "apple" in this_list:
    print("Yes, 'apple' is in the fruits list")


def items_exist(item, list_ident):
    if item in list_ident:
        print(True, ": ", item, "in", list_ident, ': ')
    else:
        print(False, ": ", item, "not in", list_ident, ': ')


items_exist("apple", third_list)
items_exist("apple", first_list)
items_exist("apple", second_list)
print(70 * '-', '10')

#  Change Item Value
#  =================

this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list)

#  Change a Range of Item Values
#  ==============================

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print('this_list === ', this_list)

this_list[1:3] = ["blackcurrant", "watermelon"]
print('this_list === ', this_list)

this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)

this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)

#  Insert Items
#  =============

this_list = ["apple", "banana", "cherry"]
print(this_list)
this_list.insert(2, "watermelon")
print(this_list)

# Add Items.
# ===========

# Append Items
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)
print(70 * '-', '11')

#  Insert Items
this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)
print(70 * '-', '12')

#  Extend List
this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)
print(70 * '-', '13')

#  Add Any Iterable
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)
print(70 * '-', '14')

#  Remove Item
print("first_list = ", first_list)
first_list.remove("banana")  # remove()
print("first_list = ", first_list)

print("second_list", second_list)
second_list.pop()  # pop()
print("second_list", second_list)

#  del first_list[2]  # remove index 2 element
print("first_list =", first_list)

fourth_list = first_list
print("fourth_list =", fourth_list)
del fourth_list  # this command will delete all the fourth_list
print(70 * "-")

# print(fourth_list)  # this command will cause NameError: fourth_list no more defined

first_list.clear()  # clear()
print("first_list =", first_list)
print(70 * '-', '15')

#  Clear the List
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print("this_list = ", this_list)

#  List Length
print("first_list length =", len(first_list))  # 0
print("second_list length =", len(second_list))  # 6
print("third_list length =", len(third_list))  # 7
print(70 * '-', '16')

#  Loop Through a List
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)
print(70 * '-', '17')

#  Loop Through the Index Numbers
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
    print(this_list[i])

print(70 * '-', '18')

#  Using a While Loop
#  ===================

this_list = ["apple", "banana", "cherry"]
i = 0
while i < len(this_list):
    print(this_list[i])
    i += 1

print(70 * '-', '19')

#  Looping Using List Comprehension
#  =================================

this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]

print(70 * '-', '20')

#  List Comprehension
#  ===================

# using 'basic' setting

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print("new_list = ", new_list)

print(70 * '-', '21')

#  Using comprehension list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list2 = [x for x in fruits if "a" in x]
print("new_list2 = ", new_list2)

newListCapitalize = [x.capitalize() for x in fruits]  # OK
print('newListCapitalize = ', newListCapitalize)

print(70 * '-', '22')

#  The Syntax
#  new_list = ["expression" for item in iterable if "condition" == True]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list3 = [x for x in fruits if x != "apple"]
print("new_list3 =", new_list3)
print(70 * '-', '23')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list4 = [x for x in fruits]
print("new_list4 =", new_list4)
print(70 * '-', '24')

new_list = [x for x in range(10)]
print(new_list)

new_list = [x for x in range(10) if x < 5]
print(new_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x.upper() for x in fruits]
print(new_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = ['hello' for x in fruits]
print(new_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
new_list = [x for x in fruits if x != "banana"]
print(new_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
new_list = [x if x != "banana" else "orange" for x in fruits]
print(new_list)
print(70 * '-', '24-Bis')

# sort().
# =======
second_list.sort()
print("second_list.sort= ", second_list)
print(70 * '-', '25')

# reverse().
# ==========
second_list.reverse()
print("second_list.reversed = ", second_list)
print(70 * '-', '26')

print("second_list", second_list)

#  Copy a List.
# ==============
five_list = second_list.copy()  # copy()
print("second_list =", second_list)
print("five_list =", five_list)

list_sixth = list(second_list)  # list()
print("list_sixth =", list_sixth)
print(70 * '-', '27')

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
print(70 * '-', '28')

#  List constructor: list().
# ==========================
fruits_list = list(("orange", "mango", "passion"))
print("fruits_list = ", fruits_list)
print(70 * '-', '29')

# count().
# ========
print("second_list=", second_list)
print(second_list.count("tomato"))  # return 0: zero occurrence for 'tomato' in second_list
print(second_list.count("kiwi"))  # return 1:  one occurrence for 'kiwi' in second_list
print(70 * '-', '30')

# --- Program End !
