'''
Using the insert method
'''


import tkinter as tk 


root = tk.Tk() 
root.geometry("200x100") 

textBox = tk.Entry(root) 
textBox.insert(0, "This is the default text") 
textBox.pack() 
root.mainloop() 


'''
Using the stringvar method
'''

import tkinter as tk 


root = tk.Tk() 
root.geometry("200x100") 

text = tk.StringVar() 
text.set("This is the default text") 
textBox = tk.Entry(root,textvariable = text) 

textBox.pack() 

root.mainloop() 
