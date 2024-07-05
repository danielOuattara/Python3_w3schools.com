# !bin/bash
# Daniel OUATTARA
# 27 03 2022
# 01-Python Tutorial-Python3.x
# w3schools.com/python/


import datetime

"""

Python Datetime
================

Python Dates
=============

A date in Python is not a data type of its own, but we
can import a module named 'datetime' to work with dates
as date objects.

Example: Import the 'datetime' module and display the 
         current date.

"""

x = datetime.datetime.now()
print(x)

print(70 * '-')


"""
Date Output
=============

When we execute the code from the example above the result 
will be: 2022-03-27 23:17:35.351712

The date contains year, month, day, hour, minute, second, 
and microsecond.

The 'datetime' module has many methods to return information 
about the date object.

Here are a few examples, you will learn more about them later 
in this chapter:

Example: Return the year and name of weekday:

"""

x = datetime.datetime.now()
print(x.year)  # 2022
print(x.strftime("%A"))  # Sunday

print(70 * '-')


""" 
Creating Date Objects
======================

To create a date, we can use the 'datetime()' class (constructor) 
of the datetime module.

The 'datetime()' class requires three parameters to create a date: 
year, month, day.

Example: Create a date object:

"""

x = datetime.datetime(2020, 5, 17)
print(x)

print(70 * '-')

"""
The 'datetime()' class also takes parameters for time and timezone 
(hour, minute, second, microsecond, tzone), but they are all optional, 
and has a default value of 0, and None for timezone.


The strftime() Method
========================

The datetime object has a method for formatting date objects into 
readable strings. The method is called strftime(), and takes one 
parameter: the format, to specify the format of the returned string:

Example: Display the name of the month:

"""

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

print(70 * '-')

"""
A reference of all the legal format codes:

Directive   Description 	                       Example 
------------------------------------------------------------
%a 	        Weekday, short version 	               Wed
------------------------------------------------------------	
%A 	        Weekday, full version 	               Wednesday
------------------------------------------------------------	
%w 	        Weekday as a number 0-6,               0 is Sunday
------------------------------------------------------------ 
%d 	        Day of month 01-31 	                   31
------------------------------------------------------------
%b 	        Month name, short version              Dec      
------------------------------------------------------------      
%B 	        Month name, full version 	           December
------------------------------------------------------------
%m 	        Month as a number 01-12 	           12
------------------------------------------------------------
%y 	        Year, short version, without century   18
------------------------------------------------------------
%Y 	        Year, full version 	                   2018
------------------------------------------------------------
%H 	        Hour 00-23 	                           17
------------------------------------------------------------
%I 	        Hour 00-12 	                           05
------------------------------------------------------------
%p 	        AM/PM 	                               PM
------------------------------------------------------------
%M 	        Minute 00-59 	                       41
------------------------------------------------------------
%S 	        Second 00-59 	                       08
------------------------------------------------------------
%f 	        Microsecond 000000-999999 	           548513
------------------------------------------------------------
%z 	        UTC offset 	                           +0100
------------------------------------------------------------
%Z 	        Timezone 	                           CST
------------------------------------------------------------
%j 	        Day number of year 001-366 	           365
------------------------------------------------------------
%U 	        Week number of year, Sunday as 
            the first day of week, 00-53 	       52
------------------------------------------------------------
%W 	        Week number of year, Monday as 
            the first day of week, 00-53 	       52
------------------------------------------------------------
%c 	        Local version of date and time 	
            Mon Dec 31 17:41:00                    2018
------------------------------------------------------------
%C 	        Century 	                           20
------------------------------------------------------------
%x 	        Local version of date 	               12/31/18
------------------------------------------------------------
%X 	        Local version of time 	               17:41:00
------------------------------------------------------------
%% 	        A % character 	                       %
------------------------------------------------------------
%G 	        ISO 8601 year 	                       2018
------------------------------------------------------------
%u 	        ISO 8601 weekday (1-7) 	               1
------------------------------------------------------------
%V 	        ISO 8601 weeknumber (01-53) 	       01 	
------------------------------------------------------------
"""

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%a"))  # Fri
print(x.strftime("%A"))  #
print(x.strftime("%w"))  #
print(x.strftime("%W"))  #
print(x.strftime("%d"))  #
print(x.strftime("%b"))  #
print(x.strftime("%B"))  #
print(x.strftime("%m"))  #
print(x.strftime("%y"))  #
print(x.strftime("%Y"))  #
print(x.strftime("%H"))  #
print(x.strftime("%I"))  #
print(x.strftime("%p"))  #
print(x.strftime("%M"))  #
print(x.strftime("%S"))  #
print(x.strftime("%f"))  #
print(x.strftime("%z"))  #
print(x.strftime("%Z"))  #
print(x.strftime("%j"))  #
print(x.strftime("%U"))  #
