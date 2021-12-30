from tkinter import *
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        self.geometry("1280x720")
        self.configure(bg = "#191414")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
        
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        canvas = Canvas(
            self,
            bg = "#191414",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        canvas.pack()

        background_img = PhotoImage(file = f"./Desktop/assets/Mbackground.png")
        background = canvas.create_image(
            641.0, 413.0,
            image=background_img)

        img0 = PhotoImage(file = f"./Desktop/assets/start.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            #command = Start_btn,
            relief = "flat")

        b0.place(
            x = 480, y = 544,
            width = 377,
            height = 97)

        img1 = PhotoImage(file = f"./Desktop/assets/Question.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            #command = Question_btn,
            relief = "flat")

        b1.place(
            x = 1180, y = 19,
            width = 87,
            height = 87)

        b0.pack()
        b1.pack()
        #label = tk.Label(self, text="This is the start page", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)

        #button1 = tk.Button(self, text="Go to Page One",
        #                    command=lambda: controller.show_frame("PageOne"))
        #button2 = tk.Button(self, text="Go to Page Two",
        #                    command=lambda: controller.show_frame("PageTwo"))
        #button1.pack()
        #button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()