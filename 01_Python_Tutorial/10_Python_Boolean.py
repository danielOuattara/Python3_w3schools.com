# bin/bash !
# Daniel OUATTARA
# 14 03 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

#  Boolean Values

print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False
print(10 != 9)  # True

a = 200
b = 33

print(50 * '-')

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(50 * '-')

#  Evaluate Values and Variables

"""bool() function """

print(bool("Hello"))  # True
print(bool(15))  # True
print(bool(0))  # False
print(bool(""))  # False

x = " home"
print(bool(x))  # True

print(50 * '-')

#  Most Values are True

print(bool("abc"))  # True
print(bool(123))  # True
print(bool(("apple", "cherry", "orange")))  # True  // tuple
print(bool(["apple", "cherry", "orange"]))  # True  // list
print(bool({"apple", "cherry", "orange"}))  # True  // set
print(bool({"one": 1, "two": 2, "three": 3}))  # True ; dictionary

print(50 * '-')

#  Some Values are False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print(50 * '-')


#  Functions can Return a Boolean

def function1_true():
    return True


print(function1_true())

if function1_true():
    print("yes !")
else:
    print("No !")

# Python also has many built-in functions that returns a boolean value, like
# the 'isinstance()' function, which can be used to determine if an object is 
# of a certain data type:

x = 200
print(isinstance(x, int))  # True

y = "Hello"
print(isinstance(y, int))  # False

print(isinstance(y, str))  # True
