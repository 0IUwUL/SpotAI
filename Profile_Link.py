from doctest import master
from tkinter import *
from dotenv import load_dotenv
import re

print("Profile")

def btn_clicked():
    global username
    username = re.findall(r"[\w']+", Uinput.get())
    try:
        username = username[5]
    except:
        #print(username)
        window.destroy()
        import Error
        exit(0)
    #print(username)
    window.destroy()
    import TY

window = Tk()

Uinput = StringVar()

window.geometry("1280x720")
window.configure(bg = "#191414")
canvas = Canvas(
    window,
    bg = "#191414",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(master = window, file = f"./assets/Profbackground.png")
background = canvas.create_image(
    639.0, 360.0,
    image=background_img,)

entry0_img = PhotoImage(master = window, file = f"./assets/Prof_textBox0.png")
entry0_bg = canvas.create_image(
    588.0, 541.5,
    image = entry0_img)

entry0 = Entry(
    master = window,
    bd = 0,
    bg = "#938888",
    highlightthickness = 0,
    textvariable = Uinput,)

entry0.place(
    x = 196.0, y = 519,
    width = 784.0,
    height = 43)

img1 = PhotoImage(master = window, file = f"./assets/Profimg1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",
    master = window,)

b1.place(
    x = 999, y = 519,
    width = 92,
    height = 45)

window.resizable(False, False)
window.mainloop()
