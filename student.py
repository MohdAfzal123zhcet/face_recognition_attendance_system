from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root=root.geometry("1530x790+0+0")
        root.title("Face recognition system")
        #==============variables=========================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        


         #img1

        img=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\2-AI-invades-automobile-industry-in-2019.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
  
        lbl=Label(root,image=self.photoimg)
        lbl.place(x=0,y=0,width=500,height=130)

          #img2
 
        img1=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\face-recognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl=Label(root,image=self.photoimg1)
        lbl.place(x=500,y=0,width=500,height=130)
 
         #img3
  
        img2=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl=Label(root,image=self.photoimg2)
        lbl.place(x=1000,y=0,width=500,height=130)




          #bg image
        img3=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\AdobeStock_303989091.jpeg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="#000080")
        title_lbl.place(x=0,y=130,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
  
         #Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

 
        img_left=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        lbl=Label(Left_frame,image=self.photoimg_left)
        lbl.place(x=5,y=0,width=720,height=130)

         #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

         #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         #courses
       
        course_label=Label(current_course_frame,text="course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select courses","COC4060","COE4510","COC4010","COC3500")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
 
        #year
        year_label=Label(current_course_frame,text="year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #semester
        semester_label=Label(current_course_frame,text="semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select semester","sem-1","sem-2","sem-3","sem-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


         #class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="class students information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=720,height=300)

        #STUDENT id

        studentid_label=Label(class_Student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)
   
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

           #STUDENT name

        studentname_label=Label(class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #class division

        class_div_label=Label(class_Student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

         #Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #gender
        gender_label=Label(class_Student_frame,text="gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

     

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #DOB

        dob_label=Label(class_Student_frame,text="dob",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #email
        email_label=Label(class_Student_frame,text="email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #phone no
        phone_label=Label(class_Student_frame,text="phone no",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_Student_frame,text="address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

          #teacher name
        teacher_label=Label(class_Student_frame,text="teacher name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

         #radio button1
        self.var_radio1=StringVar()

        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="no photo sample",value="no")
        radiobtn2.grid(row=6,column=1)

         #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        
        update_btn=Button(btn_frame,text="update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

         
        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

      
        take_photo_btn=Button(btn_frame1,text="Take photo sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

          
        update_photo_btn=Button(btn_frame1,text="reset",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)














        
         #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)

        img_right=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\gettyimages-1022573162.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        lbl=Label(Right_frame,image=self.photoimg_right)
        lbl.place(x=5,y=0,width=720,height=130)

          #---------------------------search system---------------------

        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="search by",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll no","phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(search_frame,text="search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        
        show_all_btn=Button(search_frame,text="show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)

         #=================table frame===================
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=690,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="studentid")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
        

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
          messagebox.showerror("error","all field are required")
        else:
          try:
            conn= mysql.connector.connect(host="localhost",username="root",password="mohdafzal@123",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","student details has been aded succesfully")
          except Exception as es:
            messagebox.showerror("error",f"Due To :{str(es)}")
    def fetch_data(self):
         conn= mysql.connector.connect(host="localhost",username="root",password="mohdafzal@123",database="face_recognition")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data) !=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
            self.student_table.insert("",END,values=i)
         conn.close()
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]

      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),
      self.va_std_id.set(data[4]),
      self.var_std_name.set(data[5]),
      self.var_div.set(data[6]),
      self.var_roll.set(data[7]),
      self.var_gender.set(data[8]),
      self.var_dob.set(data[9]),
      self.var_email.set(data[10]),
      self.var_phone.set(data[11]),
      self.var_address.set(data[12])
      self.var_teacher.set(data[13]),
      self.var_radio1.set(data[14])
    
    
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
          messagebox.showerror("error","all field are required")
        else:
          try:
              Update=messagebox.askyesno("Update","do you want to update this student details")
              if Update>0:
                 conn= mysql.connector.connect(host="localhost",username="root",password="mohdafzal@123",database="face_recognition")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,Dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.va_std_id.get()
                                                                                                                                                                                                                                                    ))
       
              else: 
                if not Update:
                 return
              messagebox.showinfo("success","student details successfully update completed") 
              conn.commit()
              self.fetch_data()
              conn.close()       
          except Exception as es:
           messagebox.showerror("Error",f"Due To:{str(es)}")




    def delete_data(self):
      if self.va_std_id.get()=="":
         messagebox.showerror("Error","student id must be required")
      else:
          try:
             delete=messagebox.askyesno("student delete page","do you want  to delete this student details")
             if delete>0:
                 conn= mysql.connector.connect(host="localhost",username="root",password="mohdafzal@123",database="face_recognition")
                 my_cursor=conn.cursor()
                 sql="delete from student where student_id=%s"
                 val=(self.va_std_id.get(),)
                 my_cursor.execute(sql,val)
             else:
                  if not delete:
                       return
             conn.commit()
             self.fetch_data()
             conn.close()   
             messagebox.showinfo("delete","successfully deleted student details")
          except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}")


    def reset_data(self):
      self.var_dep.set("select department"),
      self.var_course.set("select course"),
      self.var_year.set("select year"),
      self.var_semester.set("select semester"),
      self.va_std_id.set(""),
      self.var_std_name.set(""),
      self.var_div.set("select division"),
      self.var_roll.set(""),
      self.var_gender.set("male"),
      self.var_dob.set(""),
      self.var_email.set(""),
      self.var_phone.set(""),
      self.var_address.set("")
      self.var_teacher.set(""),
      self.var_radio1.set("")


#=====================generate data set or take photo sample===================================
    def generate_dataset(self):
       if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
          messagebox.showerror("error","all field are required")
       else:
           try:
              conn= mysql.connector.connect(host="localhost",username="root",password="mohdafzal@123",database="face_recognition")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from student")
              myresult=my_cursor.fetchall()
              id=0
              for x in myresult:
                id+=1
              my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,Dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.va_std_id.get()
                                                                                                                                                                                                                                                    ))
       
              conn.commit()
              self.fetch_data()
              self.reset_data()
              conn.close()

              face_classifier=cv2.CascadeClassifier(r"C:\Users\Mohd Afzal\Desktop\face recognition system\haarcascade_frontalface_default.xml")

              def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                for (x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w]
                  return face_cropped
              cap=cv2.VideoCapture(0)
              img_id=0
              while TRUE:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                   img_id+=1
                   face=cv2.resize(face_cropped(my_frame),(450,450))
                   face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                   file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                   cv2.imwrite(file_name_path,face)
                   cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                   cv2.imshow("Cropped face",face)


                if cv2.waitKey(1)==13 or int(img_id)==100:
                  break
              cap.release()
              cv2.destroyAllWindows()
              messagebox.showinfo("result","generating data set completed!!!")
           except Exception as es:
               messagebox.showerror("Error",f"Due To:{str(es)}")



                   





















                                                                                                   
       



        



if __name__ == "__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()