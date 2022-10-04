import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}が押されました")

root = tk.Tk()
root.geometry("300x500")

r,c=0,0
for i in range(9,-1,-1):
    button = tk.Button(root,text=i,font=("Times New Roman", 30),height=2,width=4)
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c +=1
    if c ==2:
        r +=1
        c = 0

root.mainloop()