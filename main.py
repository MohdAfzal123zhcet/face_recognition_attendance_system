from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root=root.geometry("1530x790+0+0")
        root.title("Face recognition system")
        
        #img1

        img=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\2-AI-invades-automobile-industry-in-2019.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl=Label(root,image=self.photoimg)
        lbl.place(x=0,y=0,width=500,height=130)

        #img2

        img1=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\gettyimages-1022573162.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl=Label(root,image=self.photoimg1)
        lbl.place(x=500,y=0,width=500,height=130)

        #img3

        img2=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\IMG_1183_augmented_reality_faces1.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl=Label(root,image=self.photoimg2)
        lbl.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\di.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        lbl=Label(text="Face Recognition Attendence System",font=("times new roman",35,"bold"),bg="white",fg="#000080")
        lbl.place(x=0,y=130,width=1530,height=45)

         #student button

        img4=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face button

        
        img5=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=500,y=300,width=220,height=40)

        
        #Attendence  button

        
        img6=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\unnamed.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=800,y=300,width=220,height=40)

         #help desk

        
        img7=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=1100,y=300,width=220,height=40)

         #train button

        
        img8=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=200,y=580,width=220,height=40)

        
         #photos button

        
        img9=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\teaser.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=500,y=580,width=220,height=40)

        
         #developer  button

        
        img10=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=800,y=580,width=220,height=40)

        
         #exit button

        
        img11=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="#000080")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")


    
       #=========================#FUNCTIONS BUTTON===================================================================
    def student_details(self):
        self.new_window=Toplevel()
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel()
        self.app=Train(self.new_window)
    

    def face_data(self):
        self.new_window=Toplevel()
        self.app=Face_Recognition(self.new_window)

        













        
    


 


if __name__ == "__main__":
   root=Tk()
   obj=Face_Recognition_System(root)
   root.mainloop()