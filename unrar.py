import tkinter
from tkinter import filedialog
import os
import patoolib


class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.title('Unrar')

        self.main_window.resizable(False, False)

        self.main_window.geometry('200x100')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label = tkinter.Label(self.top_frame, text='Unrar')
        self.label.pack(side='left', pady=10)

        self.button = tkinter.Button(
            self.bottom_frame, text='Select File', command=self.open_file)
        self.button.pack(side='left', pady=10)

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def open_file(self):

        file_path = filedialog.askopenfilename(initialdir=os.getcwd(
        ), title='Select File', filetypes=(('RAR Files', '*.rar'), ('All Files', '*.*')))

        if file_path:

            out_path = patoolib.extract_archive(
                file_path, outdir=file_path[:-4], verbosity=-1, interactive=False)

            tkinter.messagebox.showinfo(
                'Extracted Files', 'Files extracted to: ' + out_path)


my_gui = MyGUI()
