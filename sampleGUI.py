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
warnings.filterwarnings("ignore", category=DeprecationWarning) 
root = tk.Tk()
root.title("Comparison of Clustering Methods for Obesity Classification")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image = Image.open('img5.jpg')

image = image.resize((w, h))

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

image = Image.open('a5.png')

image = image.resize((1600,900))

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=30, y=80)








#header
# , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Obesity Detection Using Machine Learning Techniques", font=('times', 35,' bold '), height=2, width=60,bg='gray12',fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
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
    
    #after click on svm butttom 
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='gray46',fg='white',font=("boulder",14))
    label4.place(x=420,y=250)
    
    label5 = tk.Label(root,text ="Accuracy :"+str(ACC)+"%\nModel saved as SVM_wt1.joblib",width=43,height=2,bg='mediumseagreen',fg='white',font=("boulder",14))
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


def Dmodel_Training():
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


 
    
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as DT_wt1.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    from joblib import dump
    dump (svcclassifier,"DT_wt1.joblib")
    print("Model saved as DT_wt1.joblib")

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
    
    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as RF_wt1.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    from joblib import dump
    dump (svcclassifier,"RF_wt1.joblib")
    print("Model saved as RF_wt1.joblib")
    
   


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

    label4 = tk.Label(root,text =str(repo),width=45,height=15,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=410,y=250)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as NB_wt1.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=410,y=470)
    from joblib import dump
    dump (naive_bayes_classifier,"NB_wt1.joblib")
    print("Model saved as NB_wt1.joblib")
    


def window1():
    from subprocess import call
    call(['python','Next.py'])

#result box text=" RESULT "
framed = tk.LabelFrame(root, text="          \n          RESULTS ",width=240, height=760, bd=0, font=('times', 18, ' bold '),bg="slategray4",fg="white")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=0, y=112)


button3 = tk.Button(root,foreground="white", background="indianred", font=("times", 14, "bold"),text="SVM", command=Model_Training, width=15, height=2)
button3.place(x=26, y=230)

button4 = tk.Button(root, foreground="white", background="indianred", font=("times", 14, "bold"),text="DT", command=Dmodel_Training, width=15, height=2)
button4.place(x=26, y=330)

button5 = tk.Button(root, foreground="white", background="indianred", font=("times", 14, "bold"),text="RF", command=RF, width=15, height=2)
button5.place(x=26, y=430)

button6 = tk.Button(root, text="NB", command=NB, width=15, height=2, font=('times', 14, ' bold '),bg="indianred",fg="white")
button6.place(x=26, y=530)


exit3 = tk.Button(root, text="Next", command=window1, width=15, height=2, font=('times', 14, ' bold '),bg="seagreen4",fg="white")
exit3.place(x=24, y=649)



root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''