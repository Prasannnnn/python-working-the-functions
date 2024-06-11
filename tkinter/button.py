from tkinter import *

a = Tk()

a.title("Button")

b = Label(a,text="Button")
b.grid(column=0,row=1)

c = Button(a,text="check me",bg="hotpink",fg="purple")
c.grid(column=0, row=2)

a.geometry("300x300")

a.mainloop()