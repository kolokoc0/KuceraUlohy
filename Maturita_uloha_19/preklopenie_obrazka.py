import tkinter as tk

def preklopenie():
    global size
    for r in range(int(size[1])):
        line = file[r].strip('\n').split(' ')
        for column in range(len(line)):
            if int(line[column]) ==0:
                color = 'white'
            else:
                color= 'black'
            canvas.create_rectangle(int(size[0])*strana-strana*column,r*strana,int(size[0])*strana-strana*(column+1),(r+1)*strana,fill=color)




with open('preklopenie_obrazka.txt','r') as file:
    file = file.readlines()


size = file[0].strip('\n').split(' ')
print(size)
file = file[1::]

strana = 4
color = 'white'
win = tk.Tk()
canvas = tk.Canvas(win,width=int(size[0])*strana,height=int(size[1])*strana)
canvas.pack()

for r in range(int(size[1])):
    line = file[r].strip('\n').split(' ')
    for column in range(len(line)):
        if int(line[column]) ==0:
            color = 'white'
        else:
            color= 'black'
        canvas.create_rectangle(column*strana,r*strana,(column+1)*strana,(r+1)*strana,fill=color)





button= tk.Button(win,text='clik me',command=preklopenie)
button.pack()


win.mainloop()