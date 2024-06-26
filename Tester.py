import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np 
import pandas as pd
from ReteNeurale import *

class Tester(ttk.Frame):

    prevPoint=[0,0]
    pixel=[0]*784
    

    def __init__(self,parent):
        super().__init__(parent)
        self.c=tk.Canvas(self, bg="black", height=420, width=420)
        for i in range (0,28):
            self.c.create_line(0, i*15, 420, i*15, fill="gray")
            self.c.create_line(i*15, 0, i*15, 420, fill="gray")
        self.c.bind('<B1-Motion>', self.draw_on_canvas)
        #TODO: aggiungere anche se il pulsante viene solo premuto
        #TODO: aggiungere cancellare
        self.c.bind('<ButtonRelease-1>', self.draw_on_canvas)
        self.c.grid(row=0, column=0, rowspan=100, columnspan=100)
        test=ttk.Button(self, text="Test", command=self.invia)
        test.grid(row=3, column=100)
        self.result=ttk.Label(self, text="")
        self.result.grid(row=5, column=100)
        self.grid(row=1, column=0)
    
    def invia(self):
        global pixel
        res=guess(self.pixel)
        self.result.config(text="Il risultato e: "+str(res))


    def draw_on_canvas(self,event): 
        print(event.type)
        x=event.x
        y=event.y
        currentPoint = [x,y]
        square = [x//15, y//15]
        print(x, y)
        print(x//15, y//15)

        if self.prevPoint != [0,0]: 
            pos=square[1]*28+square[0]%28
            self.pixel[pos]=1
            self.c.create_rectangle( square[0]*15, square[1]*15, (square[0]+2)*15, (square[1]+2)*15, fill="white", outline="white")
        self.prevPoint=currentPoint
        if(event.type=="5"):
            self.prevPoint=[0,0]
        for i in range (0,28):
            for j in range (0,28):
                print(self.pixel[i*28+j], end="")
            print()

    def reset(self):
        self.grid_forget()


            