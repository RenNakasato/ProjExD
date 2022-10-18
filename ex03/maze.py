import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import datetime
import random

#全グローバル変数の説明
#key, mazu,
#どのキーが押されたかを記録、壁と床の判定、
#mx, my, cx,cy,
#キャラクターの移動関係*2、キャラクターの実際の位置*2
#st, gt
#ゲームモードの開始時間、ゲームモードの終了時間

def key_down(event):
    global key, mx, my, cx,cy, st, gt
    key = event.keysym
    # 何かあった時に全てを初期状態に変更する
    if key == "c":
        mx, my = 1, 1
        cx, cy = mx*150, my*150
        st, gt = 0, 0
        canv.coords("tori", cx, cy)
        canv.create_rectangle(100, 0, 200, 100, fill ="gray")
        canv.create_rectangle(1300, 800, 1400, 900, fill = "gray")
    #　ゲームモードの起動、青から赤に行くとクリアー
    if key=="g":
        mx, my = 1, 1
        cx, cy = mx*150, my*150
        canv.coords("tori", cx, cy)
        canv.create_rectangle(100, 0, 200, 100, fill = "blue")
        canv.create_text(150,50, text="S",fill="white",font=("", 50))
        canv.create_rectangle(1300, 800, 1400, 900, fill = "red")
        canv.create_text(1350,850, text="G",fill="white", font=("", 50))
        st = datetime.datetime.now()

#　ゲームモードのクリアの時間
def gaol():
    global mx, my, cx, cy, maze, st, gt
    if cx >= 1300 and cx < 1500 and cy >= 700 and cy < 900 and st != 0:
        gt = datetime.datetime.now()
        time = gt -st
        tkm.showinfo("おめでとう", f"{time}でクリアしました")
        #　tkmを使うことによりtkmをどうにかするまでで次の動きを封じる
        canv.create_rectangle(100, 0, 200, 100, fill ="gray")
        canv.create_rectangle(1300, 800, 1400, 900, fill = "gray")
        st = 0


def key_up(event):
    global key
    key = ""

#　矢印キーの動きとゲームモード時のクリア判定
def main_proc():
    global mx, my, cx, cy, maze,st, gt
    yazirusi = ["Up", "Down", "Left", "Right"]
    zougenn = [[-1,0],[1,0],[0,-1], [0,1]]
    if key in yazirusi:
        num = zougenn[yazirusi.index(key)]
        my += num[0]
        mx += num[1]
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

    #　起動時にランダムなこうかとんの画像にする
    num = random.randint(0, 8)
    tori = tk.PhotoImage(file=f"fig/{num}.png")#3
    mx, my = 1, 1
    cx, cy = mx*150, my*150
    canv.create_image(cx, cy, image=tori, tag="tori")
    main_proc()#7

    st, gt = 0, 0

    root.mainloop()