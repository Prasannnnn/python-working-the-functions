from tkinter import *

a = Tk()
a.title("manchester city")

b = PhotoImage(file=r"python-working-the-functions\tkinter\images tkinter\MC.png")
a.iconphoto(False,b)

Label(a,text="Hello world").pack
a.mainloop()