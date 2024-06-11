from tkinter import *


a = Tk()

a.geometry("300x300")

def button(press):
    print(press)


b = Button(a,text="Python",command=lambda m = "Python":button(m))
b.grid(padx=10,pady=10)

c = Button(a,text="Data Analysis",command=lambda m="Data Analysis":button(m))
c.grid(padx=10,pady=10)



a.mainloop()





