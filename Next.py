# AFTER CLICK ON NEXT BUTTON

from tkinter import *
import tkinter as tk
from PIL import Image ,ImageTk
from tkinter.ttk import *

root=tk.Tk()

# WINDOW TITLE
root.title("Obesity Detection Using Machine Learning Techniques")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

# FOR BACKGROUND IMAGE
image2 =Image.open('img2.jpg')
image2 =image2.resize((w,h))

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=87)

# TOP NEVIGATION BAR
w = tk.Label(root, text="                 Obesity Detection Using Machine Learning Techniques",bd=0, font=('times', 24,' bold '), anchor="w", justify="left",height=3, width=81,bg='#161A30',fg="white")
w.place(x=0, y=47,anchor="w")

w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="black")


from tkinter import messagebox as ms

# FOR OPEN PREDICTION PAGE
def call_file():
    from subprocess import call
    call(['python','Check1.py'])
    
# FOR EXIT BUTTON 
def window1():
    root.destroy()

# FOR DETECTION PAGE    
def window():
    from subprocess import call
    call(['python','GUI_Master.py'])

# SIDE CONTAINER
framed1 = tk.LabelFrame(root, text=" ", width=240, height=760, bd=0, font=('times', 14, ' bold '),bg="#708090",fg="white")
framed1.grid(row=0, column=0, sticky='nw')
framed1.place(x=0, y=102)

# LOGO IMAGE
image_path = "logo1.png"  # Path to your image file
image = Image.open(image_path)
image = image.resize((85,70))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo,borderwidth=0)
image_label.grid(row=0, column=0)
image_label.place(x=30, y=16)

# BUTTONS
exit1 = tk.Button(root, text="Prediction", command=call_file, width=15, height=2, font=('ubuntu', 15, ' bold '),bg="#FB2576",fg="white")
exit1.place(x=26, y=230)

exit2 = tk.Button(root, text="Exit", command=window1, width=15, height=2, font=('ubuntu', 15, ' bold '),bg="seagreen4",fg="white")
exit2.place(x=26, y=470)

exit2 = tk.Button(root, text="Detection", command=window, width=15, height=2, font=('ubuntu', 15, ' bold '),bg="#FB2576",fg="white")
exit2.place(x=26, y=340)


root.mainloop()
