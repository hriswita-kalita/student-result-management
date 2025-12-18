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

# Database
def create_table(self):
    con=sqlite3.connect("rms.db"); cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS result(
        roll TEXT,name TEXT,course TEXT,marks INTEGER,total INTEGER,percentage REAL)""")
    con.commit(); con.close()

# Search Logic
def search(self):
    con=sqlite3.connect("rms.db"); cur=con.cursor()
    cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
    row=cur.fetchone(); con.close()
    [self.data_labels[i].config(text=row[i]) for i in range(6)] if row else messagebox.showerror("Error","No record found",parent=self.root)

# Clear
def clear(self): self.var_search.set(""); [lbl.config(text="") for lbl in self.data_labels]

def delete(self):
    if self.var_search.get()=="": return messagebox.showerror("Error","Enter Roll No",parent=self.root)
    con=sqlite3.connect("rms.db"); cur=con.cursor()
    cur.execute("DELETE FROM result WHERE roll=?", (self.var_search.get(),))
    con.commit(); con.close(); messagebox.showinfo("Success","Record deleted",parent=self.root); self.clear()

