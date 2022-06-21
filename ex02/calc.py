import tkinter as tk
import tkinter.messagebox as tkm
import math
def button_click(event): #通知用の関数
    btn=event.widget
    txt=btn["text"]
    if txt=="=":
        eqn=entry.get()
        ans=eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    elif txt=="ac":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,txt)

if __name__=='__main__':
    root=tk.Tk()
    root.title("電卓") #タイトル
    entry=tk.Entry(root,justify="right",
                   width=10,font=("Times New Roman",40)) #画面上部の表示
    entry.grid(row=0,column=0,columnspan=3)
    r=1
    c=0
    num=0
    for i in [9,8,7,"*","/",6,5,4,"+","-",3,2,1,".","ac",0,"π","=","sin","cos","tan",]: #ボタンの作成
        button=tk.Button(root,text=i,
                        font=("Times New Roman",30),
                        width=4,height=2)
        if num%5==0:
            r+=1
            c=0
        button.grid(row=r,column=c)
        c+=1
        num+=1
        button.bind("<1>",button_click)
    root.mainloop()

    