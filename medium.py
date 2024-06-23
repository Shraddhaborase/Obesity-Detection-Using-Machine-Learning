
# MEDIUM WEIGHT DETECTED

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1200x700")
root.title("Normal Weight")

# FOR BACKGROUND IMAGE
image2 = Image.open('medium.jpg')
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
text_label = tk.Label(root, text="NORMAL WEIGHT DETECTED..!", font=("times", 20, "bold"), fg="firebrick1", bg="white")
text_label.place(x=418, y=260, anchor=tk.CENTER)

# FOR INFORMATION
info1=tk.Label(root,text="➊ You look normal weight, but have extra body fat that\ncan cause health problems. ",background="white",font=('kinnari', 15, ' bold '),fg='gray17',anchor="w", justify="left")
info1.place(x=135,y=340,anchor="w")

info1=tk.Label(root,text="➋ Focus on healthy eating: fruits, veggies, whole grains,\nditch sugary drinks and processed foods.",anchor="w", justify="left",background="white",font=('kinnari', 15, ' bold '),fg='gray17')
info1.place(x=135,y=380)

info1=tk.Label(root,text="➌ Move your body most days: 30 minutes of exercise is\nkey.",background="white",anchor="w", justify="left",font=('kinnari', 15, ' bold '),fg='gray17')
info1.place(x=135,y=450)

info1=tk.Label(root,text="➍ Talk to your doctor: they can help with a personalized\nplan.",background="white",font=('kinnari', 15, ' bold '),fg='gray17',anchor="w", justify="left")
info1.place(x=135,y=540,anchor="w")

info1=tk.Label(root,text="➎ Getting enough sleep, managing stress,quitting smok-\ningcan all improve your overall health and reduce your risk\nof chronic diseases.",anchor="w", justify="left",background="white",font=('kinnari', 15, ' bold '),fg='gray17')
info1.place(x=135,y=580)


info1=tk.Label(root,text="☻ Thank You ☻",background="white",font=('times', 16, ' bold '),fg='#8470FF')
info1.place(x=320,y=690)

root.mainloop()