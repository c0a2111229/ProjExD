import random
import time

a=random.randint(0,2)
def shutudai(a):
    monndai=["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係"]
    print("問題：")
    print(monndai[a])

def kaito(a):
    time1=time.time()
    seikai=[["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
    b=input("答えるんだ：")
    if a==0 or a==1:
        if b==seikai[a][0] or b==seikai[a][1]:
            print("正解！！！")
        else:
            print("出直してこい")
    else:
        if b==seikai[a][0] or b==seikai[a][1] or b==seikai[a][2] or b==seikai[a][3]:
            print("正解！！！")
        else:
            print("出直してこい")
    time2=time.time()
    print(f"所要時間：{time2-time1}")
shutudai(a)
kaito(a)

