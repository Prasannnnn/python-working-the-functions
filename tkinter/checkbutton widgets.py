from tkinter import*

import  tkinter

top=Tk()

checkvar1=IntVar()
checkvar2=IntVar()
c1=Checkbutton(top,text="cad",variable=checkvar1,onvalue=1,offvalue=0,height=10,width=25 )
c2=Checkbutton(top,text="robomatiics",variable=checkvar2,onvalue=1, offvalue=0,height=10, width=25)

c1.pack()
c2.pack()
top.mainloop() 