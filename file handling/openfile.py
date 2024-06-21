'''
open a file on a server
Assume we have the following file, located in the same folder as Python:

To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

a = open("file.txt","r")
print(a.read())
'''
a = open("file.txt","r")
print(a.read())