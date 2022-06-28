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
    canvas.coords("tori",cx,cy)
    root.after(80,main_proc)

if __name__=="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg=mm.make_maze(15,9) #1壁 0床の二次元リスト
    mm.show_maze(canvas,maze_bg) #canvasにmaze_bgを描く
    tori=tk.PhotoImage(file="fig/9.png")
    mx, my=1 ,1
    cx, cy=mx*100+50, my*100+50
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key=""
    count=0
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()

