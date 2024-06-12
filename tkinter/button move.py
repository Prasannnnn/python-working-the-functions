
# Importing tkinter module 
from tkinter import *
# Importing random module
import random
 
# Creating a tkinter window
a = Tk() 
 
# Initialize tkinter window with dimensions 300 x 250
a.geometry('300x250')

Label(a,text="will you accept me").pack()

Button(a,text="yes",command=a.destroy).pack()
 
# Creating a Button
btn = Button(a, text = 'No')
btn.pack()
 
# Defining method on click
def Clicked(event):
    x = random.randint(50,250)
    y = random.randint(50,200)
    btn.place(x=x, y=y)
     
     
# bind button
btn.bind("<Button-1>" ,Clicked)
btn.pack()
 
a.mainloop()