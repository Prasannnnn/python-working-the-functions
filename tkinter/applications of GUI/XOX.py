from tkinter import *

import tkinter as ttk
from tkinter import messagebox

a = Tk()

a.title("XOX Game")

a.geometry("345x375")

def checkwinner():
    if (but1['text'] == "X" and but2['text'] == "X" and but3['text'] == "X" or
        but4['text'] == "X" and but5['text'] == "X" and but6['text'] == "X" or
        but7['text'] == "X" and but8['text'] == "X" and but9['text'] == "X" or
        but1['text'] == "X" and but4['text'] == "X" and but7['text'] == "X" or
        but2['text'] == "X" and but5['text'] == "X" and but8['text'] == "X" or
        but3['text'] == "X" and but6['text'] == "X" and but9['text'] == "X" or
        but1['text'] == "X" and but5['text'] == "X" and but9['text'] == "X" or
        but3['text'] == "X" and but5['text'] == "X" and but7['text'] == "X" ):
        messagebox.showinfo("Winner","Player 1 Wins X")
    elif(but1['text'] == "O" and but2['text'] == "O" and but3['text'] == "O" or
        but4['text'] == "O" and but5['text'] == "O" and but6['text'] == "O" or
        but7['text'] == "O" and but8['text'] == "O" and but9['text'] == "O" or
        but1['text'] == "O" and but4['text'] == "O" and but7['text'] == "O" or
        but2['text'] == "O" and but5['text'] == "O" and but8['text'] == "O" or
        but3['text'] == "O" and but6['text'] == "O" and but9['text'] == "O" or
        but1['text'] == "O" and but5['text'] == "O" and but9['text'] == "O" or
        but3['text'] == "O" and but5['text'] == "O" and but7['text'] == "O" ):
        messagebox.showinfo("Winner","Player 2 Wins O")


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

    checkwinner()
a.mainloop()