from tkinter import*
from tkinter.ttk import Combobox
window = Tk()
window.title("Registration Form")
window.geometry('500x300')

h1 = Label(window,text="Registration Form",font=('Bold',22))
h1.grid(row=0,column=0,columnspan=2,padx=5,sticky=W)

t1=Label(window,text="full name")
t1.grid(row=1,column=0,sticky=W,padx=5)

t2=Label(window,text="email")
t2.grid(row=2,column=0,sticky=W,padx=5)

t3=Label(window,text="Gender")
t3.grid(row=3,column=0,sticky=W,padx=5)

t4=Label(window,text="Country")
t4.grid(row=4,column=0,sticky=W,padx=5)

t5=Label(window,text="Programming")
t5.grid(row=5,column=0,sticky=W,padx=5)

name= StringVar()
email= StringVar()

tb1=Entry(window,textvariable=name,width=30)
tb1.grid(row=1,column=1,columnspan=2,sticky=W)

tb2=Entry(window,textvariable=email,width=30)
tb2.grid(row=2,column=1,columnspan=2,sticky=W)

r1=Radiobutton(window,text="male",value=0)
r1.grid(row=3,column=1,sticky=W)

r2=Radiobutton(window,text="female",value=1)
r2.grid(row=3,column=1,sticky=E)



combo=Combobox(window,values=['India','UAE','USA','Canada'],width=30)
combo.grid(row=4,column=1,columnspan=2,sticky=W)

c1 = Checkbutton(window,text="Java")
c1.grid(row=5,column=1,sticky=W)

c2 = Checkbutton(window,text="Python")
c2.grid(row=5,column=1,sticky=E)

def submit():
    empty.config(text="your details are saved successfully!")

b1= Button(window,text="submit",fg='White',bg='Red',command=submit)
b1.grid(row=6,column=0)

empty = Label(window,fg="Blue",font=("",15))
empty.grid(row=7,column=1,columnspan=3)

window.mainloop()