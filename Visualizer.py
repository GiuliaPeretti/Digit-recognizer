import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np 
import pandas as pd

class Visualizer(ttk.Frame):
    data = pd.read_csv('mnist_train.csv')
    data = np.array(data)
    e=None
    
    
    
    def __init__(self, app):

        super().__init__(app)
        # self.title("Visualizer")
        # self.geometry("600x600")
        # self.resizable(False, False)
        # self.configure(background="pink")
        self.e = ttk.Entry(self)
        self.e.grid(row=4, column=30, rowspan=2, columnspan=5)
        b=ttk.Button(self, text='Visualize', command=self.visualize_number)
        b.grid(row=8, column=30, rowspan=2, columnspan=5)
        a=ttk.Button(self, text=">", command=self.avanti, width=3)
        a.grid(row=6, column=33, rowspan=2, columnspan=1)
        i=ttk.Button(self, text="<", command=self.indietro, width=3)
        i.grid(row=6, column=32, rowspan=2, columnspan=1)
        self.visualize_number()
        self.pack()



    def n_to_hex(self, n):
        n=hex(n)
        if(len(n)<3):
            s = '#'+(n[0]+n[2])*3
        else: 
            s = '#'+(n[2:])*3
        return s

    def visualize_number(self):
        number=-1
        print(self.e.get())
        if(self.e.get().isnumeric() and int(self.e.get())<60000 and int(self.e.get())>-1):
            number=int(self.e.get())
            print("entra")
        
        if (number==-1):
            self.e.delete(0,'end')
            for i in range (0,28):
                for j in range (0,28):
                    l = ttk.Label(self, text="", background="black", width=2)
                    l.grid(row=i+4,column=j)
        else:
            for i in range (0,len(self.data[number])):
                if (i==0):
                    risultato = ttk.Label(self, text="Nella riga "+str(number)+" c'é il numero "+str(self.data[number][0]))
                    risultato.grid(row=10,column=31, columnspan=10)
                else:
                    row=(i-1)//28+4
                    col=int((i-1)%28)
                    l = ttk.Label(self, text="", background=self.n_to_hex(self.data[number][i]), width=2)
                    l.grid(row=row,column=col)
        print(number)

    def avanti(self):
        if(self.e.get().isnumeric()):
            number=int(self.e.get())+1
            self.e.delete(0,'end')
            self.e.insert(0,number)
            self.visualize_number()

    def indietro(self):
        if(self.e.get().isnumeric()):
            number=int(self.e.get())-1
            self.e.delete(0,'end')
            self.e.insert(0,number)
            self.visualize_number()
