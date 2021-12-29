from tkinter import *


window = Tk()

def back():
    window.destroy()
    import Main

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

background_img = PhotoImage(file = f"./Question_Mark/assets/background.png")
background = canvas.create_image(
    715.0, 362.5,
    image=background_img)

img0 = PhotoImage(file = f"./Question_Mark/assets/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = back,
    relief = "flat")

b0.place(
    x = 45, y = 37,
    width = 65,
    height = 68)

window.resizable(False, False)
window.mainloop()
