import tkinter  as tk


windows=tk.Tk()
windows.title('学习')
windows.geometry('200x200')
l=tk.Label(windows,text='',bg='yellow')
l.pack()
count=0
def do_job():
    global count
    count += 1
    print(count)
    l.config(text='DO '+str(count))

menubar=tk.Menu(windows)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=windows.quit)

editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Paste',command=do_job)


submenu=tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=1)
submenu.add_command(label='submenu1',command=do_job)




windows.config(menu=menubar)


windows.mainloop()