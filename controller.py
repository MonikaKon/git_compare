import subprocess
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class Controller:

    def check_changes():
        result = subprocess.run(["ls"], capture_output = True, text = True)
        print(result.stdout)
        return result.stdout

    def select_file():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askdirectory(
            title='Open a file',
            initialdir='/')

        showinfo(
            title='Selected File',
            message=filename
        )



Controller.check_changes()