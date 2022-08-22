from cgitb import text
from logging import exception
from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np


class Face_Detection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")


        # Background Image
        img1=Image.open(r"Images\fdb1.jpeg")
        img1=img1.resize((900,660))
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.photoimg1)
        bg_img1.place(x=-50,y=0,width=700,height=660)

        img2=Image.open(r"Images\fdb2.jpeg")
        img2=img2.resize((800,660))
        self.photoimg2=ImageTk.PhotoImage(img2)
        bg_img2=Label(self.root,image=self.photoimg2)
        bg_img2.place(x=650,y=0,width=700,height=660)

        bttn_2=Button(bg_img2,text="DETECT FACE",cursor="hand2",command=self.face_detect,font=("times new roman",24,"bold"),bg="black",fg="light sky blue")
        bttn_2.place(x=120,y=600,width=450,height=40)

    #User Records
    def records(self,j,k,l,m):
        with open("record_file.csv","r+",newline="\n") as f:
            userDataList=f.readlines()
            user_list=[]
            for line in userDataList:
                feed=line.split((","))
                user_list.append(feed[0])

            if((j not in user_list) and (k not in user_list) and (l not in user_list) and (m not in user_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                date_string=now.strftime("%H:%M:%S")
                f.writelines(f"\n{j},{k},{l},{m},{date_string},{d1}")





             


    #Face
    def face_detect(self):
        def face_square(img,classifier,scaleFactor,minNeighbor,color,text,clf):  #To draw boundary against the image
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Gray scale conversion
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

            coordinate=[]  #Square coordinates are initialized to 0

            for(x,y,w,h) in features: #w=width h=height
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)  #0,255,0=green color  thickness=3
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #To predict the gray scale image
                result=int((100*(1-predict/300)))  #Confidence Formula according to the Algo

                conn=mysql.connector.connect(host="localhost",username="root",password="Mayank@22",database="face_recognition")
                my_cursor=conn.cursor()  #To access data from database
                my_cursor.execute("select `ID No` from user_data where `ID No`="+str(id))
                j=my_cursor.fetchone()
                j="+".join(j)

                my_cursor.execute("select `Name` from user_data where `ID No`="+str(id))
                k=my_cursor.fetchone()
                k="+".join(k)

                my_cursor.execute("select `Gender` from user_data where `ID No`="+str(id))
                l=my_cursor.fetchone()
                l="+".join(l)

                my_cursor.execute("select `Position` from user_data where `ID No`="+str(id))
                m=my_cursor.fetchone()
                m="+".join(m)



                if result>78:  #To show the above data
                   cv2.putText(img,f"ID No:{j}",(x,y-145),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                   cv2.putText(img,f"Name:{k}",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                   cv2.putText(img,f"Gender:{l}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                   cv2.putText(img,f"Position:{m}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                   self.records(j,k,l,m)

                else:
                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                  cv2.putText(img,"No Match Found",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)

                coordinate=[x,y,w,h]

            return coordinate 

        def  detect(img,clf,cascade): 
             coordinate=face_square(img,cascade,1.1,10,(255,25,255),"Face",clf)
             return img

        cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("DataProcess.xml")   

        video_capt=cv2.VideoCapture(0)  #0=To acces laptop camera and to access other camera we pass 1

        while True:
            ret,img=video_capt.read()
            img=detect(img,clf,cascade)
            cv2.imshow("Face Detection",img)

            if cv2.waitKey(1)==13:
                break
        video_capt.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Detection(root)
    root.mainloop()          