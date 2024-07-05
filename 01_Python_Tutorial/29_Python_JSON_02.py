# !bin/bash
# Daniel OUATTARA
# 27 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

import json

""" 
When you convert from Python to JSON, Python objects 
are converted into the JSON (JavaScript) equivalent:

Python 	JSON
---------------
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null


The json module provides a simple way to work with JSON data. 

JSON (JavaScript Object Notation) is a popular data interchange 
format that's easy for humans to read and write and easy for 
machines to parse and generate.

Here are some of the key methods and functions provided by the 
json module:

1. json.load(fp)
-----------------

This method is used to parse a JSON file (or file-like object) 
and convert it into a Python dictionary or list. 

The fp parameter should be a readable file-like object. 

"""

with open('29_data_01.json', 'r') as file:
    data = json.load(file)

print('\n', data, '\n')

"""

2. json.loads(s)
-----------------

This method parses a JSON-formatted string and converts it into 
a Python dictionary or list. 

The s parameter should be a valid JSON string.

"""

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data, '\n')

"""

3. json.dump(obj, fp)
----------------------

This method converts a Python dictionary or list to a 
JSON-formatted string and writes it to a file. 

The obj parameter is the Python object to be serialized, 
and fp is a writable file-like object.

"""

data = {"name": "John", "age": 30, "city": "New York"}

with open('29_data_02.json', 'w') as file:
    json.dump(data, file)
print('convert to JSON & write to file: completed !\n')

"""

4. json.dumps(obj)
-------------------

This method converts a Python dictionary or list to a 
JSON-formatted string. 

The obj parameter is the Python object to be serialized.

"""

data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string, '\n')

"""

Additional Parameters:
-----------------------
Both dump and dumps methods have several optional parameters 
that can be useful:

- indent: Adds indentation to the JSON output for readability.
- separators: Changes the item separator and key-value separator 
              in the JSON output.
- sort_keys: If True, the output will have its keys sorted.


Example with optional parameters:
"""

data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
print(json_string)

"""

Summary of Methods:
-------------------

- json.load(fp): Read JSON data from a file and convert to a Python object.
- json.loads(s): Convert JSON string to a Python object.
- json.dump(obj, fp): Write Python object to a file as JSON.
- json.dumps(obj): Convert Python object to a JSON string.

These methods cover the basic operations you can perform with JSON data 
in Python using the json module. 
"""