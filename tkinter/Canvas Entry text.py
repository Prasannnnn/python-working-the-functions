from tkinter import *
from tkinter import messagebox
app = Tk()


#create a submit function
def submit_data(): 
  
    # Show submitted message to user when button is clicked 
    messagebox.showinfo('Submitted',  
                        "Your data is submitted successfully!") 
  
    # Clear the entry widgets after data is submitted 
    entry_widget1.delete(0, END) 
    entry_widget2.delete(0, END) 

canvas_widget = Canvas(app,width=500,height=500)
canvas_widget.pack()

label_widget1 = Label(app, text="Enter your name") 
canvas_widget.create_window(150, 160, window=label_widget1) 
  
# Create and place the label in canvas 
# for user to enter his mail I'd 
label_widget2 = Label(app, text="Enter your mail I'd") 
canvas_widget.create_window(150, 200, window=label_widget2) 
  
# Create an input name on canvas 
# for inputting user name using widget Entry 
entry_widget1 = Entry(app) 
canvas_widget.create_window(300, 160, window=entry_widget1) 
  
# Creating another input name on canvas 
# for inputting user mail using widget Entry 
entry_widget2 = Entry(app) 
canvas_widget.create_window(300, 200, window=entry_widget2) 
  
# Creating and placing the button on canvas to submit data 
button_widget = Button(text='Submit', command=submit_data) 
canvas_widget.create_window(225, 250, window=button_widget) 
  
# Make the infinite loop for displaying app 
app.mainloop() 