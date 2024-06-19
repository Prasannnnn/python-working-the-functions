import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def undo_action():
    text_area.event_generate("<<Undo>>")

def redo_action():
    text_area.event_generate("<<Redo>>")

def about_app():
    messagebox.showinfo("About Notepad", "This is a simple Notepad application created using Tkinter.")

root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: text_area.delete(1.0, tk.END), accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo_action, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=redo_action, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
# Add any view-related options here (e.g., toggle status bar)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About Notepad", command=about_app)

root.mainloop()
