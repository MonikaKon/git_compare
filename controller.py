import subprocess
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import view_edit_window

class Controller:

    def check_changes():
        result = subprocess.run(["ls"], capture_output = True, text = True)
        print(result.stdout)
        return result.stdout

    def change_entry1(chosen_path):
        view_edit_window.View_Edit_Window.entry1.delete(0,1000)
        view_edit_window.View_Edit_Window.entry1.insert(0, chosen_path)    

    def select_file():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askdirectory(
            title='Open a file',
            initialdir='/home/jakubkajzer/Desktop')

        showinfo(
            title='Selected File',
            message=filename
        )
        
        Controller.change_entry1(filename)

