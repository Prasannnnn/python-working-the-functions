'''
The Split Function returns a lists where the string has been split at each match
'''

import re 
txt = "the rain in spain"
x= re.split("\s",txt)
print(x)
'''
You can control the number of occurrences by specifying the maxsplit parameter:
'''
import re 
a = "the rain in spain"
b = re.split("\s",a,1)
print(b)