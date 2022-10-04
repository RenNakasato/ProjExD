import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}が押されました")

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,
                 width=10,
                 font=("Times New Roman",40),
                 justify="right")

entry.grid(row=0,column=0,columnspan=4)

r,c=1,0
for i in range(9,-1,-1):
    button = tk.Button(root,text=i,font=("Times New Roman", 30),height=2,width=4)
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c +=1
    if c ==3:
        r +=1
        c = 0

root.mainloop()