# PREDICTION 
from tkinter import *
import tkinter as tk
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from PIL import Image, ImageTk
import subprocess
from PIL import Image, ImageTk
def Train():
    """GUI"""
    

    root = tk.Tk()

    root.geometry("1700x1100")
    root.title("Comparison of Clustering Methods for Obesity Classification")
    root.configure(background="#152238")
    


   # Load and convert background image
    background_image = Image.open("img10.jpg")
    background_image = ImageTk.PhotoImage(background_image)
   
   # Create a label to hold the background image
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1) 
    
    Gender = tk.IntVar()
    Age = tk.IntVar()
    Height= tk.IntVar()
    Weight= tk.IntVar()
    family_history = tk.IntVar()
    FAVC= tk.IntVar()
    FCVC= tk.IntVar()
    NCP= tk.IntVar()
    CAEC= tk.IntVar()
    SMOKE= tk.IntVar()
    CH2O= tk.IntVar()
    SCC= tk.IntVar()
    FAF= tk.IntVar()
    TUE= tk.IntVar()
    CALC= tk.IntVar()
    MTRANS= tk.IntVar()
   
    
    
    def Detect():
        
        
        e1= Gender.get()
        print(e1)
        e2=Age.get()
        print(e2)
        e3= Height.get()
        print(e3)
        e4=Weight.get()
        print(e4)
        e5=family_history.get()
        print(e5)
        e6=FAVC.get()
        print(e6)
        e7=FCVC.get()
        print(e7)
        e8=NCP.get()
        print(e8)
        e9=CAEC.get()
        print(e9)
        e10=SMOKE.get()
        print(e10)
        e11=CH2O.get()
        print(e11)
        e12=SCC.get()
        print(e12)
        e13=FAF.get()
        print(e13)
        e14=TUE.get()
        print(e14)
        e15=CALC.get()
        print(e15)
        e16=MTRANS.get()
        print(e16)
        
        
        from joblib import dump ,load
        a1=load(r'DT_wt1.joblib')
        v= a1.predict([[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]])
        print(v)
        
        
        if v[0]==0:
            print("YHH..😝 LOW UNDER WEIGHT DETECTED..!")
            yes = tk.Label(root,text="YHH..😝 LOW UNDER WEIGHT DETECTED..!",background="green",foreground="white",font=('times', 20, ' bold '),width=70)
            yes.place(x=350,y=710)
            from subprocess import call
            call(["python","low.py"])
        elif v[0]==1:
            print("Ohhhh..😎 MEDIUM NORMAL WEIGHT DETECTED..! ")
            no = tk.Label(root, text="Ohhhh..😎 MEDIUM NORMAL WEIGHT DETECTED..! ", background="GREEN", foreground="white",font=('times', 20, ' bold '),width=70)
            no.place(x=350,y=710)
            from subprocess import call
            call(["python","medium.py"])
        elif v[0]==2:
            print("OOPS..😯 VERY HIGH OBESE WEIGHT DETECTED..!")
            no = tk.Label(root, text="OOPS..😯 VERY HIGH OBESE WEIGHT DETECTED..!", background="brown", foreground="white",font=('times', 20, ' bold '),width=70)
            no.place(x=350,y=710)
            from subprocess import call
            call(["python","extrme.py"])
        elif v[0]==3:
            print("OOPS..😯 HIGH OVER WEIGHT DETECTED..")
            no = tk.Label(root, text="OOPS..😯  HIGH OVER WEIGHT DETECTED..", background="brown", foreground="white",font=('times', 20, ' bold '),width=70)
            no.place(x=350,y=710)
            from subprocess import call
            call(["python","high.py"])
        

    
        
    # TOP HEADER
    lbl = tk.Label(root, text="                  Obesity Detection Using Machine Learning Techniques",bd=0, font=('times', 24,' bold '), anchor="w", justify="left",height=3, width=81,bg='#161A30',fg="white")
    lbl.place(x=0, y=47,anchor="w")
    
    # LOGO IMAGE
    image_path = "logo1.png"  # Path to your image file
    image = Image.open(image_path)
    image = image.resize((85,70))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo,borderwidth=0)
    image_label.grid(row=0, column=0)
    image_label.place(x=30, y=16)
    
    # TITLE
    l1=tk.Label(root,text="     Prediction Information     ",background="palevioletred3",font=('times', 17, ' bold '))
    l1.place(x=760,y=135)
    
    # SIDE CONTAINER
    framed1 = tk.LabelFrame(root, text=" ", width=290, height=760, bd=0, font=('times', 14, ' bold '),bg="#708090",fg="white")
    framed1.grid(row=0, column=0, sticky='nw')
    framed1.place(x=0, y=102)
    
    #MORE BUTTON OPTION
    def show_more_options():
   
       label1=tk.Label(root,text="☞ Frequency of consumption\nvegetables(FCVC) range 1-4.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label1.place(x=5,y=400)

       label2=tk.Label(root,text="☞ Number of main meals (NCP)\nrange 1-4.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label2.place(x=5,y=450)

       label3=tk.Label(root,text="☞ Consumption of food between\nmeals(CAEC)No(0),Sometimes(1),\nFrequent(2),Always(3).",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label3.place(x=5,y=500)
        
       label4=tk.Label(root,text="☞ Smoking :YES(1) or NO(0).",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label4.place(x=5,y=570)
       
       label5=tk.Label(root,text="☞ Consumption of water daily\n(CH20) in liters.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label5.place(x=5,y=600)

       label6=tk.Label(root,text="☞ Calories consumption monitor-\ning (SCC) yes(1) or no(2).",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label6.place(x=5,y=650)

       label7=tk.Label(root,text="☞ Physical activity frequency(FAF)\nrange 0-3.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label7.place(x=5,y=700)

       label8=tk.Label(root,text="☞ Time using technology devices\n(TUE)range 0-2.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
       label8.place(x=5,y=750)


# Add a button to show more options
    more_button = tk.Button(root, text="MORE", command=show_more_options, bg="#708090", fg="#161A30", height=2, width=10,bd=0,font=('times', 13, ' bold '))
    more_button.place(x=0, y=400) 

        
    # FOR SIDE CONTAINER INFO
    info=tk.Label(root,text="NOTE",background="#708090",font=('times', 17, ' bold '),fg='#C40C0C')
    info.place(x=95,y=140)

    info1=tk.Label(root,text="☞ Gender : Male(1) & Female(0).",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17')
    info1.place(x=5,y=180)
    
    info1=tk.Label(root,text="☞ Age : In the range 16 - 25.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17')
    info1.place(x=5,y=210)
    
    info1=tk.Label(root,text="☞ Height : Measured in metres.",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17')
    info1.place(x=5,y=240)
    
    info1=tk.Label(root,text="☞ Weight : Measured in Kilogram",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
    info1.place(x=5,y=270)
    
    info1=tk.Label(root,text="☞ Family History : with overweight\nyes(1) or no(0).",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
    info1.place(x=5,y=300)

    info1=tk.Label(root,text="☞ Frequent consumption of high\ncaloric food (yes(1) or no(0)).",background="#708090",font=('kinnari', 13, ' bold '),fg='gray17',anchor="w", justify="left")
    info1.place(x=5,y=350)

    

    
    
    # FOR INPUTS DATA
    l1=tk.Label(root,text="Gender",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l1.place(x=420,y=210)
    Gender=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=Gender)
    Gender.place(x=675,y=210)

    l2=tk.Label(root,text="Age",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l2.place(x=420,y=260)
    Age=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar= Age)
    Age.place(x=675,y=260)
    
    l3=tk.Label(root,text="Height",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l3.place(x=420,y=310)
    Height=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=Height)
    Height.place(x=675,y=310)
    
    l4=tk.Label(root,text="Weight",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l4.place(x=420,y=360)
    Weight=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=Weight)
    Weight.place(x=675,y=360)
    
    l5=tk.Label(root,text="family_history",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l5.place(x=420,y=410)
    family_history=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=family_history)
    family_history.place(x=675,y=410)
  
    l6=tk.Label(root,text="FAVC",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l6.place(x=420,y=460)
    FAVC=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=FAVC)
    FAVC.place(x=675,y=460)
    
    l7=tk.Label(root,text="FCVC",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l7.place(x=420,y=510)
    FCVC=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=FCVC)
    FCVC.place(x=675,y=510)
    
    l8=tk.Label(root,text="NCP",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l8.place(x=420,y=560)
    NCP=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=NCP)
    NCP.place(x=675,y=560)
     
    l9=tk.Label(root,text="CAEC",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l9.place(x=920,y=210)
    CAEC=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=CAEC)
    CAEC.place(x=1175,y=210)
     
    l10=tk.Label(root,text="SMOKE",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l10.place(x=920,y=260)
    SMOKE=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=SMOKE)
    SMOKE.place(x=1175,y=260)
    
    l11=tk.Label(root,text="CH2O",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l11.place(x=920,y=310)
    CH2O=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=CH2O)
    CH2O.place(x=1175,y=310)
    
    l12=tk.Label(root,text="SCC",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l12.place(x=920,y=360)
    SCC=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=SCC)
    SCC.place(x=1175,y=360)
    
    l13=tk.Label(root,text="FAF",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l13.place(x=920,y=410)
    FAF=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=FAF)
    FAF.place(x=1175,y=410)
    
    l14=tk.Label(root,text="TUE",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l14.place(x=920,y=460)
    TUE=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=TUE)
    TUE.place(x=1175,y=460)
    
    l15=tk.Label(root,text="CALC",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l15.place(x=920,y=510)
    CALC=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=CALC)
    CALC.place(x=1175,y=510)
    
    l16=tk.Label(root,text="MTRANS",background="lightblue4",font=('times', 20, ' bold '),width=15)
    l16.place(x=920,y=560)
    MTRANS=tk.Entry(root,bd=2,width=15,font=("times", 20),textvar=MTRANS)
    MTRANS.place(x=1175,y=560)
    
    # SUBMIT BUTTON
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=12,bg="darkgoldenrod2")
    button1.place(x=810,y=630)


    root.mainloop()

Train()
 