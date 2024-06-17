from tkinter import *

import calendar



def show_cal():
    b = Tk()

    b.config(bg="purple")

    b.title("CALENDAR")

    b.geometry("500x600")

    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(b,text=cal_content,font=("Time New Roman" ,12 ,"bold"))

    cal_year.grid(row=5,column=1,padx=20)

    b.mainloop()



a = Tk()

a.title("Calendar")

a.config(bg="grey")

a.geometry("200x200")

cal = Label(a,text="CALENDAR",bg="Dark Blue",font=("Time New Roman",15,"bold"))

year = Label(a,text="Enter year",bg="Light green")

year_field = Entry(year)

show = Button(a,text="Show Calendar",fg="Black",bg="Red",command=show_cal)

Exit = Button(a,text="EXIT",fg="black",bg="red",command=exit)

cal.grid(row = 1, column = 1)
 
year.grid(row = 2, column = 1)
 
year_field.grid(row = 3, column = 1)
 
show.grid(row = 4, column = 1)
 
Exit.grid(row = 6, column = 1)
     


a.mainloop()