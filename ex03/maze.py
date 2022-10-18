import tkinter as tk
from turtle import goto
import maze_maker as mm
import random
import tkinter.messagebox as tkm
import datetime

def key_down(event):
    global key, maze
    global mx, cx, my, cy
    global st, gt
    key = event.keysym
    if key == "c":
        mx, my = 1, 1
        cx, cy = mx*150, my*150
        st, gt = 0, 0
        canv.coords("tori", cx, cy)
        canv.create_rectangle(100, 0, 200, 100, fill ="gray")
        canv.create_rectangle(1300, 800, 1400, 900, fill = "gray")
    if key=="g":
        mx, my = 1, 1
        cx, cy = mx*150, my*150
        canv.coords("tori", cx, cy)
        canv.create_rectangle(100, 0, 200, 100, fill = "blue")
        canv.create_rectangle(1300, 800, 1400, 900, fill = "red")
        st = datetime.datetime.now()

def gaol():
    global mx, my
    global cx, cy
    global maze
    global st, gt
    if cx >= 1300 and cx < 1500 and cy >= 700 and cy < 900 and st != 0:
        gt = datetime.datetime.now()
        time = gt -st
        tkm.showinfo("おめでとう", f"{time}でクリアしました")
        canv.create_rectangle(100, 0, 200, 100, fill ="gray")
        canv.create_rectangle(1300, 800, 1400, 900, fill = "gray")
        st = 0

def key_up(event):
    global key
    key = ""


def main_proc():
    global mx, my
    global cx, cy
    global maze
    global st, gt
    if key =="Up":
        my -= 1
    if key =="Down":
        my +=1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        mx,my = int((cx-50)/100),int((cy-50)/100)
    canv.coords("tori", cx, cy)
    gaol()
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()


    key = ""#4,5
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    # #9
    maze = mm.make_maze(15,9)
    mm.show_maze(canv, maze)

    num = random.randint(0, 8)
    tori = tk.PhotoImage(file=f"fig/{num}.png")#3
    mx, my = 1, 1
    cx, cy = mx*150, my*150
    canv.create_image(cx, cy, image=tori, tag="tori")
    main_proc()#7

    st, gt = 0, 0



    root.mainloop()