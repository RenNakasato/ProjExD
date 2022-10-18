from curses import KEY_COPY
import tkinter as tk

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()

    tori = tk.PhotoImage(file="fig/5.png")#3
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRepleasr>", key_up)

    root.mainloop()