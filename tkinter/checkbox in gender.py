from tkinter import*

master=Tk()

def var_state():
    print("male:%d,\nfemale:%d " %(var1.get(),var2.get()))

Label(master,text="your gender:").grid(row=0,sticky=W)
var1=IntVar()

Checkbutton(master,text="male", variable=var1).grid(row=1,sticky=W)
var2=IntVar()
Checkbutton(master,text="female", variable=var2).grid(row=2,sticky=W)
Button(master,text="quit",command=master.quit).grid(row=3,sticky=W,pady=4)
Button(master,text="show",command=var_state).grid(row=4,sticky=W,pady=4)

mainloop()