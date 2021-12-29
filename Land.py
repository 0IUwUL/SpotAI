from tkinter import *

att = {}

def btn_clicked(name):
    if name in att and name != 'Submit':
        att[name] += 1
    else:
        att[name] = 0
        print(att)
    #btn.button = Button(command=btn.color_change,bg="blue")

    

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

background_img = PhotoImage(file = f"./Start/assets/background.png")
background = canvas.create_image(
    640.0, 361.5,
    image=background_img)

img0 = PhotoImage(file = f"./Start/assets/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Energy'),
    relief = "flat")
    

b0.place(
    x = 829, y = 182,
    width = 334,
    height = 110)

img1 = PhotoImage(file = f"./Start/assets/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Danceability'),
    relief = "flat")


b1.place(
    x = 829, y = 432,
    width = 334,
    height = 110)

img2 = PhotoImage(file = f"./Start/assets/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Submit'),
    relief = "flat")

b2.place(
    x = 473, y = 557,
    width = 334,
    height = 110)

img3 = PhotoImage(file = f"./Start/assets/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Valence'),
    relief = "flat")

b3.place(
    x = 113, y = 432,
    width = 334,
    height = 110)

img4 = PhotoImage(file = f"./Start/assets/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Key'),
    relief = "flat")

b4.place(
    x = 113, y = 307,
    width = 334,
    height = 110)

img5 = PhotoImage(file = f"./Start/assets/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Loudness'),
    relief = "flat")

b5.place(
    x = 829, y = 307,
    width = 334,
    height = 110)

img6 = PhotoImage(file = f"./Start/assets/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked('Acousticness'),
    relief = "flat")

b6.place(
    x = 113, y = 182,
    width = 334,
    height = 110)

window.resizable(False, False)
window.mainloop()

