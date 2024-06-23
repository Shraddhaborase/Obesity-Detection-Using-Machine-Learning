# 1st Page

from tkinter import *
import tkinter as tk
from PIL import Image ,ImageTk
from tkinter.ttk import *
from tkvideo import tkvideo


root=tk.Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
video_label =tk.Label(root)
video_label.pack()


#Background Video
player = tkvideo("bg video.mp4", video_label,loop = 1, size = (1540,780)) 
player.play()

#Window Title
root.title("Obesity Detection Using Machine Learning Techniques")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

#Top Navigation Bar
w = tk.Label(root, text="                                                       Obesity Detection Using Machine Learning Techniques",bd=0, font=('times', 24,' bold '), anchor="w", justify="left",height=3, width=81,bg='#161A30',fg="white")
w.place(x=0, y=47,anchor="w")

w,h = root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="white")

#login backside Container
Login_frame=tk.Frame(root,bg="#708090")
Login_frame.place(x=54,y=295,height=250,width=160)


from tkinter import messagebox as ms

def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


#Botttom Header Bar
wlcm=tk.Label(root,text="Welcome to Obesity Detection System",width=110,height=2,background="#40679E",foreground="black",font=("opensymbol",17,"bold"))
wlcm.place(x=0,y=737)

#Login Button
d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=1,background="#FB2576",foreground="white",font=("ubuntu",14,"bold"))
d2.place(x=80,y=350)

#Register Button
d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=1,background="#FB2576",foreground="white",font=("ubuntu",14,"bold"))
d3.place(x=80,y=450)


root.mainloop()
