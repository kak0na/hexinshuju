import tkinter as tk
import pickle
from tkinter.messagebox import showinfo,showerror,showwarning,askyesno

window=tk.Tk()
window.title('Welcome to Dana Python')
window.geometry('450x300')
#welcome image
canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#user information
tk.Label(window,text='User name:',font=('微软雅黑,20')).place(x=50,y=170)
tk.Label(window,text='Password:',font=('微软雅黑,20')).place(x=50,y=220)

var_usr_name=tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=170)

var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=220)
#login
def usr_login():
    usr_name=var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_pwd=='':
        tk.Label(window,text='请输入密码再试',fg='red').place(x=170,y=240)
        return ''
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            showinfo('Welcome','How are you?'+usr_name)
        else:
            showerror('Error','Error,your password is error')
    else:
        is_sign_up=askyesno('Welcome','You have not sign up yet.Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():

    def sign_to_file():
        nn=new_name.get()
        np=new_pwd.get()
        np2 = new_pwd2.get()
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
        if np!=np2:
            showerror('Error','密码不一致')
        elif nn in usrs_info:
            showerror('Error','该用户已经注册过了')
        elif np=='':
            showerror('Error','密码为空')
        else:
            usrs_info[nn]=np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(usrs_info, usr_file)
            showinfo('Welcome','注册成功')
            window_sign_up.destroy()
    def quit1():
        window_sign_up.destroy()
    global window_sign_up
    try:
        window_sign_up.destroy()
    except:
        pass
    window_sign_up=tk.Toplevel(window)
    window_sign_up.title('Sign up window')
    window_sign_up.geometry('350x200')

    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='New name:').place(x=50,y=30)
    new_name_entry =tk.Entry(window_sign_up,textvariable=new_name).place(x=170,y=30)

    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='New password:').place(x=50,y=80)
    new_pwd_entry =tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=170,y=80)

    new_pwd2=tk.StringVar()
    tk.Label(window_sign_up,text='Confirm Password:').place(x=50,y=130)
    new_pwd2_entry =tk.Entry(window_sign_up,textvariable=new_pwd2,show='*').place(x=170,y=130)

    new_sign_up=tk.Button(window_sign_up,text='Sign Up',command=sign_to_file)
    new_sign_up.place(x=110,y=160)

    new_quit=tk.Button(window_sign_up,text='Quit',command=quit1)
    new_quit.place(x=210,y=160)

btn_login=tk.Button(window,text='Login',command=usr_login)
btn_login.place(x=170,y=260)

btn_login=tk.Button(window,text='Sign up',command=usr_sign_up)
btn_login.place(x=250,y=260)


window.resizable(0,0)
window.mainloop()