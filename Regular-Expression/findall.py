'''
The findall() Function
The findall() function returns a list containing all matches.
'''
import re

a = "I cant relate despression"
b = re.findall("at",a)
print(b)
'''
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:
'''

import re

y = "The rain in Spain"
x = re.findall("Portugal", y)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")