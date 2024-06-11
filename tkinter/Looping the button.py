# Import package and it's modules 
from tkinter import *


# text_update function 
def text_updation(language): 
	text.delete(0, END) 
	text.insert(0, language) 

# create root window 
root = Tk() 

# root window title and dimension 
root.title("Prasanna") 

# Set geometry (widthxheight) 
root.geometry('400x400') 

# Entry Box 
text = Entry(root, width=30, bg='White') 
text.pack(pady=10) 

# create buttons 
button_dict = {} 
words = ["Python", "Java", "R", "JavaScript"] 
for lang in words: 
	
	# pass each button's text to a function 
	def action(x = lang): 
		return text_updation(x) 
		
	# create the buttons 
	button_dict[lang] = Button(root, text = lang, 
							command = action) 
	button_dict[lang].pack(pady=10) 

# Execute Tkinter 
root.mainloop()
