from tkinter import *

from pytube import YouTube

import tkinter as tk
from tkinter import messagebox,filedialog


def widgets():
    #header Label 
    b = Label(a, text="Youtube Video Downloader",padx=15,pady=15,font=("Time New Roman",12,"bold"),bg="purple",fg="White")
    b.grid(row=1,column=1,padx=10,columnspan=3)
    #Link Label 
    c = Label(a, text="Youtube Link", padx=15,pady=15,font=("Time New Roman",12,"bold"),bg = "purple",fg="Brown")
    c.grid(row=2,column=0,padx=5,pady=5)
    #Download path Label
    d = Label(a, text="Download Path ", padx=9,pady=5, font=("Time New Roman",12,"bold"),bg="purple",fg = "Blue")
    d.grid(row=3,column=0,padx=9,pady=5)
    #Entry field for link label
    a.linkText = Entry(a,width=35,textvariable=video_link,font="Cambria 14")
    a.linkText.grid(row=2,column=1,padx=5,pady=5,columnspan=2)
    #Entry field for Download path
    a.destinationText = Entry(a,width=27,textvariable=download_path,font=("Cambria 14"))
    a.destinationText.grid(row=3,column=1,padx=5,pady=5)
    #Browse the directory
    e = Button(a,text="Browse",command=Browse,width=10,bg="bisque",relief=GROOVE)
    e.grid(row=3,column=2,padx=1,pady=1)
    #Download Button
    f = Button(a,text="Download Video",command=Download,width=20,bg="thistle1",padx=10,pady=10,relief=GROOVE,font="Cambria 13")
    f.grid(row=4,column=1,padx=20,pady=20)

def Browse():
    #to browse the folders select the folder path
    download_dirt =  filedialog.askdirectory(initialdir=r"C:\Users\Prasanna\Intern\Python\Videos",title="save video")
    download_path.set(download_dirt)

def Download():
    #getting user-input youtube link
    youtube_link = video_link.get()
    #select the optimal location for saving life
    download_folder = download_path.get()
    #creating object of youtube
    getVideo = YouTube(youtube_link)
    #getting all the video streams of the youtube videos and selecting the first from the 
    videoStream = getVideo.streams.first()
    #downloading the video to destination
    #directory
    videoStream.download(download_folder)
    #displaying the message
    messagebox.showinfo("Successfully","Download and Saved IN\n"+download_folder)


    
    
a = tk.Tk()

a.geometry("720x520")

a.resizable(False,False)

a.title("Youtube Downloader")

a.config(bg="purple")

video_link = StringVar()
download_path = StringVar()

widgets()

a.mainloop()