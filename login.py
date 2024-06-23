#LOGIN PAGE

import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x650+200+50")
root.title("Login Form")

username = tk.StringVar()
password = tk.StringVar()
        
#For background Image
image2 = Image.open('img7.jpg')
image2 = image2.resize((1530, 787))
background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)  


def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

         # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            # ===========================================
            from subprocess import call
            call(['python',"GUI_Master_old.py"])
            root.destroy()

            from subprocess import call
            call(['python','gui_main.py'])

         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Match.')


# CONTAINER      
Login_frame=tk.Frame(root,bg="#708090")
Login_frame.place(x=500,y=250,height=300,width=540)

# TITLE
title=tk.Label(root, text="Login Here", font=("times", 25, "bold"),bd=0,bg="#708090")
title.place(x=640,y=270,width=250)      
logolbl=tk.Label(Login_frame,bd=1).grid(row=0,columnspan=2,pady=20)

# FOR USERNAME NAME        
lbluser=tk.Label(Login_frame,text="Username",compound=LEFT,font=("times", 20, "bold"),bg="#708090",).grid(row=1,column=0,padx=35,pady=30)

# USERNAME ENTRY
txtuser=tk.Entry(Login_frame,bd=1,textvariable=username,font=("",19))
txtuser.grid(row=1,column=1,padx=20)

# FOR PASSWORD       
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("times", 20, "bold"),bg="#708090").grid(row=2,column=0,padx=35,pady=0)

# PASSWORD ENTRY
txtpass=tk.Entry(Login_frame,bd=1,textvariable=password,show="*",font=("",19))
txtpass.grid(row=2,column=1,padx=20)

# LOGIN BUTTON       
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("ubuntu", 15, "bold"),bg="seagreen4")
btn_log.grid(row=3,column=1,pady=20)
btn_log.place(x=300,y=230)        

# REGISTER BUTTON       
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("ubuntu", 15, "bold"),bg="#FB2576")
btn_reg.grid(row=3,column=0,pady=25)
btn_reg.place(x=60,y=230)        
       

root.mainloop()