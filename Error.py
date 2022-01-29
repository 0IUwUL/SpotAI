from tkinter import *

window = Tk()

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

background_img = PhotoImage(master = window, file = f"./assets/Errorbackground.png")
background = canvas.create_image(
    639.0, 401.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()
