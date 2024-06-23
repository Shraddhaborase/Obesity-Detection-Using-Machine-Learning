
# LOW WEIGHT DETECTED

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1210x700")
root.title("Low Weight")

# FOR BACKGROUND IMAGE
image2 = Image.open('Low.jpg')
image2 = image2.resize((1550,800))  # Set the desired width and height
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=1, y=1)

# TOP HEADER
lbl = tk.Label(root, text="                 Obesity Detection Using Machine Learning Techniques",bd=0, font=('times', 24,' bold '), anchor="w", justify="left",height=3, width=81,bg='#161A30',fg="white")
lbl.place(x=0, y=47,anchor="w")

# TOP HEADER ICON
image_path = "logo1.png"  # Path to your image file
image = Image.open(image_path)
image = image.resize((85,70))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo,borderwidth=0)
image_label.grid(row=0, column=0)
image_label.place(x=30, y=16)

# TITLE
text_label = tk.Label(root, text="LOW WEIGHT DETECTED..!", font=("times", 21, "bold"), fg="firebrick1", bg="white")
text_label.place(x=420, y=250, anchor=tk.CENTER)

# FOR INFORMATION
info1=tk.Label(root,text="➊ Eat More Fruits and Vegetables :",background="white",font=('times', 16, ' bold '),fg='seagreen4')
info1.place(x=135,y=300,anchor="w")

info1=tk.Label(root,text="● Focus on filling your plate with whole vegetables and fruits at every\nmeal.Aim for lots of natural colors—carrots, sweet potatoes, broccoli,\nbananas,ETC High protein foods include meats, fish, eggs, some dairy\nproducts,legumes, nuts, and others.",anchor="w", justify="left",background="white",font=('kinnari', 12, ' bold '),fg='gray17')
info1.place(x=135,y=320)

info1=tk.Label(root,text="➋ Lifestyle changes :",background="white",font=('times', 16, ' bold '),fg='seagreen4')
info1.place(x=135,y=440,anchor="w")

info1=tk.Label(root,text="● Regular exercise is also important for everyone Getting enough sleep,\nmanaging stress,quitting smoking can all improve your overall health\nand reduce your risk of chronic diseases.",anchor="w", justify="left",background="white",font=('kinnari', 12, ' bold '),fg='gray17')
info1.place(x=135,y=460)

info1=tk.Label(root,text="☻ Thank You ☻",background="white",font=('times', 16, ' bold '),fg='#8470FF')
info1.place(x=320,y=690)

root.mainloop()
