import tkinter  as tk


windows=tk.Tk()
windows.title('学习')
#windows.geometry('200x100')
var=tk.StringVar()
l=tk.Label(windows,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()

def hit_me1():
    var.set('现在显示1')
def hit_me2():
    var.set('现在显示2')
def hit_me3():
    var.set('现在显示3')
b1=tk.Button(windows,text='Hit me',command=hit_me1,width=15,height=2)
b2=tk.Button(windows,text='Hit me',command=hit_me2,width=15,height=2)
b3=tk.Button(windows,text='Hit me',command=hit_me3,width=15,height=2)
b1.pack()
b2.pack()
b3.pack()
windows.mainloop()