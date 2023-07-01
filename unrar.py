import tkinter
from tkinter import filedialog
import os
import patoolib


class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        # Set the title of the window
        self.main_window.title('Unrar')
        # Disable resizing of the window
        self.main_window.resizable(False, False)
        # Set the size of the window
        self.main_window.geometry('200x100')

        # Create the top and bottom frames for organizing widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a label widget and pack it into the top frame
        self.label = tkinter.Label(self.top_frame, text='Unrar')
        self.label.pack(side='left', pady=10)

        # Create a button widget for file selection and pack it into the bottom frame
        self.button = tkinter.Button(
            self.bottom_frame, text='Select File', command=self.open_file)
        self.button.pack(side='left', pady=10)

        # Pack the frames into the main window
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the tkinter event loop
        tkinter.mainloop()

    def open_file(self):
        # Open a file dialog for selecting a file
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(
        ), title='Select File', filetypes=(('RAR Files', '*.rar'), ('All Files', '*.*')))

        if file_path:
            # Extract the archive to the same directory as the selected file
            out_path = patoolib.extract_archive(
                file_path, outdir=file_path[:-4], verbosity=-1, interactive=False)

            # Display a message box with the path where the files were extracted
            tkinter.messagebox.showinfo(
                'Extracted Files', 'Files extracted to: ' + out_path)


# Create an instance of the MyGUI class
my_gui = MyGUI()
