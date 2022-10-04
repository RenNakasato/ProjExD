import tkinter as tk
import math

sisoku = ""

# エントリーに数字を入力する
def click_button(event):
    btn = event.widget
    txt = btn["text"]
    if entry.get() == "" and txt in ["+","-","*","/"]:
        pass
    else:
        entry.insert(tk.END,txt)
    sioku = txt

#2乗の計算を行う関数
def click_rui_two(event):
    num = entry.get()
    txt = eval(num)
    txt = txt * txt
    entry.delete(0,tk.END)
    entry.insert(tk.END, txt)

#3乗の計算を行う関数
def click_rui_trhee(event):
    num = entry.get()
    txt = eval(num)
    txt = txt * txt * txt
    entry.delete(0,tk.END)
    entry.insert(tk.END, txt)

# ルートの計算を行う
def click_ru_to(event):
    num = entry.get()
    txt = eval(num)
    txt = math.sqrt(txt)
    entry.delete(0,tk.END)
    entry.insert(tk.END, txt)

#　エントリーを空にする
def click_clar(event):
    entry.delete(0, tk.END)
    
#エントリーの中身を確認し演算する。
def click_equal(event):
    num = entry.get()
    txt = eval(num)
    entry.delete(0,tk.END)
    entry.insert(tk.END, txt)


root = tk.Tk()
root.geometry("500x600")

entry = tk.Entry(root,
                 width=10,
                 font=("Times New Roman",40),
                 justify="right")

entry.grid(row=0,column=0,columnspan=8)

#r = row, c = column
r,c=1,1

#数字のボタンを作る
for i in range(9,-1,-1):
    button = tk.Button(root,text=i,font=("Times New Roman", 30),height=2,width=4)
    button.grid(row=r,column=c)
    button.bind("<1>",click_button)
    c +=1
    if c ==4:
        r +=1
        c = 1
# 小数点にする
button = tk.Button(root,text=".",font=("Times New Roman", 30),height=2,width=4)
button.grid(row=r,column=2)
button.bind("<1>",click_button)

#Cを追加して、押すとすべて消す
button_clar = tk.Button(root,text="c",font=("Times New Roman", 30),height=2,width=4)
button_clar.grid(row=1,column=7)
button_clar.bind("<1>",click_clar)

#^2を追加して、押すと2乗する
button_rui = tk.Button(root,text="^2",font=("Times New Roman", 30),height=2,width=4)
button_rui.grid(row=2,column=7)
button_rui.bind("<1>",click_rui_two)

# ^3を追加して、押すと3乗する
button_rui = tk.Button(root,text="^3",font=("Times New Roman", 30),height=2,width=4)
button_rui.grid(row=3,column=7)
button_rui.bind("<1>",click_rui_trhee)

#　ルートを追加して、押すとルートする。
button_ru_to = tk.Button(root,text="√",font=("Times New Roman", 30),height=2,width=4)
button_ru_to.grid(row=3,column=7)
button_ru_to.bind("<1>",click_ru_to)

# 四則演算関係
button_plus = tk.Button(root,text="+",font=("Times New Roman",30),height=2,width=4)
button_plus.grid(row=1,column=8)
button_plus.bind("<1>",click_button)

button_minus = tk.Button(root,text="-",font=("Times New Roman",30),height=2,width=4)
button_minus.grid(row=2,column=8)
button_minus.bind("<1>",click_button)

button_mult = tk.Button(root,text="*",font=("Times New Roman",30),height=2,width=4)
button_mult.grid(row=3,column=8)
button_mult.bind("<1>",click_button)

button_div = tk.Button(root,text="/",font=("Times New Roman",30),height=2,width=4)
button_div.grid(row=4,column=8)
button_div.bind("<1>",click_button)

#＝を行う
button_eq = tk.Button(root,text="=",font=("Times New Roman",30),height=2,width=4)
button_eq.grid(row=r,column=c+1)
button_eq.bind("<1>",click_equal)

root.mainloop()
