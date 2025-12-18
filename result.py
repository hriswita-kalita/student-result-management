from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x700+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        Label(self.root, text="Add Student Result", font=("goudy old style", 20, "bold"),
              bg="#ff9800").place(x=10, y=15, relwidth=1180, height=35)
        

        # Variables
        self.var_student = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()

        # Labels
        Label(self.root, text="Select Student", font=("goudy old style", 15), bg="white").place(x=50, y=80)
        Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=130)
        Label(self.root, text="Course", font=("goudy old style", 15), bg="white").place(x=50, y=180)
        Label(self.root, text="Marks Obtained", font=("goudy old style", 15), bg="white").place(x=50, y=230)
        Label(self.root, text="Full Marks", font=("goudy old style", 15), bg="white").place(x=50, y=280)

        # Entry Fields
        self.cmb_student = ttk.Combobox(self.root, textvariable=self.var_student, state="readonly")
        self.cmb_student.place(x=220, y=80, width=200)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),
              bg="lightyellow").place(x=220, y=130, width=200)
        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15),
              bg="lightyellow").place(x=220, y=180, width=200)
        Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 15),
              bg="lightyellow").place(x=220, y=230, width=200)
        Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 15),
              bg="lightyellow").place(x=220, y=280, width=200)
        
        # Buttons
        Button(self.root, text="Submit", font=("goudy old style", 15),
               bg="#4caf50", command=self.add).place(x=220, y=340, width=100, height=35)
        Button(self.root, text="Clear", font=("goudy old style", 15),
               bg="#9e9e9e", command=self.clear).place(x=340, y=340, width=100, height=35)
        
        # Image
        self.bg_img = Image.open("images/result.png")
        self.bg_img = self.bg_img.resize((450, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        Label(self.root, image=self.bg_img, bg="white").place(x=600, y=90)

        #=================================================================================================

    def add(self):
        pass

    def clear(self):
        self.var_student.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

if __name__ == "__main__":
    root = Tk()
    ResultClass(root)
    root.mainloop()
