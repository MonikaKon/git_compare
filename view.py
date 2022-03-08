from fileinput import filename
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from functools import partial
#from tkinter.messagebox import showinfo

#from controller import Controller

from view_edit_window import View_Edit_Window

class View():
    root = tk.Tk()
    my_array = ["example "+str(x) for x in range(1, 40)]

    def __init__(self):
        # create the root window
        
        View.root.title('Git compare')
        View.root.resizable(False, False)
        View.root.geometry('350x150')
        View.root.columnconfigure(0, weight=1)
        View.root.rowconfigure(1, weight=1)

        button_frame = tk.Frame(View.root, bg = "deep pink", bd = 1)
        edit_button = Button(button_frame, text = "Edit", 
                    command= partial(View_Edit_Window, View.root))
        main_frame = tk.Frame(View.root, bg = "green", bd = 1)

        button_frame.grid(row = 0, column = 0, sticky = N + W)
        edit_button.grid(row = 0, column = 0, sticky =W+N)
        main_frame.grid(row = 1, column = 0, sticky=N+E+W+S)

        list_canvas = Canvas(main_frame, bg = "yellow")
        list_scroll = Scrollbar(main_frame, orient = VERTICAL, command=list_canvas.yview)
        list_canvas.config(yscrollcommand=list_scroll.set)


        for example in View.my_array:
            my_label = Label(list_canvas, text=example)
            my_label.pack()

        list_scroll.pack(side=RIGHT,fill=Y)
        list_canvas.pack(side=LEFT,expand=True,fill=BOTH)

        # run the application
        View.root.mainloop()

