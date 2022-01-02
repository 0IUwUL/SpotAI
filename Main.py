from tkinter import *

window = Tk()

def Start_btn():
    window.destroy()
    import Land

def Question_btn():
    window.destroy()
    import Info

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

background_img = PhotoImage(file = f"./assets/Deskbackground.png")
background = canvas.create_image(
    641.0, 413.0,
    image=background_img)

img0 = PhotoImage(file = f"./assets/Deskstart.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Start_btn,
    relief = "flat")

b0.place(
    x = 480, y = 544,
    width = 377,
    height = 97)

img1 = PhotoImage(file = f"./assets/DeskQuestion.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = Question_btn,
    relief = "flat")

b1.place(
    x = 1180, y = 19,
    width = 87,
    height = 87)

window.resizable(False, False)
window.mainloop()
