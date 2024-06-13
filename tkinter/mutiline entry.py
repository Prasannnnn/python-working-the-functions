import tkinter as tk
from tkinter import ttk

a=tk.Tk()

a.title("Multiline Entry")

a.geometry("400x300")

ttk.Label(a,text="Enter your comment: ",font=("Times New Roman",15)).grid(column=0,row=5,padx=10,pady=25)

#test widget

b=tk.Text(a,width=20,height=3)

b.grid(column=1,row=5)

a.mainloop()