'''
What is Frame in Tkinter?
A frame is a rectangular region on the screen. 
A frame can also be used as a foundation class to implement complex widgets. 
It is used to organize a group of widgets.
'''

'''
Tkinter Frame Options
The following are commonly used Options that can be used with this widget:

bg: This option used to represent the normal background color displayed behind the label and indicator.
bd: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
cursor: By using this option, the mouse cursor will change to that pattern when it is over the frame.
height: The vertical dimension of the new frame.
highlightcolor: This option used to represent the color of the focus highlight when the frame has the focus.
highlightthickness: This option used to represent the color of the focus highlight when the frame does not have focus.
highlightbackground: This option used to represent the thickness of the focus highlight..
relief: The type of the border of the frame. It’s default value is set to FLAT.
width: This option used to represents the width of the frame.
'''


import tkinter as tk

# Function to create widgets with all options
def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

# Create the main window
window = create_widget(None, tk.Tk)
window.title("tkinter GUI ")

# Create a Frame widget with all options
frame = create_widget(window, tk.Frame, bg='lightblue', bd=3, cursor='hand2', height=100, 
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                      relief=tk.RAISED, width=200)
frame.pack(padx=20, pady=20)

# Create Label widget with all options
label = create_widget(frame, tk.Label, text='Coding and Programming', font='50', bg='lightblue', bd=3, cursor='hand2',
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                      relief=tk.RAISED)
label.pack()

# Create a frame for buttons
button_frame = create_widget(window, tk.Frame, bg='lightblue', bd=3, cursor='hand2', height=50, 
                              highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                              relief=tk.RAISED, width=200)
button_frame.pack(pady=10)

# Function to create buttons with all options
def create_button(parent, text, fg):
    return create_widget(parent, tk.Button, text=text, fg=fg, bg='lightblue', bd=3, cursor='hand2',
                         highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                         relief=tk.RAISED)

# Create buttons
buttons_info = [("Python", "red"), ("R", "brown"), ("Java", "blue"), 
                ("Javascript", "green"), ("Django", "green"), ("HTML", "green")]

for text, fg in buttons_info:
    button = create_button(button_frame, text=text, fg=fg)
    button.pack(side=tk.LEFT)

# Run the Tkinter event loop
window.mainloop()
