# bin/bash !
# Daniel OUATTARA
# 30 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
Python File Open
=================
File handling is an important part of any web application.

Python has several functions for creating, reading, updating,
and deleting files.


File Handling
==============
The key function for working with files in Python is the
'open()' function. It takes two parameters: 'filename' and 'mode'.

There are four different modes for opening a file:
"x" - Create - Creates the specified file, returns an error if the file exists
"r" - Read   - Default value. Opens a file for reading, raise error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write  - Opens a file for writing, creates the file if it does not exist

In addition, you can specify if the file should be handled as binary or text mode

"t" - Text   - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)


Syntax
=======
To open a file for reading it is enough to specify the name of the file:"""

print('-' * 50)

try:
    file = open("demo1.txt")
except:
    print('FileNotFoundError: File does not exist')
else:
    print('File found, terminated')
    print('-' * 50)
    print(file.read())  # to read the file

print('-' * 50)

""" The code above is the same as: """

file = open("demo2.txt", "rt")
print(file.read())  # to read the file

print('-' * 50)

# file is an object,

# this command output all methods and properties about this file object
print(dir(file))

print('-' * 50)

# this command output detailed information about methods and properties about this file object
print("help(file) = ", help(file))

""" Because "r" for read, and "t" for text are the default values, 
you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.

"""
