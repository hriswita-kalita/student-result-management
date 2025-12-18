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