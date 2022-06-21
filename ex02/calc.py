import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンが押されました")

if __name__=='__main__':
    root=tk.Tk()
    root.title("電卓") #タイトル
    root.geometry("300x500") #500x300の大きさのウィジェットを生成
    r=0
    c=0
    num=0
    for i in [9,8,7,6,5,4,3,2,1,0]: #ボタンの作成
        button=tk.Button(root,text=i,font=("Times New Roman",30)
                        ,width=4,height=2,command=button_click)
        if num%3==0:
            r+=1
            c=0
        button.grid(row=r,column=c)
        c+=1
        num+=1
        button.bind("<1>",button_click)
    root.mainloop()

    