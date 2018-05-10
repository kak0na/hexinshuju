import tkinter  as tk


windows=tk.Tk()
windows.title('学习')
windows.geometry('200x200')
var=tk.StringVar()
l=tk.Label(windows,text='None',bg='yellow',width=15,height=2,font=20)
l.pack()
def selet():
    if var1.get()==0 and var2.get()==0:l.config(text='都不喜欢')
    elif var1.get()==1 and var2.get()==0:l.config(text='只勾选了python')
    elif var1.get() == 0 and var2.get() == 1:l.config(text='只勾选了C++')
    else :l.config(text='两个都选了')
var1=tk.IntVar()
var2=tk.IntVar()
c1=tk.Checkbutton(windows,text='Python',variable=var1,onvalue=1,offvalue=0,command=selet)
c2=tk.Checkbutton(windows,text='C++',variable=var2,onvalue=1,offvalue=0,command=selet)
c1.pack()
c2.pack()
windows.mainloop()