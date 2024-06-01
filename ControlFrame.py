import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from Visualizer import *
from Tester import *

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):
        print("init control frame")

        super().__init__(container)
        self['text'] = 'Options'

        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='Visualizer',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Tester',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=0, padx=5, pady=5, sticky='ew', columnspan=30, rowspan=1)
        print("menu visualizzato")
        # initialize frames
        self.frames = {}
        self.frames[0] = Visualizer(container)
        self.frames[1] = Tester(container)

        self.change_frame()

    def change_frame(self):
        print("frame cambiato")
        frame = self.frames[self.selected_value.get()]
        if(self.selected_value.get()==0):
            self.frames[1].forget()
            self.frames[0].tkraise()
            self.frames[0].grid(row=1, column=0)
        else:
            self.frames[0].forget()
            self.frames[1].tkraise()
            self.frames[1].pack(row=1, column=0)

