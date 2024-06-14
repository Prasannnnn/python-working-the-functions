from tkinter import *

import tkinter as tk

a = Tk()

a.title("Checkbutton checking")

def on_button_toggle():
    if var.get()==1:
        print("checkbutton is selected")
    else:
        print("checkbutton is deselected")

var = tk.IntVar()
b = tk.Checkbutton(a,text="Enable Feature",variable=var,onvalue=1,offvalue=0,command=on_button_toggle)
# Setting options for the Checkbutton
b.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)
b.config(bitmap="info",width=20,height=2)
b.pack(padx=40,pady=40)
b.flash()

a.mainloop()