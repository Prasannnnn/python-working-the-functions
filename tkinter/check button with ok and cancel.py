from tkinter import Tk,RIGHT,BOTH,RAISED
from tkinter.ttk import Frame,Button,Style

class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("buttons")
        self.style=Style()
        self.style.theme_use("default")

        frame=Frame(self,relief=RAISED,borderwidth=1)
        frame.pack(fill=BOTH,expand=True)

        self.pack(fill=BOTH,expand=True)

        closeButton=Button(self,text="close")
        closeButton.pack(side=RIGHT,padx=10,pady=10)
        okbutton=Button(self,text="ok")
        okbutton.pack(side=RIGHT)

def main():
    root=Tk()
    root.geometry("400x500+300+300")
    app=Example()
    root.mainloop()

if __name__ =='__main__':
    main()


    