from tkinter import *
from tkinter.ttk import *
import numpy as np 
import pandas as pd 

# def reset():
#     pixel=[[0]*28]*28
    
def draw_on_canvas(event):
    print(event.type)
    global prevPoint
    global currentPoint
    global pixel
    x=event.x
    y=event.y
    currentPoint = [x,y]
    #currentPoint = [x//28, y//28]
    square =  [x//15, y//15 ]
    print(x, y)
    print(x//15, y//15)

    if prevPoint != [0,0]: 
        #TODO: sistemare cooridnate matrice
        pos=(y//15)*28+(x//15)%28
        pixel[pos]=1
        c.create_rectangle( square[0]*15, square[1]*15, (square[0]+1)*15, (square[1]+1)*15, fill="white", outline="white")
        #c.create_line(prevPoint[0], prevPoint[1],currentPoint[0],currentPoint[1], activewidth=100, fill="white")
        #c.create_oval((x-brush_size/2, y-brush_size/2, x+brush_size/2, y+brush_size/2), outline="white",fill="white")
    prevPoint=currentPoint
    if(event.type=="5"):
        prevPoint=[0,0]
    for i in range (0,28):
        for j in range (0,28):
            print(pixel[i*28+j], end="")
        print()

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
prevPoint=[0,0]
currentPoint=[0,0]
pixel=[0]*784
#sistemare la dimensione
c=Canvas(gui, bg="black", height=420, width=420)
#TODO: aggiungi griglia per vedere pixel
for i in range (0,28):
    c.create_line(0, i*15, 420, i*15, fill="gray")
    c.create_line(i*15, 0, i*15, 420, fill="gray")
c.bind('<B1-Motion>', draw_on_canvas)
#TODO: aggiungere anche se il pulsante viene solo premuto
#TODO: aggiungere cancellare
c.bind('<ButtonRelease-1>', draw_on_canvas)
c.grid(row=0, column=0, rowspan=100, columnspan=100)
#c.grid(row=0, column=0, rowspan=100, columnspan=100)
answer=Entry(gui)
answer.grid(row=0, column=100)
        
gui.mainloop()