from fileinput import filename
import tkinter as tk
from tkinter import NSEW, VERTICAL, Button, Canvas, Frame, Label, Scrollbar, StringVar, ttk
from tkinter import filedialog as fd
from functools import partial
#from tkinter.messagebox import showinfo

#from controller import Controller

from view_edit_window import View_Edit_Window

class View():
    root = tk.Tk()
    my_array = ["example "+str(x) for x in range(1, 11)]

    def __init__(self):
        # create the root window
        
        View.root.title('Git compare')
        View.root.resizable(False, False)
        View.root.geometry('350x150')

        edit_button = Button(View.root, text = "Edit", 
                    command= partial(View_Edit_Window, View.root))

        my_frame = tk.Frame(View.root, bg = "light blue")
        #my_canva = Canvas(my_frame, bg = "yellow")
        #my_scroll = Scrollbar(View.root, orient = VERTICAL, command=my_frame.yview)

        for example in View.my_array:
            my_label = Label(my_frame, text=example)
            my_label.grid()

        edit_button.grid(row = 0, column = 0)
        my_frame.grid(row = 1, column = 0)
        #my_canva.grid(row = 1, column = 0)
        #my_scroll.grid(row = 1, column=3)

        # run the application
        View.root.mainloop()

