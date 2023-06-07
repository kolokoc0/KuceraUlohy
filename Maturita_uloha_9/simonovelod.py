import tkinter as tk, random
from tkinter import Canvas
root=tk.Tk()
canvas: Canvas = tk.Canvas(width=700, height=650)
canvas.pack()

a=20
b=30
safety=0

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def start():
    global a,b,safety
    c=0
    y="0"
    b = 30
    for i in range(15):
        globals()["var_" + str(i)] = a
        while c<650:
            safety+=1
            if safety==1000:
                print("Safety overheated.")
                exit
            for a in range(15):
                canvas.create_line(650, 0, 650, 650, fill="red")
                globals()["var_" + str(i)] += random.randint(1,10)
                c = globals()["var_" + str(i)]
                print(c,b)
                lodicka(c, b)
                b +=35
            if c==650 or c>650:
                y=str(i)
                canvas.create_text(350, 325, fill="darkblue", font="Times 15",text=y+"won.")
                exit
    canvas.after(10,start)


def create():
    b = 30
    for i in range(15):
        lodicka(a,b)
        b+=35
    canvas.create_line(650,0,650,650,fill="red")
create()

canvas.bind("<Button-1>",start())

root.mainloop()