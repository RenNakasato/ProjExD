import tkinter as tk
import tkinter.messagebox as tkm

def click_button(event):
    btn = event.widget
    txt = btn["text"]
    # tkm.showinfo(txt,f"{txt}が押されました")
    entry.insert(tk.END,txt)


def click_equal(event):
    num = entry.get()
    txt = eval(num)
    entry.delete(0,tk.END)
    entry.insert(tk.END, txt)



root = tk.Tk()
root.geometry("400x600")

entry = tk.Entry(root,
                 text=0,
                 width=10,
                 font=("Times New Roman",40),
                 justify="right")

entry.grid(row=0,column=0,columnspan=6)

r,c=1,0
for i in range(9,-1,-1):
    button = tk.Button(root,text=i,font=("Times New Roman", 30),height=2,width=4)
    button.grid(row=r,column=c)
    button.bind("<1>",click_button)
    c +=1
    if c ==3:
        r +=1
        c = 0

button_plus = tk.Button(root,text="+",font=("Times New Roman",30),height=2,width=4)
button_plus.grid(row=1,column=5)
button_plus.bind("<1>",click_button)

button_minus = tk.Button(root,text="-",font=("Times New Roman",30),height=2,width=4)
button_minus.grid(row=2,column=5)
button_minus.bind("<1>",click_button)

button_eq = tk.Button(root,text="=",font=("Times New Roman",30),height=2,width=4)
button_eq.grid(row=4,column=5)
button_eq.bind("<1>",click_equal)

root.mainloop()