import tkinter as tk
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global mx, my
    global cx, cy
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
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()


    key = ""#4,5
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #9
    maze = mm.make_maze(15,9)
    mm.show_maze(canv, maze)

    tori = tk.PhotoImage(file="fig/5.png")#3
    mx, my = 1, 1
    cx, cy = mx*150, my*150
    canv.create_image(cx, cy, image=tori, tag="tori")
    main_proc()#7


    root.mainloop()