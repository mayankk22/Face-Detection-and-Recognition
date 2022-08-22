 #Id
        id_label=Label(personal_info_frame,text="Id No :",font=("times new roman",12,"bold"),bg="Slategray4")
        id_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(personal_info_frame,textvariable=self.var_id,width=19,font=("times new roman",13,"bold"))
        id_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

