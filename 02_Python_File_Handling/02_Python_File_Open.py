# bin/bash !
# Daniel OUATTARA
# 30 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


"""
Open a File on the Server
=========================
Assume we have the following file, located in
the same folder as Python: demofile.txt """

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

""" To open the file, use the built-in open() function.
The open() function returns a file object, which has a 
read() method for reading the content of the file:

Example: """

print(70 * '-')

f = open("demofile.txt", "r")
print(help(f))

print(70 * '-')
demofile = f.read()
print(demofile)

print(70 * '-')

""" If the file is located in a different location, 
you will have to specify the file path, like this:

Example:  Open a file on a different location:"""

# relative path
f = open('./my_files/welcome.txt', "r")
print(f.read())

print(5 * '~')

# absolute path
# f = open("C:\\Users\\DBO\\Desktop\\COMPUTING\\PYTHON\\w3schools.com Python3.8\\02_Python_File_Handling\\my_files\\welcome.txt", "r")
# f = open("C:/Users/DBO/Desktop/COMPUTING/PYTHON/w3schools.com Python3.8/02_Python_File_Handling/my_files/welcome.txt", "r")

f2 = open('/home/daniel/Documents/Computing/PYTHON/w3schools.com '
          'Python3.8/env/02_Python_File_Handling/my_files/welcome.txt')
print(f2.read())

print(70 * '-')

# f = open(r"C:\Users\DBO\Desktop\COMPUTING\PYTHON\w3schools.com Python3.8\02_Python_File_Handling\my_files\welcome.txt", "r")
# print(f.read())

# print(70 * '-')


"""Read Only Parts of the File
==============================
By default the read() method returns the whole text, but 
you can also specify how many characters you want to return:

Example: Return the 11 first characters of the file:"""

f = open("demofile.txt", "r")
print(f.read(11))

print(70 * '~')

""" Read Lines
================
You can return one line by using the 'readline()' method:

Example: Read one line of the file:"""

file = open("demofile.txt", "r")
print(file.readline())

print(70 * '-')

""" By calling readline() two times, you can read the two first lines:

Example: Read two lines of the file:"""

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print(70 * '-')

""" By looping through the lines of the file, you can read the whole 
file, line by line:

Example: Loop through the file line by line:"""

f = open("demofile.txt", "r")
for x in f:
    x = x.rstrip()
    print(x)

print(70 * '-')


""" Close Files
===============
It is a good practice to always close the file when you are done with it.

Example: Close the file when you are finish with it:"""

f = open("demofile.txt", "r")
print(f.readline())
f.close()

print(70 * '-')

"""Note: You should always close your files, in some cases, due to 
         buffering, changes made to a file may not show until you 
         close the file. """
