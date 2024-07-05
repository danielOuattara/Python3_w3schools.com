# !bin/bash
# Daniel OUATTARA
# 27 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/

import json

print(70 * '-')

"""
Python JSON
============

JSON is a syntax used for storing and exchanging data.
JSON is text, written with JavaScript object notation.

JSON in Python
===============

Python has a built-in package called json, which can be 
used to work with JSON data.

Example: Import the json module:

# import json
 
Parse JSON - Convert from JSON to Python
=========================================

memo technics: 
---------------
- load to Python (Deserialize s, to a Python object.)
- dump from Python (Serialize obj to a JSON formatted str)

If you have a JSON object, you can parse it by using the 
json.loads() method. The result will be a Python dictionary.

Example: Convert from JSON to Python:
"""

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print("JSON string: ", x)

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("Python dict: ", y)
print(y['age'])

print(70 * '-')

""" 
Convert from Python to JSON
=============================

If you have a Python object, you can convert it into a JSON 
string by using the json.dumps() method.

Example: Convert from Python to JSON:

"""

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("python object : ", x)

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("json string : ", y)

print(70 * '-')

"""
Example: Convert Python objects into JSON strings, and print 
the values: """

# import json

# dict
print(dict(name="John", age=30))
print(json.dumps({"name": "John", "age": 30}))
print("---")

# list
print(["apple", "bananas"])
print(json.dumps(["apple", "bananas"]))
print("---")

# tuple
print(("apple", "bananas"))
print(json.dumps(("apple", "bananas")))
print("---")

# string
print("hello")
print(json.dumps("hello"))
print("---")

# int
print(42)
print(json.dumps(42))
print("---")

# float
print(31.76)
print(json.dumps(31.76))
print("---")

# Boolean
print(True)
print(json.dumps(True))
print("---")

# Boolean
print(False)
print(json.dumps(False))
print("---")

# None
print(None)
print(json.dumps(None))

print(70 * '-')

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

Example: Convert a Python object containing all the legal 
data types:
"""

# import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(x)
print(json.dumps(x))
print('---')

""" 
Format the json.dumps() result
================================

The example above prints a JSON string, but it is not 
very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier 
to read the result:

Example: Use the 'indent' parameter to define the numbers 
         of indents:"""

print(json.dumps(x, indent=2))

print(70 * '-')

"""
You can also define the separators, default value is 
(", ", ": "), which means using a comma and a space to 
separate each object, and a colon and a space to separate 
keys from values:

Example: Use the separators parameter to change the default 
         separator:
"""
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print(70 * '-')

""" 
Order the Result
=================

The json.dumps() method has parameters to order the keys in 
the result.

Example: Use the 'sort_keys' parameter to specify if the result 
         should be sorted or not:"""

print(json.dumps(x, indent=2, sort_keys=True))

print(70 * '-')

# for item in dir(json):
#     print(item)

"""
JSONDecodeError
JSONDecoder
JSONEncoder
__all__
__author__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
__version__
_default_decoder
_default_encoder
codecs
decoder
detect_encoding
dump
dumps
encoder
load
loads
scanner
"""

print(help(json.dump), '\n\n')
print(help(json.dumps), '\n\n')
print(help(json.load), '\n\n')
print(help(json.loads), '\n\n')



