from tkinter import *
from tkinter import messagebox
import time
import random


tk = Tk()
app_running = True

def on_closing():
    global app_running
    if messagebox.askokcancel('Quit','Do you want to quit?'):
        app_running = False
        tk.destroy()

tk.protocol('LM_DELETE_WINDOW', on_closing)

tk.title('Cross and Circles')
tk.resizable(0,0)
canvas = Canvas(tk,width=1200,height=768,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
s_x = 3
s_y = 3
def draw_table():
    pass

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
