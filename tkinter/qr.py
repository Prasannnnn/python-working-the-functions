from tkinter import *
from tkinter import filedialog, colorchooser
import qrcode
from PIL import Image, ImageTk, ImageOps

def upload_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if logo_path:
        logo_img = Image.open(logo_path)
        logo_img.thumbnail((100, 100))
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label.config(image=logo_tk)
        logo_label.image = logo_tk

def choose_qr_color():
    global qr_color
    qr_color = colorchooser.askcolor(title="Choose QR Code Color")[1]
    qr_color_label.config(bg=qr_color)

def choose_bg_color():
    global bg_color
    bg_color = colorchooser.askcolor(title="Choose Background Color")[1]
    bg_color_label.config(bg=bg_color)

def generate_qr_code():
    name = title_entry.get()
    text = text_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')

    if logo_path:
        logo = Image.open(logo_path)
        logo_size = logo_scale.get() / 100  # Scale from 0 to 1
        max_logo_size = min(img.size) * logo_size
        logo.thumbnail((max_logo_size, max_logo_size))
        logo = ImageOps.expand(logo, border=10, fill='white')  # Add white border to the logo
        logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, logo_position, logo.convert("RGBA"))

    img.save(f"qrcode/{name}.png")

    qr_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

# Main window setup
root = Tk()
root.title("QR Code Generator with Logo")
root.geometry("800x600")
root.config(bg="light blue")

# Widgets for the main window
Label(root, text="Title", fg="white", bg="black", font=15).place(x=50, y=50)
title_entry = Entry(root, width=20, font="arial 15")
title_entry.place(x=50, y=80)

Label(root, text="Text", fg="white", bg="black", font=15).place(x=50, y=130)
text_entry = Entry(root, width=20, font="arial 15")
text_entry.place(x=50, y=160)

Button(root, text="Upload Logo", width=20, height=2, bg="green", fg="white", command=upload_logo).place(x=50, y=210)

Label(root, text="QR Code Color", fg="white", bg="black", font=15).place(x=50, y=260)
qr_color_label = Label(root, bg="black", width=20, height=2)
qr_color_label.place(x=200, y=260)
Button(root, text="Choose Color", width=15, height=1, bg="blue", fg="white", command=choose_qr_color).place(x=50, y=300)

Label(root, text="Background Color", fg="white", bg="black", font=15).place(x=50, y=350)
bg_color_label = Label(root, bg="white", width=20, height=2)
bg_color_label.place(x=200, y=350)
Button(root, text="Choose Color", width=15, height=1, bg="blue", fg="white", command=choose_bg_color).place(x=50, y=390)

Label(root, text="Logo Size (%)", fg="white", bg="black", font=15).place(x=50, y=440)
logo_scale = Scale(root, from_=10, to_=50, orient=HORIZONTAL)
logo_scale.set(20)
logo_scale.place(x=200, y=440)

Button(root, text="Generate", width=20, height=2, bg="blue", fg="white", command=generate_qr_code).place(x=50, y=490)

logo_label = Label(root, bg="light blue")
logo_label.place(x=400, y=100)

qr_label = Label(root, bg="yellow")
qr_label.pack(padx=50, pady=10, side=RIGHT)

# Initial colors
qr_color = "black"
bg_color = "white"
logo_path = None

root.mainloop()
