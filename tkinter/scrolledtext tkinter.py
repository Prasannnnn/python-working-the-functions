import tkinter as tk

from tkinter import ttk

from tkinter import scrolledtext


a = tk.Tk()

a.title("Scrolled Text widget")

ttk.Label(a,text="scrolled text widget  ",font=("Times New Roman",15)).grid(column=0,row=0)

ttk.Label(a,text="Enter your Comments", font=("Bold",12)).grid(column=0,row=1)

b = scrolledtext.ScrolledText(a,wrap=tk.WORD,width=40,height=8,
                              font=("Times New Roman",15))

b.grid(column=0,row=2,pady=10,padx=10)

b.focus()

b.mainloop()





a.mainloop()