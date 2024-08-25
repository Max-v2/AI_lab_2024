# scripts/gui.py
import tkinter as tk
from tkinter import filedialog

def load_file():
    file_path = filedialog.askopenfilename()
    print(f"File loaded: {file_path}")

root = tk.Tk()
root.title("AI Interface")

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack()

root.mainloop()