import random
import time
import copy
taisyou=10
kesson=2
kurikae=5
def monndai(x,y):
    az=[chr(ord("A")+i) for i in range(26)]
    tai=[]
    hyou=[]
    ke=[]
    for i in range(x):
        a=random.randint(0,25-i)
        tai.append(az.pop(a))
    hyou=copy.copy(tai)
    for j in range(y):
        b=random.randint(0,9-j)
        ke.append(hyou.pop(b))
    random.shuffle(hyou)
    print("対象文字：")
    print(" ".join(tai))
    print("表示文字：")
    print(" ".join(hyou))
    return ke

def quiz(a):
    start=time.time()
    while a>0:
        ke=monndai(taisyou,kesson)
        ke.sort()
        ans1=input("欠損文字はいくつあるでしょうか？")
        if ans1==str(kesson):
            print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
            ans2=input("1つ目の文字を入力してください")
            ans3=input("2つ目の文字を入力してください")
            if ans2==ke[0] and ans3==ke[1]:
                end=time.time()
                print("正解です！！")
                print(f"所要時間：{end-start:.1f}")
                break
            else:
                print("不正解です。またチャレンジしてください")
                print("-"*30)
                a-=1
        else:
            print("不正解です。またチャレンジしてください")
            print("-"*30)
            a-=1
quiz(kurikae)


            