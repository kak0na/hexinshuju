import tkinter  as tk
from tkinter.messagebox import showinfo
windows=tk.Tk()
windows.title('学习')
windows.geometry('200x200')
def hit_me():
    showinfo('提示','hhahahahha')
b=tk.Button(windows,text='Hit me',command=hit_me).pack()


windows.mainloop()