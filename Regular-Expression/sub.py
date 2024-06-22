'''
The sub() function replaces the matches with the text of your choice:

example:
Replace every white-space character with the number 9:
'''
import re 
txt = "the boys is mine"
x = re.sub("\s","9",txt)
print(x)
#You can control the number of replacements by specifying the count parameter:
import re
a = "I am great , I have powers, I did it, I am perfect"
b = re.sub("\s","9",a,2)
print(b)