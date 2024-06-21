'''
open a file on a server
Assume we have the following file, located in the same folder as Python:

To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

a = open("file.txt","r")
print(a.read())
'''
# a = open(r"demo.txt","r")
# print(a.read())

'''
If the file is located in a different location, you will have to specify the file path, like this:
'''
# b = open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\file handling\demo.txt","r")
# print(b.read())

'''
Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:

Example
Return the 5 first characters of the file:
'''


# f = open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\file handling\demo.txt", "r")
# print(f.read(1000))


'''
Read Lines
You can return one line by using the readline() method:

Example
Read one line of the file:


'''

# f = open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\file handling\demo.txt", "r")
# print(f.readline())

'''
By calling readline() two times, you can read the two first lines:
'''

# f = open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\file handling\demo.txt", "r")
# print(f.readline())
# print(f.readline())

'''
By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:
'''
# f = open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\file handling\demo.txt", "r")
# for x in f:
#   print(x)


'''
Close Files
It is a good practice to always close the file when you are done with it.

Example
Close the file when you are finish with it:


'''
f = open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\file handling\demo.txt", "r")
print(f.readline())
f.close()
