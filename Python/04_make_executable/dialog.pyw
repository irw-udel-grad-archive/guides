import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# File picker
file_path = filedialog.askopenfilename()

# Folder picker
dir_path = filedialog.askdirectory()