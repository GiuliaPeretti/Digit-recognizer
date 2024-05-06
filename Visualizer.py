from tkinter import *
from tkinter.ttk import *
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt


def n_to_hex(n):
    n=hex(n)
    if(len(n)<3):
        s = '#'+(n[0]+n[2])*3
    else: 
        s = '#'+(n[2:])*3
    return s

def visualize_number(number=-1):
    print(e.get())
    if(e.get().isnumeric() and int(e.get())<60000 and int(e.get())>-1):
        number=int(e.get())
        print("entra")
    
    if (number==-1):
        for i in range (0,28):
            for j in range (0,28):
                l = Label(v, text="", background="black", width=2)
                l.grid(row=i,column=j)
    else:
        for i in range (0,len(data[number])):
            if (i==0):
                risultato = Label(v, text="Nella riga "+str(number)+" c'é il numero "+str(data[number][0]))
                risultato.grid(row=6,column=30, columnspan=10)
            else:
                j=(i-1)//28
                k=int((i-1)%28)
                l = Label(v, text="", background=n_to_hex(data[number][i]), width=2)
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
    

data = pd.read_csv('mnist_train.csv')
data = np.array(data)

v=Tk()
v.title("Visualizer")
v.geometry("600x600")
v.resizable(False, False)
v.configure(background="pink")


e= Entry(v)
e.grid(row=0, column=30, rowspan=2, columnspan=5)
b=Button(v, text='Visualize', command=visualize_number)
b.grid(row=4, column=30, rowspan=2, columnspan=5)
a=Button(v, text=">", command=avanti, width=3)
a.grid(row=2, column=33, rowspan=2, columnspan=1)
i=Button(v, text="<", command=indietro, width=3)
i.grid(row=2, column=32, rowspan=2, columnspan=1)
visualize_number()




v.mainloop()