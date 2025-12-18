from tkinter import *
from PIL import Image , ImageTk # pip install pillow

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x7480+80+170" )
        self.root.config(bg="white")
        self.root.focus_force()

       # Title
        title = Label(self.root, text = "Manage Course Details", font = ("goudy old style", 20, "bold"), bg = "#033054", fg = "white").place(x=10, y=15, relwidth=1180, height=35) 
        
       #Variables 
        self.var_courseName = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        
       # Widgets
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        self.txt_courseName = Entry(self.root, textvariable=self.var_courseName, font=("goudy old style", 15, "bold"), bg="white")
        self.txt_courseName.place(x=150, y=60, width=200)
        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="white").place(x=150, y=100, width=200)
        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"), bg="white").place(x=150, y=140, width=200)
        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="white")
        self.txt_description.place(x=150, y=180, width=500, height=100)

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()