from tkinter import *


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#1db954")
canvas = Canvas(
    window,
    bg = "#1db954",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./assets/TY.png")
background = canvas.create_image(
    641.0, 435.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()
