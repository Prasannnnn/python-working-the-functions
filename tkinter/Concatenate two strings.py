'''
In this example, we take two strings as input from the user. Then, we let the user concatenate or 
compare those two strings on the basis of the button he pressed present on the app and display the result 
in the message box. 
'''

# Python program to use entry 
# box on canvas- Tkinter 

# Import the library tkinter 
from tkinter import *
from tkinter import messagebox 

# Creating an app 
app = Tk() 

# Create a function to compare the strings 
def compare_string(): 

	# Taking the value in entry widget from user 
	# and storing it in variables 
	string1 = entry_widget1.get() 
	string2 = entry_widget2.get() 

	# Check if two strings are equal or not 
	if string1 == string2: 
		a = "Strings are same"
	else: 
		a = "Strings are different"

	# Show compared result to user when button is clicked 
	messagebox.showinfo("Compared Strings", a) 

# Create a function to concat the strings 


def concat_string(): 

	# Taking the value in entry widget from user 
	# and storing it in variables 
	string1 = entry_widget1.get() 
	string2 = entry_widget2.get() 

	# Show concatenated result to user when button is clicked 
	messagebox.showinfo("Compared Strings", 
						'Concatenated String: '+string1+string2) 


# Creating and displaying a canvas 
canvas_widget = Canvas(app, width=500, 
					height=500) 
canvas_widget.pack() 

# Creating and placing the label in canvas 
label_widget1 = Label(app, text="Enter the string 1") 
canvas_widget.create_window(150, 160, 
							window=label_widget1) 

# Creating and placing the label in canvas 
label_widget2 = Label(app, text="Enter the string 2") 
canvas_widget.create_window(350, 160, 
							window=label_widget2) 

# Creating an input name on canvas 
# for input using widget Entry 
entry_widget1 = Entry(app) 
canvas_widget.create_window(150, 200, 
							window=entry_widget1) 

# Creating another input name on canvas 
# for input using widget Entry 
entry_widget2 = Entry(app) 
canvas_widget.create_window(350, 200, 
							window=entry_widget2) 

# Creating and placing the button on canvas to concat strings 
button_widget = Button(text='Concatenate the strings', 
					command=concat_string) 
canvas_widget.create_window(150, 250, window=button_widget) 

# Creating and placing the button on canvas to compare strings 
button_widget = Button(text='Compare the strings', 
					command=compare_string) 
canvas_widget.create_window(350, 250, window=button_widget) 

# Make the infinite loop for displaying app 
app.mainloop() 
