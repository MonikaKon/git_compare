import tkinter as tk
from tkinter import Label, ttk
from tkinter import filedialog as fd
#from tkinter.messagebox import showinfo
import controller

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=controller.Controller.select_file
)

open_button.pack(expand=True)

# run the application
root.mainloop()
