import tkinter as tk
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, key
    if key =="Up":
        cy -=20
    if key =="Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()

    tori = tk.PhotoImage(file="fig/5.png")#3
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""#4,5
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()#7

    #9
    maze = mm.make_maze(15,9)
    mm.show_maze(canv, maze)

    root.mainloop()