import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np 
import time
import pandas as pd

class Visualizer(ttk.Frame):
    data = pd.read_csv('blackAndWhite.csv')
    data = np.array(data)
    
    
    
    
    def __init__(self, app):

        super().__init__(app)
        # self.title("Visualizer")
        # self.geometry("600x600")
        # self.resizable(False, False)
        # self.configure(background="pink")
        # ttk.Label(self,background="pink", width=100).grid(row=0, column=30, rowspan=2, columnspan=2)
        self.pixel=[[ttk.Label]*28]*28
        self.entry = ttk.Entry(self)
        self.entry.grid(row=4, column=30, rowspan=2, columnspan=5)
        self.Visualize=ttk.Button(self, text='Visualize', command=self.visualize_number)
        self.Visualize.grid(row=8, column=30, rowspan=2, columnspan=5)
        self.avanti=ttk.Button(self, text=">", command=self.vai_avanti, width=3)
        self.avanti.grid(row=6, column=33, rowspan=2, columnspan=1)
        self.indietro=ttk.Button(self, text="<", command=self.vai_indietro, width=3)
        self.indietro.grid(row=6, column=32, rowspan=2, columnspan=1)
        self.visualize_number()
        self.grid(row=1, column=0)



    def n_to_hex(self, n):
        n=hex(n)
        if(len(n)<3):
            s = '#'+(n[0]+n[2])*3
        else: 
            s = '#'+(n[2:])*3
        return s

    def visualize_number(self):
        number=-1
        print(self.entry.get())
        if(self.entry.get().isnumeric() and int(self.entry.get())<60000 and int(self.entry.get())>-1):
            number=int(self.entry.get())
            print("entra")
        
        if (number==-1):
            self.entry.delete(0,'end')
            for i in range (0,28):
                for j in range (0,28):
                    self.pixel[i][j] = ttk.Label(self, text="", background="black", width=2)
                    self.pixel[i][j].grid(row=i,column=j)
        else:
            for i in range (0,len(self.data[number])):
                if (i==0):
                    self.risultato = ttk.Label(self, text="Nella riga "+str(number)+" c'é il numero "+str(self.data[number][0]))
                    self.risultato.grid(row=10,column=31, columnspan=10)
                else:
                    row=(i-1)//28
                    col=int((i-1)%28)
                    self.pixel[row][col] = ttk.Label(self, text="", background=self.n_to_hex(self.data[number][i]), width=2)
                    self.pixel[row][col].grid(row=row,column=col)
        print(number)


    def vai_avanti(self):
        if(self.entry.get().isnumeric()):
            number=int(self.entry.get())+1
            self.entry.delete(0,'end')
            self.entry.insert(0,number)
            self.visualize_number()
        #self.reset()

    def vai_indietro(self):
        if(self.entry.get().isnumeric()):
            number=int(self.entry.get())-1
            self.entry.delete(0,'end')
            self.entry.insert(0,number)
            self.visualize_number()

    def reset(self):
        # self.entry.grid_remove()
        # self.Visualize.grid_remove()
        # self.avanti.grid_remove()
        # self.indietro.grid_remove()
        # self.risultato.grid_remove()
        # for i in range(0,28):
        #     for j in range(0,28):
        #         self.pixel[i][j].grid_remove()
        self.grid_forget()