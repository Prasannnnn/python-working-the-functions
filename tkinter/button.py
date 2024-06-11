from tkinter import *

a = Tk()

a.title("Button")

def buttonclick():
    print("Click me clicked")

b = Label(a,text="Button")
b.grid(column=0,row=1)

c = Button(a,text="quit",bg="hotpink",fg="purple",command=a.destroy)
c.grid(column=0, row=2)


d = Button(a,text="Click Me",command=buttonclick,activebackground="blue",activeforeground="white",anchor="center",bd=3,background="lightgray",cursor="hand2",disabledforeground="grey",foreground="black",font=("arial",12),height=2,highlightbackground="black",highlightcolor="green",highlightthickness=2,justify="center",overrelief="raised",padx=10,pady=5,width=15,wraplength=100)
d.grid(column=0,row=4)

a.geometry("300x300")

a.mainloop()



'''
Button(a,text="Click Me",command=buttonclick,activebackground="blue",activeforeground="white",anchor="center",bd=3,background="lightgray",cursor="hand2",disabledforeground="grey",foreground="black",font=("arial",12),height=2,highlightbackground="black",highlightcolor="green",highlightthickness=2,justify="center",overrelief="raised",padx=10,pady=5,width=15,wraplength=100)
d.grid(column=0,row=4)
Explanation of this line
Button Creation:
Button(a,....)
---> d is the button object.
---> Button() is a constructor that creates the button.
---> a is the parent widget (e.g., a window or frame) where this button will be placed
Button Properties and Configuration:
text="Click Me"
---> The text displayed on the button
command=buttonclick
---> The function to be called when the button is clicked. 
    buttonclick should be a function defined  in above code.
activebackground="blue"
---> Background color of the button when it is clicked or activated
activeforeground="white"
---> Text color of the button when it is clicked or activated
anchor="center"
---> Specifies where the text should be positioned within the button. In this case, it's centered.
bd=3
---> Border width of the button.
background="lightgray"
---> Background color of the button in its normal state
cursor="hand2"
---> Cursor style when hovering over the button. "hand2" typically looks like a pointing hand.
disabledforeground="grey"
---> Text color of the button when it is disabled
foreground="black"
---> Text color of the button in its normal state.
font=("arial", 12)
---> Font style and size of the text on the button.
height=2
---> Height of the button (measured in text lines).
highlightbackground="black"
---> Background color of the highlight border when the button has focus.
highlightcolor="green"
---> Color of the highlight border when the button has focus.
highlightthickness=2
---> Thickness of the highlight border.
justify="center"
---> Justification of the text within the button (centered).
overrelief="raised"
---> Relief style when the mouse is over the button. "raised" makes it look like it pops out.
padx=10
---> Padding in the x-direction (left and right) inside the button.
pady=5
---> Padding in the y-direction (top and bottom) inside the button.
width=15
---> Width of the button (measured in text units).
wraplength=100
---> Maximum line length for the text within the button. Text longer than this will wrap to the next line.

d.grid(column=0, row=4)
---> Places the button in the grid layout manager at column 0, row 4 of the parent widget a.


'''