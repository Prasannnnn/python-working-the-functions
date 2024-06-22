'''
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned.
Example:
Search for the first white-space character in the string:
'''
import re

txt = "The rain in Spain"
sea = re.search("\s", txt)

print("The first white-space character is located in position:", sea.start())
'''
The re.search("\s", txt) function call searches for the first occurrence of any whitespace 
character (spaces, tabs, newlines, etc.) in the string txt. 
The .start() method then returns the starting index of the match, which in this case is 3.
'''