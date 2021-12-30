from tkinter import *
from tkinter import messagebox

att = {}

def btn_En():
    att['Energy'] = int(Checkbutton0.get())
def btn_Dnc():
    att['Danceability'] = int(Checkbutton1.get())
def btn_Val():
    att['Valence'] = int(Checkbutton2.get())
def btn_Key():
    att['Key'] = int(Checkbutton3.get())
#def btn_Ldn():
#    att['Loudness'] = int(Checkbutton4.get())
def btn_Ac():
    att['Acousticness'] = int(Checkbutton5.get())
def btn_clicked():
    total = 0
    for name in att:
        total += att[name] 

    if(total > 3 or total < 3):
        messagebox.showerror(title="Error", message="Please choose 3 attributes")
    else:
        window.destroy()
        import Spot_Clustering_Model
    
window = Tk()

Checkbutton0 = IntVar()  
Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()  
#Checkbutton4 = IntVar()  
Checkbutton5 = IntVar()
    
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
img0a = PhotoImage(file = f"./Start/assets/img0a.png")
b0 = Checkbutton(
        variable = Checkbutton0,
        onvalue = 1,
        offvalue = 0,
        command = lambda: btn_En(),
        image = img0, 
        indicatoron=False,
        selectimage=img0a,
    )
    
b0.place(
    x = 829, y = 182,
    width = 334,
    height = 110)

img1 = PhotoImage(file = f"./Start/assets/img1.png")
img1a = PhotoImage(file = f"./Start/assets/img1a.png")
b1 = Checkbutton(
        variable = Checkbutton1,
        onvalue = 1,
        offvalue = 0,
        command = lambda : btn_Dnc(),
        image = img1, 
        indicatoron=False,
        selectimage=img1a,
    )

b1.place(
    x = 829, y = 432,
    width = 334,
    height = 110)

img3 = PhotoImage(file = f"./Start/assets/img3.png")
img3a = PhotoImage(file = f"./Start/assets/img3a.png")
b3 = Checkbutton(
        variable = Checkbutton2,
        onvalue = 1,
        offvalue = 0,
        command = lambda : btn_Val(),
        image = img3, 
        indicatoron=False,
        selectimage=img3a,
    )

b3.place(
    x = 113, y = 432,
    width = 334,
    height = 110)

img4 = PhotoImage(file = f"./Start/assets/img4.png")
img4a = PhotoImage(file = f"./Start/assets/img4a.png")
b4 = Checkbutton(
        variable = Checkbutton3,
        onvalue = 1,
        offvalue = 0,
        command = lambda : btn_Key(),
        image = img4, 
        indicatoron=False,
        selectimage=img4a,
    )

b4.place(
    x = 113, y = 307,
    width = 334,
    height = 110)

#img5 = PhotoImage(file = f"./Start/assets/img5.png")
#img5a = PhotoImage(file = f"./Start/assets/img5a.png")
#b5 = Checkbutton(
#        variable = Checkbutton4,
#        onvalue = 1,
#        offvalue = 0,
#        command = lambda : btn_Ldn(),
#        image = img5, 
#        indicatoron=False,
#        selectimage=img5a,
#    )

#b5.place(
#    x = 829, y = 307,
#    width = 334,
#    height = 110)

img6 = PhotoImage(file = f"./Start/assets/img6.png")
img6a = PhotoImage(file = f"./Start/assets/img6a.png")
b6 = Checkbutton(
        variable = Checkbutton5,
        onvalue = 1,
        offvalue = 0,
        command = lambda : btn_Ac(),
        image = img6, 
        indicatoron=False,
        selectimage=img6a,
    )

b6.place(
    x = 113, y = 182,
    width = 334,
    height = 110)

#submit button
img2 = PhotoImage(file = f"./Start/assets/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : btn_clicked(),
    relief = "flat")

b2.place(
    x = 473, y = 557,
    width = 334,
    height = 110)


window.resizable(False, False)
window.mainloop()

