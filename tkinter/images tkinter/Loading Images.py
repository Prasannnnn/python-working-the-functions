from tkinter import *

from PIL import ImageTk,Image

from tkinter import filedialog

def upload_file():
    #select imagename from a folder
    x = openfilename()

    img = Image.open(x)

    img = img.resize((250,250),Image.LANCZOS)

    img = ImageTk.PhotoImage(img)

    panel = Label(a,image=img)

    panel.image = img

    panel.grid(row=2)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title ='"pen')
    return filename


a=Tk()

a.title("Image Loader")

a.geometry("550x300+300+150")

a.resizable(width=True,height=True)

b = Button(a,text="upload a file",command=upload_file).grid(row=1,columnspan=4)







a.mainloop()
