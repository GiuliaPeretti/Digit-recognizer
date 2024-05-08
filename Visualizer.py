import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np 
import pandas as pd

class Visualizer(tk.Frame):
    e = None

    def __init__(self,app):
        data = pd.read_csv('mnist_train.csv')
        data = np.array(data)

        super().__init__(app)
        self.title("Visualizer")
        self.geometry("600x600")
        self.resizable(False, False)
        self.configure(background="pink")


        e = self.Entry(self)
        e.grid(row=0, column=30, rowspan=2, columnspan=5)
        b=self.Button(self, text='Visualize', command=self.visualize_number)
        b.grid(row=4, column=30, rowspan=2, columnspan=5)
        a=self.Button(self, text=">", command=self.avanti, width=3)
        a.grid(row=2, column=33, rowspan=2, columnspan=1)
        i=self.Button(self, text="<", command=self.indietro, width=3)
        i.grid(row=2, column=32, rowspan=2, columnspan=1)
        self.visualize_number(self)


    def n_to_hex(n):
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
            for i in range (0,28):
                for j in range (0,28):
                    l = self.Label(self, text="", background="black", width=2)
                    l.grid(row=i,column=j)
        else:
            for i in range (0,len(self.data[number])):
                if (i==0):
                    risultato = self.Label(self, text="Nella riga "+str(number)+" c'é il numero "+str(self.data[number][0]))
                    risultato.grid(row=6,column=30, columnspan=10)
                else:
                    j=(i-1)//28
                    k=int((i-1)%28)
                    l = self.Label(self, text="", background=self.n_to_hex(self.data[number][i]), width=2)
                    l.grid(row=j,column=k)
        print(number)

    def avanti():
        if(e.get().isnumeric()):
            number=int(e.get())+1
            e.delete(0,END)
            e.insert(0,number)
            visualize_number(number)

    def indietro():
        if(e.get().isnumeric()):
            number=int(e.get())-1
            e.delete(0,END)
            e.insert(0,number)
            visualize_number(number)
