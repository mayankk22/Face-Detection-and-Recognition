from cgitb import text
from logging import exception
from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np


class Process_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")


        # Background Image
        img1=Image.open(r"Images\pbg.jpg")
        img1=img1.resize((1300,660))
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.photoimg1)
        bg_img1.place(x=0,y=0,width=1300,height=660)

        #Process_data Button
        b_bttn=Button(self.root,text="PROCESS THE DATA",command=self.process_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="black",fg="light sky blue")
        b_bttn.place(x=450,y=320,width=500,height=45)


    def process_classifier(self):
        data_dir=("data")    #data path stored in a variable
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]    #faces and ids are intialized to empty list according to algorithm
        ids=[]

        for image in path:  #accessing all the images which are stored in path
            img=Image.open(image).convert('L')   #Conversion to Gray Scale
            imageNp=np.array(img,'uint8')  #To convert the image into GRID format using numpy and stored it in a variable
            id=int(os.path.split(image)[1].split('.')[1])  #To get the integer id

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Processing",imageNp)
            cv2.waitKey(1)==13     #Window closes after pressing enter
        ids=np.array(ids) 

        #Processing Classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("DataProcess.xml")   #To save the data in a file
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Data Processing Completed")










if __name__ == "__main__":
    root=Tk()
    obj=Process_data(root)
    root.mainloop()        