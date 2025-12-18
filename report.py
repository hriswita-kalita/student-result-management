from tkinter import *
from tkinter import messagebox
import sqlite3

class ReportClass:
    def __init__(self, root):
        self.root=root; self.root.title("Result Management System"); self.root.geometry("1200x650+80+80"); self.root.config(bg="white")

# Title
Label(self.root,text="View Student Results",font=("goudy old style",30,"bold"),bg="#f7a400",fg="black").place(x=0,y=0,relwidth=1,height=70)

# Variables
self.var_search=StringVar()

