from tkinter import *

a = Tk()


Button(a,relief=RAISED,bitmap="error").pack(pady=10)
Button(a,relief=RAISED,bitmap="hourglass").pack(pady=10)
Button(a,relief=RAISED,bitmap="info").pack(pady=10)
Button(a,relief=RAISED,bitmap="question").pack(pady=10)
Button(a,relief=RAISED,bitmap="warning").pack(pady=10)
Button(a,relief=RAISED,bitmap="gray75").pack(pady=10)
Button(a,relief=RAISED,bitmap="gray50").pack(pady=10)
Button(a,relief=RAISED,bitmap="gray25").pack(pady=10)
Button(a,relief=RAISED,bitmap="questhead").pack(pady=10)

a.mainloop()