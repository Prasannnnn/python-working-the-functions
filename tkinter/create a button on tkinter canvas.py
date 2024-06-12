from tkinter import *

a = Tk()


a.geometry("500x300")


title = Label(a,text="Python Programming",bg="purple",font=("bold",30))
title.pack()

b = Canvas(a , width=330,height=200,bg="brown")
b.place(x=50,y=50)

c = Button(a, text="welcome to coding",width=40,height=5,bd=10,command=a.destroy)

c.place(x=65,y=100)


a.mainloop()