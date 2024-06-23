# ALGORITHM PAGE

from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import warnings
import joblib
from joblib import dump
import pickle
from tkinter.ttk import *

# FOR WARNINGS
warnings.filterwarnings("ignore", category=DeprecationWarning)
 
root = tk.Tk()

#WINDOW TITLE
root.title("Comparison of Clustering Methods for Obesity Classification")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# BACKEND BACKGROUND IMAGE
image = Image.open('img5.jpg')
image = image.resize((w, h))

background_image = ImageTk.PhotoImage(image)
background_image=ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

# FRONT BACKGROUND IMAGE 
image = Image.open('a5.png')
image = image.resize((1293,720))

background_image = ImageTk.PhotoImage(image)
background_image=ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=240, y=90)


# TOP HEADER
lbl = tk.Label(root, text="                 Obesity Detection Using Machine Learning Techniques",bd=0, font=('times', 24,' bold '), anchor="w", justify="left",height=3, width=81,bg='#161A30',fg="white")
lbl.place(x=0, y=47,anchor="w")


# SVM MODEL TRAINING
def Model_Training():
    data = pd.read_csv("obesity.csv")
    data.head()

    data = data.dropna()
    
    """Feature Selection => Manual"""
    x = data.drop(['0be1dad'], axis=1)
    data = data.dropna()
    print(type(x))
    y = data['0be1dad']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123456)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    # AFTER CLICK ON SVM BUTTON CONTAINER
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#282A3A',fg='white',font=("boulder",14))
    label4.place(x=420,y=250)
    label5 = tk.Label(root,text ="Accuracy :"+str(ACC)+"%\nModel saved as SVM_wt1.joblib",width=43,height=2,bg='#282A3A',fg='#C69749',font=("boulder",14))
    label5.place(x=430,y=470)
    X = data.drop('0be1dad', axis=1)  # Adjust the column name according to your dataset
    y = data['0be1dad']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the SVM model
    svm_model = SVC()
    svm_model.fit(X_train_scaled, y_train)
    from joblib import dump
    dump (svcclassifier,"SVM_wt1.joblib")
    print("Model saved as SVM_wt1.joblib")
    svm_model = joblib.load("SVM_wt1.joblib")
    
    # Save the SVM model to a pickle file
    with open("SVM_wt.pkl1", "wb") as file:
        pickle.dump(svm_model, file)
    with open("scaler.pkl1", "wb") as file:
        pickle.dump(scaler, file)

#  DT MODEL TRAINING
def DT():
    data = pd.read_csv("obesity.csv")
    data.head()
    data = data.dropna()
    """Feature Selection => Manual"""
    x = data.drop(['0be1dad'], axis=1)
    data = data.dropna()
    print(type(x))
    y = data['0be1dad']
    print(type(y))
    x.shape
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=2)

    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier(criterion='entropy', random_state=0)  
    svcclassifier.fit(x_train, y_train)
    y_pred = svcclassifier.predict(x_test)
   
    print(y_pred)
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
        
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()

    # ACCURACY CONTAINER
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#282A3A',fg='white',font=("boulder",14))
    label4.place(x=420,y=250)
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as DT_wt1.joblib",width=45,height=3,bg='#282A3A',fg='#C69749',font=("boulder",14))
    label5.place(x=420,y=470)
    from joblib import dump
    dump (svcclassifier,"DT_wt1.joblib")
    print("Model saved as DT_wt1.joblib")

# RF MODEL TRAINING
def RF():
    data = pd.read_csv("obesity.csv")
    data.head()
    data = data.dropna()
    """Feature Selection => Manual"""
    x = data.drop(['0be1dad'], axis=1)
    data = data.dropna()
    print(type(x))
    y = data['0be1dad']
    print(type(y))
    x.shape
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10,random_state=123)

    from sklearn.ensemble import RandomForestClassifier  
    svcclassifier =RandomForestClassifier(n_estimators= 10, criterion="entropy") 
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    
    from mlxtend.plotting import plot_confusion_matrix
    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
     
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    # ACCURACY CONTAINER
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#282A3A',fg='white',font=("boulder",14))
    label4.place(x=420,y=250)
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as RF_wt1.joblib",width=45,height=3,bg='#282A3A',fg='#C69749',font=("boulder",14))
    label5.place(x=420,y=470)
    from joblib import dump
    dump (svcclassifier,"RF_wt1.joblib")
    print("Model saved as RF_wt1.joblib")
    
   
# NB MODEL TRAINING TRAINING
def NB():
    data = pd.read_csv("obesity.csv")
    data.head()
    data = data.dropna()
    """Feature Selection => Manual"""
    x = data.drop(['0be1dad'], axis=1)
    data = data.dropna()
    print(type(x))
    y = data['0be1dad']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)

    from sklearn.naive_bayes import GaussianNB
    naive_bayes_classifier = GaussianNB()
    naive_bayes_classifier.fit(x_train, y_train)
    y_pred = naive_bayes_classifier.predict(x_test)
    print(y_pred)
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print("\n")
    
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig('Confusion Matrix.png', bbox_inches='tight')
    plt.show()
    print("=" * 40)
    print("==========")
    print("Classification Report : ", (classification_report(y_test, y_pred)))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    # ACCURACY CONTAINER
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#282A3A',fg='white',font=("boulder",14))
    label4.place(x=420,y=250)
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as NB_wt1.joblib",width=45,height=3,bg='#282A3A',fg='#C69749',font=("boulder",14))
    label5.place(x=420,y=470)
    from joblib import dump
    dump (naive_bayes_classifier,"NB_wt1.joblib")
    print("Model saved as NB_wt1.joblib")
    

# NEXT PAGE CONNECTIVITY
def window1():
    from subprocess import call
    call(['python','Next.py'])

# RESULT CONRAINER
framed = tk.LabelFrame(root, text="          \n          \n          RESULTS ",width=240, height=760, bd=0, font=('times', 18, ' bold '),bg="#708090",fg="white")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=0, y=102)

image_path = "logo1.png"  # Path to your image file
image = Image.open(image_path)
image = image.resize((85,70))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo,borderwidth=0)
image_label.grid(row=0, column=0)
image_label.place(x=30, y=16)

# SVM BUTTON
button3 = tk.Button(root,foreground="white", background="#FB2576", font=("ubuntu", 14, "bold"),bd=1, text="SVM", command=Model_Training, width=15, height=2)
button3.place(x=26, y=220)

# DT BUTTON
button4 = tk.Button(root, foreground="white", background="#FB2576", font=("ubuntu", 14, "bold"),bd=1,text="DT", command=DT, width=15, height=2)
button4.place(x=26, y=320)

# RF BUTTON
button5 = tk.Button(root, foreground="white", background="#FB2576", font=("ubuntu", 14, "bold"),text="RF", command=RF, width=15, height=2)
button5.place(x=26, y=420)

# NB BUTTON
exit = tk.Button(root, text="NB", command=NB, width=15, height=2, font=('ubuntu', 14, ' bold '),bg="#FB2576",fg="white")
exit.place(x=26, y=530)

# NEXT PAGE BUTTON
exit3 = tk.Button(root, text="Next", command=window1, width=15, height=2, font=('ubuntu', 14, ' bold '),bg="seagreen4",fg="white")
exit3.place(x=24, y=649)

root.mainloop()