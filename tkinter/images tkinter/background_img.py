from tkinter import *

a = Tk()

a.title("Background Image")

bg = PhotoImage(file=r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\tkinter\images tkinter\image.png")

b = Label(a,image=bg)
b.place(x=0,y=0)

c = Label(a,text="Welcome")
c.pack(pady=50)

d = Frame(a)
d.pack(pady=20)

# Add buttons 
button1 = Button(d,text="Exit",command=a.destroy) 
button1.pack(pady=20) 
  
button2 = Button(d, text = "Start") 
button2.pack(pady = 20) 
  
button3 = Button(d, text = "Reset") 
button3.pack(pady = 20) 

a.mainloop()