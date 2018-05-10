import tkinter as tk

window=tk.Tk()
window.geometry('200x130')
tk.Button(window,text='100').place(x=10,y=100,anchor='nw')

window.mainloop()