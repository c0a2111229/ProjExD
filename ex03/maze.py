import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key, count
    key=event.keysym
    count+=1

def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy,mx,my,tori
    delta={#キー：押されているkey,値のリスト：移動幅
           "":[0,0],
           "Up":[0,-1],"Down":[0,+1],
           "Left":[-1,0],"Right":[+1,0]}
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]]==0: #もし移動先が床なら移動する
            mx, my=mx+delta[key][0], my+delta[key][1]
    except:
        pass
    cx, cy=mx*100+50, my*100+50
    if 15<=count<25: #こうかとんの画像を押した回数で変更する
        tori=tk.PhotoImage(file="fig/5.png")
        canvas.create_image(cx,cy,image=tori,tag="tori")
    elif 25<=count<35: 
        tori=tk.PhotoImage(file="fig/7.png")
        canvas.create_image(cx,cy,image=tori,tag="tori")
    elif 35<=count: 
        tori=tk.PhotoImage(file="fig/8.png")
        canvas.create_image(cx,cy,image=tori,tag="tori")
    canvas.coords("tori",cx,cy)
    root.after(80,main_proc)

def button_break(event): #迷路の破壊関数
    global maze_bg
    for i in range(15): #maze_bgを作り変える
        for j in range(9):
            if maze_bg[j][i]==1:
                maze_bg[j][i]=0
    mm.show_maze(canvas,maze_bg)
    canvas.create_image(cx,cy,image=tori,tag="tori")
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,"全てが破壊されました...")

def button_create(event): #迷路の再構築関数
    global maze_bg
    maze_bg=mm.make_maze(15,9) #1壁 0床の二次元リスト
    mm.show_maze(canvas,maze_bg) #canvasにmaze_bgを描く
    canvas.create_rectangle(100, 100,100+100,100+100, 
                                    fill="yellow")
    canvas.create_rectangle(1500-100, 900-100, 1300, 700, 
                                    fill="red")
    canvas.create_image(cx,cy,image=tori,tag="tori")
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,"迷路が再構築されました")

if __name__=="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg=mm.make_maze(15,9) #1壁 0床の二次元リスト
    mm.show_maze(canvas,maze_bg) #canvasにmaze_bgを描く
    canvas.create_rectangle(100, 100,100+100,100+100, 
                                    fill="yellow") #スタート地点を黄色に設定
    canvas.create_rectangle(1500-100, 900-100, 1300, 700, 
                                    fill="red") #ゴール地点を赤色に設定
    button1=tk.Button(root,text="break",command=button_break,height=3,width=15)
    button1.bind("<1>",button_break) 
    button2=tk.Button(root,text="create",command=button_create,height=3,width=15)
    button2.bind("<1>",button_create)
    button1.pack() #breakボタンの生成
    button2.pack() #createボタンの生成
    tori=tk.PhotoImage(file="fig/9.png")
    mx, my=1 ,1
    cx, cy=mx*100+50, my*100+50
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key=""
    count=0 #ボタンを押した回数
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()

