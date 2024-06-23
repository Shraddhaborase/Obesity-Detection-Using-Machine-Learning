# VERY HIGH OBESE WEIGHT DETECTED

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.configure(background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1200x700")
root.title("Very High Obese Weight")

# FOR BACKGROUND IMAGE
image2 = Image.open('extreme.jpg')
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
text_label = tk.Label(root, text="VERY HIGH OBESE WEIGHT DETECTED..!", font=("times", 20, "bold"), fg="firebrick1", bg="white")
text_label.place(x=418, y=240, anchor=tk.CENTER)

# FOR INFORMATION
info1=tk.Label(root,text="➊ Food to Avoid :",background="white",font=('times', 16, ' bold '),fg='seagreen4')
info1.place(x=135,y=280,anchor="w")

info1=tk.Label(root,text="● Processed foods These foods are often high in unhealthy fats, sodium,\nand sugar,Refined carbohydrates,such as white bread, pasta, and rice,\nare quickly digested and can cause spikes in blood sugar levels.",anchor="w", justify="left",background="white",font=('kinnari', 11, ' bold '),fg='gray17')
info1.place(x=135,y=300)

info1=tk.Label(root,text="● sugary drinks, such as soda, juice, and sports drinks, are a major source\nof empty calories.They can contribute to weight gain, type 2 diabetes,\nand heart disease.",background="white",anchor="w", justify="left",font=('kinnari', 11, ' bold '),fg='gray17')
info1.place(x=135,y=360)

info1=tk.Label(root,text="➋ Activities to avoid :",background="white",font=('times', 16, ' bold '),fg='seagreen4')
info1.place(x=135,y=440,anchor="w")

info1=tk.Label(root,text="● Sudden increases in activity level can be dangerous for people with high\nweight obesity Activities that put a lot of stress on the joints, such as\nrunning and jumping, should be avoided.\n● focus on low-impact activities, such as walking, swimming, and cycling.",anchor="w", justify="left",background="white",font=('kinnari', 11, ' bold '),fg='gray17')
info1.place(x=135,y=460)

info1=tk.Label(root,text="➌ Other things to avoid :",background="white",font=('times', 16, ' bold '),fg='seagreen4')
info1.place(x=135,y=560,anchor="w")

info1=tk.Label(root,text="● Stress can lead to unhealthy eating habits and make it difficult to lose \nweight .\n● healthy ways to manage stress, such as yoga or meditation.\n● Alcohol is high in calories and can contribute to weight gain.\n● Smoking is a major risk factor for heart disease, stroke, and lung cancer.",anchor="w", justify="left",background="white",font=('kinnari', 11, ' bold '),fg='gray17')
info1.place(x=135,y=580)

info1=tk.Label(root,text="☻ Thank You ☻",background="white",font=('times', 16, ' bold '),fg='#8470FF')
info1.place(x=320,y=690)

root.mainloop()
