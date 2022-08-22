from multiprocessing.dummy import Process
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD 
from PIL import Image,ImageTk
import os
from particular import particulars
from face_detection import Face_Detection
from process import Process_data
from user_records import User_Record
from developer import Developer

class face_recog_sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")

        # Background Image
        img1=Image.open(r"Images\bg9.jpeg")
        img1=img1.resize((1300,700))
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.photoimg1)
        bg_img1.place(x=0,y=0,width=1300,height=700) 

        img2=Image.open(r"Images\bg.jpeg")
        img2=img2.resize((400,400))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img2=Label(self.root,image=self.photoimg2)
        bg_img2.place(x=420,y=120,width=400,height=400)
        

        # User Data Button
        img3 = Image.open(r"Images\user_details.jpeg")
        img3 = img3.resize((200,200))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1=Button(bg_img1,image=self.photoimg3,command=self.user_details,borderwidth=0,cursor="hand2")
        b1.place(x=70,y=35,width=170,height=170)

        b1_1=Button(bg_img1,text="USER'S PARTICULARS",command=self.user_details,cursor="hand2",font=("times new roman",7,"bold"),bg="white",fg="black")
        b1_1.place(x=140,y=200,width=130,height=20)


        # Face Detector Button
        img4 = Image.open(r"Images\face_detector.jpeg")
        img4 = img4.resize((190,190))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2=Button(bg_img1,image=self.photoimg4,borderwidth=0,cursor="hand2",command=self.face_data)
        b2.place(x=200,y=250,width=150,height=150)

        b2_1=Button(bg_img1,text="FACE AUTHENTICATION",cursor="hand2",command=self.face_data,font=("times new roman",7,"bold"),bg="white",fg="black")
        b2_1.place(x=190,y=400,width=140,height=20)


        # Process Data Button
        img5 = Image.open(r"Images\train_data.jpeg")
        img5 = img5.resize((150,150))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3=Button(bg_img1,image=self.photoimg5,borderwidth=0,cursor="hand2",command=self.process_data)
        b3.place(x=300,y=460,width=100,height=85)

        b3_1=Button(bg_img1,text="PROCESS DATA",cursor="hand2",command=self.process_data,font=("times new roman",7,"bold"),bg="white",fg="black")
        b3_1.place(x=290,y=550,width=120,height=20)


        # Developer Button
        img6 = Image.open(r"Images\developer.jpeg")
        img6 = img6.resize((150,150))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b4=Button(bg_img1,image=self.photoimg6,borderwidth=0,cursor="hand2",command=self.developer_bttn)
        b4.place(x=500,y=530,width=100,height=90)

        b4_1=Button(bg_img1,text="DEVELOPER",cursor="hand2",command=self.developer_bttn,font=("times new roman",7,"bold"),bg="white",fg="black")
        b4_1.place(x=490,y=625,width=125,height=20)


        # Exit Button
        img7 = Image.open(r"Images\exit.jpeg")
        img7 = img7.resize((150,150))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5=Button(bg_img1,image=self.photoimg7,borderwidth=0,cursor="hand2")
        b5.place(x=710,y=530,width=110,height=100)

        b5_1=Button(bg_img1,text="YOUR WAY OUT",cursor="hand2",font=("times new roman",7,"bold"),bg="white",fg="black")
        b5_1.place(x=700,y=625,width=125,height=20)


         # Help Desk Button
        img8 = Image.open(r"Images\help_desk.jpeg")
        img8 = img8.resize((170,130))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6=Button(bg_img1,image=self.photoimg8,borderwidth=0,cursor="hand2")
        b6.place(x=880,y=445,width=170,height=115)

        b6_1=Button(bg_img1,text="TROUBLESHOOTING",cursor="hand2",font=("times new roman",7,"bold"),bg="white",fg="black")
        b6_1.place(x=900,y=555,width=120,height=20)


         # Photos Button
        img9 = Image.open(r"Images\photos.jpeg")
        img9 = img9.resize((160,180))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b7=Button(bg_img1,image=self.photoimg9,borderwidth=0,cursor="hand2",command=self.open_img)
        b7.place(x=960,y=250,width=150,height=150)

        b7_1=Button(bg_img1,text="USER'S IMAGES",cursor="hand2",command=self.open_img,font=("times new roman",8,"bold"),bg="white",fg="black")
        b7_1.place(x=960,y=380,width=130,height=20)


        # Records Button
        img10 = Image.open(r"Images\records.jpg")
        img10 = img10.resize((210,250))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b8=Button(bg_img1,image=self.photoimg10,borderwidth=0,cursor="hand2",command=self.user_data_record)
        b8.place(x=1000,y=40,width=190,height=190)

        b8_1=Button(bg_img1,text="USER'S RECORDS",cursor="hand2",command=self.user_data_record,font=("times new roman",8,"bold"),bg="white",fg="black")
        b8_1.place(x=1040,y=200,width=120,height=20)


    def open_img(self):
        os.startfile("data")

    #Function Buttons

    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=particulars(self.new_window)

    def process_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Process_data(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Detection(self.new_window) 

    def user_data_record(self):
        self.new_window=Toplevel(self.root)
        self.app=User_Record(self.new_window) 

    def developer_bttn(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)           








if __name__ == "__main__":
    root=Tk()
    obj=face_recog_sys(root)
    root.mainloop()       