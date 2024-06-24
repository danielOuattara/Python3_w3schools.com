# bin/bash !
# Daniel OUATTARA
# 30 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

"""
Python File Write
==================

Write to an Existing File
==========================
To write to an existing file, you must add a parameter
to the open() function:

"a" - Append - will append to the end of the file
"w" - Write  - will overwrite any existing content

Example : """

#  Open the file "demo3_2.txt" and append content to the file
f = open("demo3_0.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#  open and read the file after the appending:
f = open("demo3_1.txt", "r")
print(f.read())
f.close()

""" Example: """
#  Open the file "demo3_2.txt" and overwrite the content:
f = open("demo3_2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demo3_2.txt", "r")
print(f.read())
f.close()

"""Note: the "w" method will overwrite the entire file."""


""" Create a New File
======================
To create a new file in Python, use the "open()" method, 
with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write  - will create a file if the specified file does not exist

Example: Create a file called "demofile_test.txt":"""
f = open("demofile_test.txt", "x")

""" Result: a new empty file is created!

Example: Create a new file if it does not exist:"""

f = open("my_file_2.txt", "w")

