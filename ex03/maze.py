from email.mime import image
import imghdr
import tkinter as tk
from venv import create




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #１

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()

    tori = tk.PhotoImage(file="fig/5.png")#3
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    root.mainloop()