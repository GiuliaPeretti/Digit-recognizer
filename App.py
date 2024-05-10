import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Visualizer import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My App')
        self.geometry('600x600')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        vis = Visualizer()
        vis.mainloop()

if __name__ == "__main__":
  app = App()
  app.mainloop()