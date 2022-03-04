from fileinput import filename
import tkinter as tk
from tkinter import Label, StringVar, ttk
from tkinter import filedialog as fd
#from tkinter.messagebox import showinfo
from controller import Controller

class View():
    root = tk.Tk()
    entry1 = tk.Entry(root)
    def __init__(self):
        # create the root window
        
        View.root.title('Tkinter Open File Dialog')
        View.root.resizable(False, False)
        View.root.geometry('300x150')


        # open button
        open_button = ttk.Button(
            View.root,
            text='Open a File',
            command= Controller.select_file
        )
        chosen_file = StringVar()
        chosen_file = "Please, open file"
        
        View.entry1.insert(0, chosen_file)

        open_button.pack(expand=True)
        View.entry1.pack()

        # run the application
        View.root.mainloop()

    def change_entry1( chosen_path):
        View.entry1.insert(0, chosen_path)