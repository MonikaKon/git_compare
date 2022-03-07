from fileinput import filename
import tkinter as tk
from tkinter import Button, Label, StringVar, ttk
from tkinter import filedialog as fd
from functools import partial
#from tkinter.messagebox import showinfo

#from controller import Controller

from view_edit_window import View_Edit_Window

class View():
    root = tk.Tk()


    def __init__(self):
        # create the root window
        
        View.root.title('Git compare')
        View.root.resizable(False, False)
        View.root.geometry('350x150')

        edit_button = Button(View.root, text = "Edit", command= partial(View_Edit_Window, View.root))

        edit_button.grid(row = 0, column = 0)

        # run the application
        View.root.mainloop()

