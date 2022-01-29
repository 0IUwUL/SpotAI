from tkinter import *

def run():
    window.destroy()
    import Profile_Link


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

background_img = PhotoImage(file = f"./assets/Wait_background.png")
background = canvas.create_image(
    640.0, 361.5,
    image=background_img)

window.resizable(False, False)

window.after(1000, lambda : run())

window.mainloop()