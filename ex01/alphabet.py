import random
import datetime


taisyo = []
kesson = []

count = 0

def toi():
    global taisyo, kesson
    alp = [chr(65+i) for i in range(26)]
    taisyo = random.sample(alp,k=5)
    kesson = random.sample(taisyo,k=2)
    hyouzi = list(set(taisyo)-set(kesson))

    print(f"対象文字:\n{taisyo}")
    print(f"欠損文字:\n{kesson}")
    print(f"表示文字:\n{hyouzi}")


def kakunin():
    global kesson, count
    kes_num = len(kesson)
    user_ans = int(input("欠損文字はいくつあるでしょうか?:"))
    if user_ans == kes_num:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
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
    while (count < 10):
        print("\n"*2)
        print("-"*10)
        taisyo = []
        kesson = []
        toi()
        kakunin()
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました")
