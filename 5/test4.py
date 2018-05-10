import tkinter  as tk


windows=tk.Tk()
windows.title('学习')
windows.geometry('200x200')
var=tk.StringVar()
l=tk.Label(windows,text='None',bg='yellow',width=15,height=2,font=20)
l.pack()
def selet():
    value=var.get()
    l.config(text='you selet'+value)

r1=tk.Radiobutton(windows,text='Option A',variable=var,value='A',command=selet)
r2=tk.Radiobutton(windows,text='Option B',variable=var,value='B',command=selet)
r3=tk.Radiobutton(windows,text='Option C',variable=var,value='C',command=selet)
r1.pack()
r2.pack()
r3.pack()
windows.mainloop()