from tkinter import *

import tkinter as tk

a = tk.Tk()

#creating object of image class
#image should be same folder
#in which script is saved
b = PhotoImage(file=r"python-working-the-functions\tkinter\images tkinter\MC.png")
a.iconphoto(False,b)

c = Button(a, text="Click Me",command=a.destroy)
c.pack(side=TOP)


a.mainloop()