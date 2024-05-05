from tkinter import *
from tkinter.ttk import *
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt

# def reset():
#     pixel=[[0]*28]*28
    
def draw_on_canvas(event):
    x=event.x
    y=event.y
    c.create_oval((x-brush_size/2, y-brush_size/2, x+brush_size/2, y+brush_size/2), outline="white",fill="white")

gui=Tk()
gui.title("Visualizer")
gui.geometry("600x600")
gui.resizable(True, True)
gui.configure(background="pink")

# pixel=[]
# row,col=28,28
# for i in range (0,row):
#     p=[]
#     for j in range (0,col):
#         b = Button(gui, text=str(i)+"x"+str(j), width=5)
#         b.grid(row=i,column=j)
#         p.append(b)
#     pixel.append(p)
brush_size=4
c=Canvas(gui, bg="black")
c.bind('<B1-Motion>', draw_on_canvas)
c.pack()
#c.grid(row=0, column=0, rowspan=100, columnspan=100)
        
gui.mainloop()