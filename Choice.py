from tkinter import *
from tkinter import messagebox

chose = {}

def btn_clicked():
    print("Choice")
    num = 0
    for a in chose:
        num += chose[a]
    if num != 1:
        messagebox.showerror(title="Error", message="Please choose 1")
    else:
        window.destroy()
        try:
            if chose['Att'] == 1:
                import Land
        except:
            import Playlist

def Playlist():
    chose['Playlist'] = int(Checkbutton1.get())

def Att():
    chose['Att'] = int(Checkbutton0.get())


window = Tk()

Checkbutton0 = IntVar()  
Checkbutton1 = IntVar() 

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

background_img = PhotoImage(file = f"./assets/Choice_background.png")
background = canvas.create_image(
    640.0, 361.5,
    image=background_img)

img0 = PhotoImage(file = f"./assets/Choice_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(),
    relief = "flat")

b0.place(
    x = 471, y = 555,
    width = 334,
    height = 110)

img1 = PhotoImage(file = f"./assets/Choice_img1.png")
img1a = PhotoImage(file = f"./assets/Choice_img1a.png")
b1 = Checkbutton(
    variable = Checkbutton0,
    onvalue = 1,
    offvalue = 0,
    command = lambda : Att(),
    image = img1, 
    indicatoron=False,
    selectimage=img1a,
)

b1.place(
    x = 106, y = 177,
    width = 365,
    height = 365)

img2 = PhotoImage(file = f"./assets/Choice_img2.png")
img2a = PhotoImage(file = f"./assets/Choice_img2a.png")
b2 = Checkbutton(
    variable = Checkbutton1,
    onvalue = 1,
    offvalue = 0,
    command = lambda : Playlist(),
    image = img2, 
    indicatoron=False,
    selectimage=img2a,
)

b2.place(
    x = 805, y = 177,
    width = 365,
    height = 365)

window.resizable(False, False)
window.mainloop()
