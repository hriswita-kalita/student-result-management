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

# Search
Label(self.root,text="Search By | Roll No.",font=("goudy old style",20,"bold"),bg="white").place(x=300,y=100)
Entry(self.root,textvariable=self.var_search,font=("goudy old style",20),bg="lightyellow").place(x=540,y=100,width=160)
Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=720,y=100,width=100,height=35)
Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=840,y=100,width=100,height=35)

# Header Labels
headers=["Roll No","Name","Course","Marks Obtained","Total Marks","Percentage"]; self.data_labels=[]; x=150
for h in headers:
    Label(self.root,text=h,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=x,y=230,width=150,height=50)
    lbl=Label(self.root,text="",font=("goudy old style",15),bg="white",bd=2,relief=GROOVE); lbl.place(x=x,y=280,width=150,height=50)
    self.data_labels.append(lbl); x+=150

# Delete
Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=520,y=380,width=160,height=40)

