import os
import tkinter as tk
from tkinter import ttk

def clear():
    if os.name == 'posix':  # For Linux and MacOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')


class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        # Set default options
        options = {
            'bg': '#4CAF50',
            'fg': 'white',
            'font': ('Times New Roman', 12),
            'padx': 10,
            'pady': 5,
            'bd': 0,
            'width':20,
            'heigh':1
        }
        options.update(kwargs)  # Update with any user-defined options
        super().__init__(master, **options)
