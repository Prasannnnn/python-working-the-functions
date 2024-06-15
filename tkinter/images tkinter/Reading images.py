import tkinter as tk
from PIL import ImageTk,Image
import os


a = tk.Tk()

a.title("Reading Images")

img =ImageTk.PhotoImage(Image.open(r"python-working-the-functions\tkinter\images tkinter\image.png"))

panel = tk.Label(a,image=img)

panel.pack(side="bottom",fill="both",expand="yes")

a.mainloop()