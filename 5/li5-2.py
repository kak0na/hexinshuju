import tkinter

top=tkinter.Tk()
hello=tkinter.Label(top,text='''这是一个简单的程序''')
hello.pack()

quit=tkinter.Button(top,text='退出',command=top.quit,bg='red',fg='white')
quit.pack(fill=tkinter.X,expand=1)
tkinter.mainloop()