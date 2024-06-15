import tkinter as tk
from PIL import ImageTk,Image

a=tk.Tk()

canva = tk.Canvas(a,width=1000,height=500)

canva.pack()

img = ImageTk.PhotoImage(Image.open(r"C:\Users\Prasanna\Intern\Python\python-working-the-functions\tkinter\images tkinter\asd.png"))

canva.create_image(135,20,anchor=tk.NW,image=img)

a.mainloop()