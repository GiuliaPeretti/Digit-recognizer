import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Visualizer import *
from Tester import *
from ControlFrame import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Digit recognizer')
        self.geometry('600x600')

if __name__ == "__main__":
    app = App()
    frame = Visualizer(app)
    app.mainloop()