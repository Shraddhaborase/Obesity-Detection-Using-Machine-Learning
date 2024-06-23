# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
#from pymsgbox import *


root=tk.Tk()

root.title("Automated menu planning Using Machine Learning")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('a3.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Automated menu planning Using Machine Learning",width=100,background="purple",height=2,font=("Times new roman",19,"bold"))
w.place(x=70,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="purple")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......Welcome to Automated menu planning Analysis  System ......",width=95,height=3,background="purple",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=750)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="purple",foreground="black",font=("times new roman",14,"bold"))
d2.place(x=1200,y=18)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="purple",foreground="black",font=("times new roman",14,"bold"))
d3.place(x=1300,y=18)



root.mainloop()
