from tkinter import *
import tkinter as tk

# Create main window
a = Tk()
a.geometry("500x300")
a.title("Login Form")

# Declaring string variables for username and password
name_var = tk.StringVar()
pass_var = tk.StringVar()

# Define a function that will get the name and password and print them on the screen
def sub():
    name = name_var.get()
    pasw = pass_var.get()

    print("The name is:", name)
    print("The password is:", pasw)

    name_var.set("")
    pass_var.set("")

# Creating labels and entry widgets for username and password
name_label = Label(a, text="Username", font=("Cambria", 14))
name_entry = Entry(a, textvariable=name_var, font=('calibre', 10, 'normal'))

passw_label = Label(a, text="Password", font=('calibre', 10, 'bold'))
passw_entry = Entry(a, textvariable=pass_var, font=('calibre', 10, 'normal'), show='*')

# Creating a submit button
sub_btn = Button(a, text='Submit', command=sub)

# Placing the labels and entries in the required positions using grid method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# Running the main loop for the window to display
a.mainloop()
