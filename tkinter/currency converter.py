from tkinter import *
from tkinter import ttk
#import Libraries of currency converter
from currency_converter import CurrencyConverter
import os
#assign tk values
root=Tk()
root.title("Currency converter")
#class function
class Currency(object):
    def __init__(self,master) -> None:
        frame=Frame(master)
        frame.grid()
        self.currency = CurrencyConverter()
        self.options=["INR","EUR","CAD","NZD","CNY","AUD","DKK"]#INR as ind ,EUR as European,
        #CAD as canadian dollars,NZD as Newzealand,CNY as chinese yuvan,DKK as danish krone

        self.amount_label = Label(root, text="Amount: ",font=("verdana",12))
        self.amount_label.grid(row=0,column=0)
        self.amount_entry=Entry(root)
        self.amount_entry.grid(row=0,column=1)

        self.selection_frame=LabelFrame(root,text="Currencies :",font=("verdana",12))
        self.selection_frame.grid(row=1, column=0,columnspan=2)
        self.from_label=Label(self.selection_frame,text="From :",font=("verdana",12))
        self.from_label.grid(row=0,column=0)
        self.to_label=Label(self.selection_frame,text="To :",font=("verdana",12))
        self.to_label.grid(row=0,column=1)

        self.from_menu = ttk.Combobox(self.selection_frame, values=self.options)
        self.from_menu.grid(row=1,column=0)
        self.from_menu.current(1)
        self.to_menu = ttk.Combobox(self.selection_frame, values=self.options)
        self.to_menu.grid(row=1,column=1)
        self.to_menu.current(1)

        self.result_label=Label(root,text=f" ")
        self.result_label.grid(row=2,column=0,columnspan=2)
        self.convert_button=Button(root,text="Convert",command=self.converter)
        self.convert_button.grid(column=0,row=3,columnspan=2)
#converter currencies
    def converter(self):
        try:
            currency_result = round(self.currency.convert(float(self.amount_entry.get()), self.from_menu.get(), self.to_menu.get()), 2)
            self.result_label.configure(text=f"{currency_result}  {self.to_menu.get()}")
        except ValueError:
            self.result_label.configure(text="Value Error")

#call the main functions
if __name__=='__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    Currency(root)
    root.mainloop()

