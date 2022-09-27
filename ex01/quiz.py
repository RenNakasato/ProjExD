import random

#問題集
quizs_anss = [{"サザエの旦那の名前は？":["ますお","マスオ"]},
            {"カツオの妹の名前は？":["わかめ","ワカメ"]},
            {"タラオはカツオから見てどんな関係？":["甥","おい","甥っ子","おいっこ"]}]

def shutudai():

    #今回の問題
    quiz_ans = random.choice(quizs_anss)
    quiz = quiz_ans.keys()
    ans = quiz_ans.values()

    print("問題")
    print(quiz)

    return ans

def kaito(ans):
    user_ans = input("答えるんだ:")

    if user_ans in ans:
        print("正解")
    else:
        print("不正解")

#if __name__ == "__main__":

answer = shutudai()

kaito(answer)
