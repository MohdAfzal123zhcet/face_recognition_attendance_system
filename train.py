from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root=root.geometry("1530x790+0+0")
        root.title("Face recognition system")



        title_lbl=Label(text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="#000080")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        img_top=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        lbl=Label(image=self.photoimg_top)
        lbl.place(x=0,y=55,width=1530,height=325)

        #button

        
        b1_1=Button(text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="BLACK",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)


                
        img_bottom=Image.open(r"D:\Users\Mohd Afzal\Desktop\face recognition system\college_images\face-recognition.png")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        lbl=Label(image=self.photoimg_bottom)
        lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #convert in gray sacle
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])



            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the clasifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed")








if __name__ == "__main__":
   root=Tk()
   obj=Train(root)
   root.mainloop()