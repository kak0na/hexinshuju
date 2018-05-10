import tkinter  as tk


windows=tk.Tk()
windows.title('学习')
windows.geometry('200x200')
e=tk.Entry(windows,show=None)
e.pack()
def into_point():
    var=e.get()
    t.insert('insert',var)
def into_end():
    var=e.get()
    t.insert('end',var)
b1=tk.Button(windows,text='into_point',command=into_point,width=15,height=2)
b2=tk.Button(windows,text='into_end',command=into_end,width=15,height=2)
t=tk.Text(windows,height=2)
b1.pack()
b2.pack()
t.pack()
windows.mainloop()