'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

# f = open("demo2.txt", "a")
# f.write("Fifty shades of Grey songs!")
# f.close()

# #open and read the file after the appending:
# f = open("demo2.txt", "r")
# print(f.read())


f = open("demo3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demo3.txt", "r")
print(f.read())

'''
Note: the "w" method will overwrite the entire file.
'''


'''
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
'''
f = open("myfile.txt", "x")
f.write("Vanakam da mapla")
f.close()

f=open("myfile.txt","r")
print(f.read())