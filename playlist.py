from tkinter import *
#from Spot_Clustering_Model import finale
#from Spot_Clustering_Model import pas
#import pandas as pd 

#print(finale)
#display = []
#count = 0

#for items in finale:
#    display.append(items.sort_values(pas[count], ascending = False))
#    count+=1

#print(display)

def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file = f"./Playlist/assets/background.png")
background = canvas.create_image(
    640.0, 350.5,
    image=background_img)

img0 = PhotoImage(file = f"./Playlist/assets/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = -14, y = 0,
    width = 87,
    height = 87)

window.resizable(False, False)
window.mainloop()
