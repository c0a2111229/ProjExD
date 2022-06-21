print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showwarning(txt,f"[{txt}]aaaaaaa")
root=tk.Tk()
root.title("aaaa")
root.geometry("500x200")
label=tk.Label(root,
               text="ラベルaaaaaaaaaaaaaaaaa",
               font=("Ricty diminished",20))
label.pack()
button=tk.Button(root,text="push",command=button_click)
button.bind("<1>",button_click)
button.pack()
entry=tk.Entry(width=30)
entry.insert(tk.END,"aaaaa")
entry.pack()
root.mainloop()
