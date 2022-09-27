import random
import datetime
import time

taisyo = [] #対象文字列
kesson = [] #欠損文字列
max_num = 10 #ゲームの最大値
count = 0 #ゲームの回数

#問題の表示場所
def toi():
    global taisyo, kesson#対象文字列、欠損文字列
    #ない法表記でアルファベット出力
    alp = [chr(65+i) for i in range(26)]
    # random.sample(リスト,どのぐらいのサイズのものか)
    taisyo = random.sample(alp,k=5)
    kesson = random.sample(taisyo,k=2)
    #集合させて同じアルファベットを削除
    hyouzi = list(set(taisyo)-set(kesson))

    #表示
    print(f"対象文字:\n{taisyo}")
    print(f"欠損文字:\n{kesson}")
    print(f"表示文字:\n{hyouzi}")

#問題自体の処理
def kakunin():
    global kesson, count#欠損文字列、ゲーム回数
    #欠損文字が何個か聞く
    kes_num = len(kesson)
    user_ans = int(input("欠損文字はいくつあるでしょうか?:"))
    if user_ans == kes_num:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
        #removeによってリスト内の特定の文字を削除する
        for i in range(1,kes_num+1):
            user_fst = input(f"{i}つ目の文字を入力してください:")
            user_fst = user_fst.upper()
            if user_fst in kesson:
                kesson.remove(user_fst)
            else:
                break
        if len(kesson) == 0:
            print("正解です")
            count = 10
        else:
            print("不正解")
    else:
        print("不正解")
    count += 1


if __name__ == "__main__":

    st = datetime.datetime.now()
    #回数制限で10回まで
    while (count < max_num):
        print("\n")
        print("-"*10)
        toi()
        kakunin()
        time.sleep(3)
        print("\n")
        time.sleep(1)
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました")
