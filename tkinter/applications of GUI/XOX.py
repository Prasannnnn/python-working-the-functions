from tkinter import *

import tkinter as ttk

a = Tk()

a.title("XOX Game")

a.geometry("345x375")

but1 = ttk.Button(a,text="  ",command=lambda:buttonpress(1))
but1.grid(row=0,column=0,ipadx=50,ipady=50)
but2 = ttk.Button(a,text="  ",command=lambda:buttonpress(2))
but2.grid(row=0,column=1,ipadx=50,ipady=50)
but3 = ttk.Button(a,text="  ",command=lambda:buttonpress(3))
but3.grid(row=0,column=2,ipadx=50,ipady=50)
but4 = ttk.Button(a,text="  ",command=lambda:buttonpress(4))
but4.grid(row=1,column=0,ipadx=50,ipady=50)
but5 = ttk.Button(a,text="  ",command=lambda:buttonpress(5))
but5.grid(row=1,column=1,ipadx=50,ipady=50)
but6 = ttk.Button(a,text="  ",command=lambda:buttonpress(6))
but6.grid(row=1,column=2,ipadx=50,ipady=50)
but7 = ttk.Button(a,text="  ",command=lambda:buttonpress(7))
but7.grid(row=2,column=0,ipadx=50,ipady=50)
but8 = ttk.Button(a,text="  ",command=lambda:buttonpress(8))
but8.grid(row=2,column=1,ipadx=50,ipady=50)
but9 = ttk.Button(a,text="  ",command=lambda:buttonpress(9))
but9.grid(row=2,column=2,ipadx=50,ipady=50)


player =1 
def buttonpress(ButtonNumber):
    global player
    if ButtonNumber == 1 and player == 1:
        but1.config(text="X")
        player = 2

    elif ButtonNumber == 1 and player == 2:
        but1.config(text="O")
        player = 1

    if ButtonNumber == 2 and player == 1:
        but2.config(text="X")
        player = 2

    elif ButtonNumber == 2 and player == 2:
        but2.config(text="O")
        player = 1

    if ButtonNumber == 3 and player == 1:
        but3.config(text="X")
        player = 2

    elif ButtonNumber == 3 and player == 2:
        but3.config(text="O")
        player = 1
    
    if ButtonNumber == 4 and player == 1:
        but4.config(text="X")
        player = 2

    elif ButtonNumber == 4 and player == 2:
        but4.config(text="O")
        player = 1

    if ButtonNumber == 5 and player == 1:
        but5.config(text="X")
        player = 2

    elif ButtonNumber == 5 and player == 2:
        but5.config(text="O")
        player = 1

    if ButtonNumber == 6 and player == 1:
        but6.config(text="X")
        player = 2

    elif ButtonNumber == 6 and player == 2:
        but6.config(text="O")
        player = 1
    if ButtonNumber == 7 and player == 1:
        but7.config(text="X")
        player = 2

    elif ButtonNumber == 7 and player == 2:
        but7.config(text="O")
        player = 1

    if ButtonNumber == 8 and player == 1:
        but8.config(text="X")
        player = 2

    elif ButtonNumber == 8 and player == 2:
        but8.config(text="O")
        player = 1

    if ButtonNumber == 9 and player == 1:
        but9.config(text="X")
        player = 2

    elif ButtonNumber == 9 and player == 2:
        but9.config(text="O")
        player = 1
a.mainloop()