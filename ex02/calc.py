import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event): #通知用の関数
    btn=event.widget
    txt=btn["text"]
    #tkm.showinfo(txt,f"{txt}のボタンが押されました")
    entry.insert(tk.END,txt)

if __name__=='__main__':
    root=tk.Tk()
    root.title("電卓") #タイトル
    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)
    r=1
    c=0
    num=0
    for i in [9,8,7,6,5,4,3,2,1,0,"+","="]: #ボタンの作成
        button=tk.Button(root,text=i,font=("Times New Roman",30)
                        ,width=4,height=2)
        if num%3==0:
            r+=1
            c=0
        button.grid(row=r,column=c)
        c+=1
        num+=1
        button.bind("<1>",button_click)
    root.mainloop()

    