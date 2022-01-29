from tkinter import *
import re
print("Playlist")
def btn_clicked():
    try:
        global link
        link = re.findall(r"[\w']+", str(Uinput.get()))
        link = link[5]
        window.destroy()
        import Profile_Link
    except:
        window.destroy()
        import Error
        exit(0)

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

background_img = PhotoImage(file = f"./assets/Playlist_background.png")
background = canvas.create_image(
    639.0, 360.0,
    image=background_img)

entry0_img = PhotoImage(file = f"./assets/Playlist_img_textBox0.png")
entry0_bg = canvas.create_image(
    588.0, 541.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#938888",
    highlightthickness = 0,
    textvariable = Uinput)

entry0.place(
    x = 196.0, y = 519,
    width = 784.0,
    height = 43)

img0 = PhotoImage(file = f"./assets/Playlist_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 999, y = 519,
    width = 92,
    height = 45)

window.resizable(False, False)
window.mainloop()
