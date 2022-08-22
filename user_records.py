from cgitb import text
from logging import exception
from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os.path
import glob
import os
import csv
from tkinter import filedialog

userData=[]
class User_Record:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")

        #Text Variables
        self.var_record_id=StringVar()
        self.var_record_name=StringVar()
        self.var_record_gender=StringVar()
        self.var_record_posn=StringVar()
        self.var_record_time=StringVar()
        self.var_record_date=StringVar()


        # Background Image
        img1=Image.open(r"Images\bg9.jpeg")
        img1=img1.resize((1300,700))
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.photoimg1)
        bg_img1.place(x=0,y=0,width=1300,height=700) 

        # Left Label Frame
        Left_Frame=LabelFrame(bg_img1,bd=2,bg="Slategray4",relief=RIDGE,text="USER INFORMATION",font=("times new roman",12,"bold"),fg="white")
        Left_Frame.place(x=20,y=120,width=630,height=520)

        # SubLeft Label Frame
        sub_left_frame=LabelFrame(Left_Frame,bd=2,highlightbackground="black",bg="Slategray4")
        sub_left_frame.place(x=5,y=20,width=615,height=200)

        #User Id
        id_label=Label(sub_left_frame,text="ID No :",font=("times new roman",12,"bold"),bg="Slategray4")
        id_label.grid(row=0,column=0,padx=15,pady=15,sticky=W)

        id_entry=ttk.Entry(sub_left_frame,textvariable=self.var_record_id,font=("times new roman",13,"bold"))
        id_entry.grid(row=0,column=1,padx=15,pady=15,sticky=W)

        #Name
        name_label=Label(sub_left_frame,text="Name :",font=("times new roman",12,"bold"),bg="Slategray4")
        name_label.grid(row=0,column=2,padx=15,pady=15,sticky=W)

        name_entry=ttk.Entry(sub_left_frame,textvariable=self.var_record_name,width=19,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=3,padx=15,pady=15,sticky=W)

        #Gender
        gender_label=Label(sub_left_frame,text="Gender :",font=("times new roman",12,"bold"),bg="Slategray4")
        gender_label.grid(row=1,column=0,padx=15,pady=15,sticky=W)

        gender_entry=ttk.Entry(sub_left_frame,textvariable=self.var_record_gender,width=19,font=("times new roman",13,"bold"))
        gender_entry.grid(row=1,column=1,padx=15,pady=15,sticky=W)

        #Position
        posn_label=Label(sub_left_frame,text="Position :",font=("times new roman",12,"bold"),bg="Slategray4")
        posn_label.grid(row=1,column=2,padx=15,pady=15,sticky=W)

        posn_entry=ttk.Entry(sub_left_frame,textvariable=self.var_record_posn,width=19,font=("times new roman",13,"bold"))
        posn_entry.grid(row=1,column=3,padx=15,pady=15,sticky=W)

        #Time
        time_label=Label(sub_left_frame,text="Time :",font=("times new roman",12,"bold"),bg="Slategray4")
        time_label.grid(row=2,column=0,padx=15,pady=15,sticky=W)

        time_entry=ttk.Entry(sub_left_frame,textvariable=self.var_record_time,width=19,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=15,pady=15,sticky=W)

        #Date
        date_label=Label(sub_left_frame,text="Date :",font=("times new roman",12,"bold"),bg="Slategray4")
        date_label.grid(row=2,column=2,padx=15,pady=15,sticky=W)

        date_entry=ttk.Entry(sub_left_frame,textvariable=self.var_record_date,width=19,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=15,pady=15,sticky=W)

        #Button Frame
        btn_frame1=LabelFrame(Left_Frame,bd=2,highlightbackground="black",bg="Slategray4",relief=RIDGE,)
        btn_frame1.place(x=5,y=300,width=605,height=34)

        import_btn=Button(btn_frame1,text="Import Data File",cursor="hand2",command=self.ImportData,width="14",font=("times new roman",13,"bold"),bg="black",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame1,text="Export Data File",cursor="hand2",command=self.ExportData,width="14",font=("times new roman",13,"bold"),bg="black",fg="white")
        export_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame1,text="Update",cursor="hand2",width="14",font=("times new roman",13,"bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame1,text="Reset",cursor="hand2",command=self.reset_userdata,width="14",font=("times new roman",13,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=3)


        # Right Label Frame
        Right_Frame=LabelFrame(bg_img1,bd=2,bg="Slategray4",relief=RIDGE,text="DETAILS",font=("times new roman",12,"bold"),fg="white")
        Right_Frame.place(x=670,y=120,width=590,height=520)

        #Table Frame
        table_frame=Frame(Right_Frame,bd=2,highlightbackground="black",bg="Slategray4",relief=RIDGE)
        table_frame.place(x=5,y=20,width=575,height=470)

        #Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.UserDataTable=ttk.Treeview(table_frame,column=("ID No","Name","Gender","Position","Time","Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.UserDataTable.xview)
        scroll_y.config(command=self.UserDataTable.yview)

        self.UserDataTable.heading("ID No",text="ID No")
        self.UserDataTable.heading("Name",text="Name")
        self.UserDataTable.heading("Gender",text="Gender")
        self.UserDataTable.heading("Position",text="Position")
        self.UserDataTable.heading("Time",text="Time")
        self.UserDataTable.heading("Date",text="Date")
        self.UserDataTable["show"]="headings"

        self.UserDataTable.column("ID No",width=115)
        self.UserDataTable.column("Name",width=115)
        self.UserDataTable.column("Gender",width=115)
        self.UserDataTable.column("Position",width=115)
        self.UserDataTable.column("Time",width=115)
        self.UserDataTable.column("Date",width=115)

        self.UserDataTable.pack(fill=BOTH,expand=1)
        self.UserDataTable.bind("<ButtonRelease>",self.take_cursor)

    #Import Data
    def getData(self,rows):
        self.UserDataTable.delete(*self.UserDataTable.get_children())
        for i in rows:
            self.UserDataTable.insert("",END,values=i)


    def ImportData(self):
        global userData
        userData.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="User Records",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as userfile:
            readfile=csv.reader(userfile,delimiter=",")
            for i in readfile:
                userData.append(i)
            self.getData(userData)    

    #Export Data
    def ExportData(self):
        try:
            if len(userData)<1:
                messagebox.showerror("Data Not Found","No Data Available to Save",parent=self.root)
                return False
            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="User Records",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)    
            with open(file_name,mode="w",newline="") as userfile:
                export_write=csv.writer(userfile,delimiter=",")
                for i in userData:
                    export_write.writerow(i)
                messagebox.showinfo("Data Saved","Data Successfully Saved to"+os.path.basename(file_name))
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 


    def take_cursor(self,event=""):
        cursor_row=self.UserDataTable.focus()
        res=self.UserDataTable.item(cursor_row)
        table_rows=res['values']
        self.var_record_id.set(table_rows[0])
        self.var_record_name.set(table_rows[1])
        self.var_record_gender.set(table_rows[2])
        self.var_record_posn.set(table_rows[3])
        self.var_record_time.set(table_rows[4])
        self.var_record_date.set(table_rows[5])


    def reset_userdata(self):
        self.var_record_id.set("")
        self.var_record_name.set("")
        self.var_record_gender.set("")
        self.var_record_posn.set("")
        self.var_record_time.set("")
        self.var_record_date.set("")


            




        


if __name__ == "__main__":
    root=Tk()
    obj=User_Record(root)
    root.mainloop() 