# bin/bash !
# Daniel OUATTARA
# 13 03 2020
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


"""Python Strings"""

# String Literals
print("hello")
print('hello')


# Assign a string to a variable
a = "hello"
print(a)


# Multi-line Strings
b = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(b)

print(80 * "-")

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

print(80 * "-")

#  Strings in Python are Arrays
greeting = "Hello world !"
print(greeting[0])
print(greeting[1])
print(greeting[2])

print(80 * "-")

#  Looping through a string
for x in "banana":
    print(x)

print(80 * "-")

# String Length

a = "Hello World again !"
print("len(a) = ", len(a))

print(80 * "-")

#  Check string

print("world" in a)  # w : lower case
print("World" in a)  # W : upper case

print("world" not in a)
print("World" not in a)

print(80 * "-")

#  Slicing Positive indexing: last index not included !
print(greeting[2:5])  #
print(greeting[6:])
print(greeting[:7])

#  Slicing Negative Indexing: first index not included !
print(greeting[-5: -2])
print(greeting[-1])
print(greeting[-2])
print(greeting[-3])
print(greeting[-4])


#  String Length
print("len_of_greeting =", len(greeting))


#  String Methods

#  strip() 
greeting = "  Hello World ! "
print(greeting.strip())

#  lower() 
print(greeting.lower())

#  upper() 
print(greeting.upper())

# replace() 
print(greeting.replace('d', "d Again"))

#  split() 
print(greeting.split())  # returns ['Hello', 'World', '!']

# Check String
text = "The rain in Spain stays mainly in the plain"

x = "rain" in text
print(x)  # True

y = "rain" not in text
print(y)  # False

z = "snow" not in text
print(z)  # True

#  String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)  # HelloWorld
print(a, b)  # Hello World
print(a + b)  # HelloWorld
c = a + " " + b
print(c)  # Hello World


#  format() method

age = 3
# print(" My name is John, I am" + age)
""" 
above code raises a TypeError !
instead prefer using "format()" method
"""

text = "My name is John, I am {}"
print(text.format(age))

print(f"My name is John, I am {age}")

#  Or :
print('My name is John Doe, I\' am', age)

quantity = 3
itemNo = 567
price = 49.45

my_order = "I want {} pieces of item {} for ${} "
print(my_order.format(quantity, itemNo, price))

my_order = "You want to pay ${2} for {0} items of pieces id {1} "
print(my_order.format(quantity, itemNo, price))

print("He wants {} pieces of item {} for ${}".format(5, 567, 49.45))
print("She want {0} pieces of item {1} for ${2}".format(7, 567, 49.45))
print("We want {qty} pieces of item {item_ref} for ${money}".format(qty=9, item_ref=567, money=49.45))


#  Escape character
text = "We are the so-called \"Vikings\" from the north."
print(text)

"""
Other escape characters used in Python:

Code 	Result 	
----    -------
 \' 	    Single Quote 	
 \\  	    Backslash 	
 \n 	    New Line 	
 \r 	    Carriage Return 	
 \t 	    Tab 	
 \b 	    Backspace 	
 \f 	    Form Feed 	
 \ooo 	Octal value  """
# \xhh 	Hex value
"""

String Methods
==================
Python has a set of built-in methods that you can use 
on strings.

Note: All string methods returns new values. They do 
not change the original string.

Method       	 Description
-------          ------------
 capitalize()	 Converts the first character to upper case
 casefold()	     Converts string into lower case
 center()	     Returns a centered string
 count()	     Returns the number of times a specified value occurs in a string
 encode()	     Returns an encoded version of the string
 endswith()	     Returns true if the string ends with the specified value
 expandtabs()	 Sets the tab size of the string
 find()	         Searches the string for a specified value and returns the position of where it was found
 format()	     Formats specified values in a string | TODO: learn this method.
 format_map()	 Formats specified values in a string
 index()	     Searches the string for a specified value and returns the position of where it was found
 isalnum()	     Returns True if all characters in the string are alphanumeric
 isalpha()	     Returns True if all characters in the string are in the alphabet
 isdecimal()	 Returns True if all characters in the string are decimals
 isdigit()	     Returns True if all characters in the string are digits
 isidentifier()	 Returns True if the string is an identifier
 islower()	     Returns True if all characters in the string are lower case
 isnumeric()	 Returns True if all characters in the string are numeric
 isprintable()	 Returns True if all characters in the string are printable
 isspace()	     Returns True if all characters in the string are whitespaces
 istitle() 	     Returns True if the string follows the rules of a title
 isupper()	     Returns True if all characters in the string are upper case
 join()	         Joins the elements of an iterable to the end of the string
 ljust()	     Returns a left justified version of the string
 lower()	     Converts a string into lower case
 lstrip()	     Returns a left trim version of the string
 maketrans()	 Returns a translation table to be used in translations
 partition()	 Returns a tuple where the string is parted into three parts
 replace()	     Returns a string where a specified value is replaced with a specified value
 rfind()	     Searches the string for a specified value and returns the last position of where it was found
 rindex()	     Searches the string for a specified value and returns the last position of where it was found
 rjust()	     Returns a right justified version of the string
 rpartition()	 Returns a tuple where the string is parted into three parts
 rsplit()	     Splits the string at the specified separator, and returns a list
 rstrip()	     Returns a right trim version of the string
 split()	     Splits the string at the specified separator, and returns a list
 splitlines()	 Splits the string at line breaks and returns a list
 startswith()	 Returns true if the string starts with the specified value
 strip()	     Returns a trimmed version of the string
 swapcase()	     Swaps cases, lower case becomes upper case and vice versa
 title()	     Converts the first character of each word to upper case
 translate()	 Returns a translated string
 upper()	     Converts a string into upper case
 zfill()	     Fills the string with a specified number of 0 values at the beginning
"""
