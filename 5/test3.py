import tkinter  as tk


windows=tk.Tk()
windows.title('学习')
windows.geometry('200x200')
var1=tk.StringVar()
l=tk.Label(windows,textvariable=var1,bg='yellow',width=15,height=2,font=20)
l.pack()

def into_point():
    value=lb.get(lb.curselection())
    var1.set(value)
b1=tk.Button(windows,text='into_point',command=into_point,width=15,height=2)
var2=tk.StringVar()
var2.set((11,22,33,44))
lb=tk.Listbox(windows,listvariable=var2)
lb.insert(1,'first')
b1.pack()
lb.pack()
windows.mainloop()