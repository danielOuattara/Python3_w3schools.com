# Daniel OUATTARA
# 30 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

import os

"""

Python Delete File
========================
To delete a file, you must import the OS module,
and run its os.remove() function:

Example: Remove the file "demofile_test.txt": """

#  import os

# os.remove("demofile_test.txt")

""" Check if File exist:
==========================
To avoid getting an error, you might want to check 
if the file exists before you try to delete it:

Example: Check if file exists, then delete it: """

#  import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

try:
    os.remove('demofile.txt')
except:
    print('FileNotFoundError')

""" Delete Folder
====================
To delete an entire folder, use the os.rmdir() method:

Example: Remove the folder "my_folder":"""

# import os
# os.rmdir("my_folder")

if os.path.exists("my_folder_2"):
    os.rmdir("my_folder_2")
else:
    print('my_folder_2 does not exist')

try:
    os.rmdir("my_folder_3")
except:
    print('my_folder_3 does not exist')
