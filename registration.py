# REGISTRATION FORM

import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os

window = tk.Tk()
window.geometry("700x700+200+50")
window.title("REGISTRATION FORM")
window.configure(background="grey")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# DATABASE CODE
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()


# PASSWORD CHECK
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # to check mail
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
        
        
    # VALIDATION
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            window.destroy()
            from subprocess import call
            call(["python", "Login.py"])

# FOE BACKGROUND IMAGE
image2 = Image.open('reg bg.jpg')
image2 = image2.resize((1530, 787))

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0) 

# REGISTRATION HEADING
l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="#192841", fg="white")
l1.place(x=250, y=60)

# FULL NAME LABELS
l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=200, y=170)

# ENTRY
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=400, y=170)

# ADDRESS LABELS
l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=200, y=220)

# ENTRY
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=400, y=220)

# EMAIL LABELS
l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=200, y=270)

# ENTRY
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=400, y=270)

# NUMBER LABELS
l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=200, y=320)

# ENTRY
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=400, y=320)

# GENDER LABEL
l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=200, y=370)

# DOT BUTTON
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=400,
                                                                                                                y=370)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(
    x=510, y=370)

# AGE LABEL
l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=200, y=420)

# ENTRY
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=400, y=420)

# USER NAME LABEL
l4 = tk.Label(window, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=200, y=470)

# ENTRY
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=400, y=470)

# PASSWORD LABEL
l9 = tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=200, y=520)

# ENTRY
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=400, y=520)

# CON PASSWORD LABEL
l10 = tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=200, y=570)

# ENTRY
t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=400, y=570)

# BUTTON
btn = tk.Button(window, text="Register", bg="#EEAD0E",font=("ubuntu",18),fg="black", width=9, height=1, command=insert, bd=1)
btn.place(x=320, y=660)

window.mainloop()