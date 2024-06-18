from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def widgets():
    # Header Label
    b = Label(a, text="YouTube Video Downloader", padx=15, pady=15, font=("Times New Roman", 12, "bold"), bg="purple", fg="white")
    b.grid(row=1, column=1, padx=10, columnspan=3)
    
    # Link Label
    c = Label(a, text="YouTube Link", padx=15, pady=15, font=("Times New Roman", 12, "bold"), bg="purple", fg="brown")
    c.grid(row=2, column=0, padx=5, pady=5)
    
    # Download path Label
    d = Label(a, text="Download Path", padx=9, pady=5, font=("Times New Roman", 12, "bold"), bg="purple",
        fg="blue")
    d.grid(row=3, column=0, padx=9, pady=5)
    
    # Entry field for link label
    a.linkText = Entry(a, width=35, textvariable=video_link, font="Cambria 14")
    a.linkText.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
    
    # Entry field for Download path
    a.destinationText = Entry(a, width=27, textvariable=download_path, font=("Cambria 14"))
    a.destinationText.grid(row=3, column=1, padx=5, pady=5)
    
    # Browse the directory
    e = Button(a, text="Browse", command=Browse, width=10, bg="bisque", relief=GROOVE)
    e.grid(row=3, column=2, padx=1, pady=1)
    
    # Download Button
    f = Button(a, text="Download Video", command=Download, width=20, bg="thistle1", padx=10, pady=10, relief=GROOVE, font="Cambria 13")
    f.grid(row=4, column=1, padx=20, pady=20)

def Browse():
    # To browse the folders and select the folder path
    download_dir = filedialog.askdirectory(initialdir=".", title="Save video")
    download_path.set(download_dir)

def Download():
    try:
        # Getting user-input YouTube link
        youtube_link = video_link.get()
        # Selecting the optimal location for saving file
        download_folder = download_path.get()
        
        # Creating object of YouTube
        get_video = YouTube(youtube_link)
        
        # Getting the first available video stream
        video_stream = get_video.streams.first()
        
        # Downloading the video to destination directory
        video_stream.download(download_folder)
        
        # Displaying the message
        messagebox.showinfo("Success", "Downloaded and Saved In\n" + download_folder)
    except VideoUnavailable:
        messagebox.showerror("Error", "Video unavailable. Please check the URL.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

a = tk.Tk()
a.geometry("720x520")
a.resizable(False, False)
a.title("YouTube Downloader")
a.config(bg="purple")

video_link = StringVar()
download_path = StringVar()

widgets()
a.mainloop()
