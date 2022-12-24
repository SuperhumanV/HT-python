from tkinter import *
from tkinter import messagebox
import time
import random


tk = Tk()
app_running = True
#закрытие окна на крестик
def on_closing():
    global app_running
    if messagebox.askokcancel('Quit','Do you want to quit?'):
        app_running = False
        tk.destroy()
size_canvas_x = 768
size_canvas_y = 768
tk.protocol('LM_DELETE_WINDOW', on_closing)

tk.title('Cross and Circles')
tk.resizable(0,0)
canvas = Canvas(tk,width=size_canvas_x,height=size_canvas_y,bd=0,highlightthickness=0)
canvas.create_rectangle(0,0,size_canvas_x,size_canvas_y,fill = 'white')
canvas.pack()
tk.update()

#кол-во ячеек
s_x = 3
s_y = 3

#отступы
step_x = size_canvas_x//s_x
step_y = size_canvas_y//s_y
#Намечаем таблицу по горизонтали
def draw_table():
    for i in range(0,s_x+1):
        #начертится линия из левого верхнего угла в левый правый угол
        canvas.create_line(0,i*step_y,size_canvas_x,i*step_y)
    for i in range(0,s_y+1):
            canvas.create_line(i*step_y,0,i*step_y,size_canvas_y)


draw_table()
points = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
list_ids = []


class Point:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
    def __str__(self):
        return str(self.__class__) + ':' + str(self.__dict__)

def draw_point(x,y,type):
    size = 15
    color = 'black'
    if type == 0:
     color = 'magenta'
     id = canvas.create_oval(x*step_x+size,y*step_y+size,x*step_x+step_x-size,y*step_y+step_y-size,fill = color)
     id2 = canvas.create_oval(x*step_x+size+size,y*step_y+size+size,x*step_x+step_x-size-size,y*step_y+step_y-size-size,fill = 'white')
     list_ids.append(id)
     list_ids.append(id2)

    if type == 1:
        color = 'cyan'
        id1 = canvas.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x, y * step_y + step_y //2,fill = 'black')
        id2 = canvas.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2, y * step_y + step_y, fill = 'black')
        list_ids.append(id1)
        list_ids.append(id2)


def add_to_points(event):
    #print(event.num,event.x,event.y)
    type = 0
    if event.num == 3:
      type = 1
    if points[event.x//step_x] [event.y//step_y]==-1:
     points[event.x//step_x] [event.y//step_y]=type
     draw_point(event.x//step_x, event.y//step_y,type)


canvas.bind_all('<Button-1>', add_to_points)
canvas.bind_all('<Button-3>', add_to_points)

def button_press():
    global list_ids
    global points
    print(list_ids)
    for i in list_ids:
     canvas.delete(i)
    list_ids = []
    print(list_ids)
    points = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

b1 = Button(tk,text='Новая игра',command=button_press())
b1.pack()
while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
