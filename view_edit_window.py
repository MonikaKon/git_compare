import tkinter as tk
from tkinter import Label, StringVar, ttk
from tkinter import filedialog as fds

import controller


class View_Edit_Window():

    edit_window = tk.Toplevel
    entry1 = tk.Entry

    def __init__(self, root):
        View_Edit_Window.edit_window=tk.Toplevel(root)
        View_Edit_Window.edit_window.title('Git compare settings')
        View_Edit_Window.edit_window.resizable(False, False)
        View_Edit_Window.edit_window.geometry('300x150')

        # open button
        open_button = tk.Button(
            View_Edit_Window.edit_window,
            text='Open a File',
            command= controller.Controller.select_file
        )

        chosen_file = StringVar()
        chosen_file = "Please, open file"
        open_button.grid(row = 0, column = 0)
        
        View_Edit_Window.entry1=tk.Entry(View_Edit_Window.edit_window)       
        View_Edit_Window.entry1.grid(row = 0, column = 1)

        View_Edit_Window.entry1.insert(0, chosen_file)    



