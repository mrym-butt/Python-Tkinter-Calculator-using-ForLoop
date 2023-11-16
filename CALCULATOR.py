from tkinter import *

root=Tk()
root.geometry("300x400")
root.title("MY CALCULATOR")
root.wm_iconbitmap("calc-icon.ico")
def click(event):
    global strval
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if strval.get().isdigit():
            val=int(strval.get())
        else:
            val=eval(screen_widget.get())
        strval.set(val)
        screen_widget.update()
    elif text == "clr":
        strval.set("")
        screen_widget.update()
    else:
        strval.set(strval.get() + str(text))
        screen_widget.update()

strval=StringVar()
strval.set("")
screen_widget=Entry(root,textvariable=strval, font="Arial 10 bold")
screen_widget.pack(fill=X, padx=10,pady=10, ipadx=8)
# f2 = Frame(root)
# f2.pack(side=RIGHT,anchor="ne")
# for k in ["*", "/", "="]:
#     b2 = Button(f2, text=k, font="Arial 10 bold", padx=8, pady=8)
#     b2.pack(side=TOP)
#     b2.bind("<Button-1>", click)
f1=Frame(root,bg="grey")
f1.pack()
for i in range(9,0,-1):
    b=Button(f1, text=i, font="Arial 10 bold", padx=18,pady=18)
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)
    if (9 - i) % 3 == 2:
        f1 = Frame(root, bg="grey")
        f1.pack(pady=5)


for j in["0","-","+"]:
    b1=Button(f1, text=j, font="Arial 10 bold", padx=18,pady=18)
    b1.pack(side=LEFT)
    b1.bind("<Button-1>", click)

f2 = Frame(root, bg="grey")
f2.pack()
for k in ["*", "/", "="]:
    b2 = Button(f2, text=k, font="Arial 10 bold",padx=18,pady=18)
    b2.pack(side=LEFT)
    b2.bind("<Button-1>", click)


f1=Frame(root,bg="grey")
b=Button(f1, text="clr", font="Arial 10 bold", padx=63,pady=18, bg="aqua")
b.pack(side=LEFT, fill=BOTH)
b.bind("<Button-1>", click)
f1.pack()
root.mainloop()