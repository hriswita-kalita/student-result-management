from tkinter import 
from tkinter import ttk, messagebox 
import sqlite3

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x7480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, relwidth=1180, height=35)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_admission = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        # Labels
        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)

        Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=400, y=60)
        Label(self.root, text="Contact No.", font=("goudy old style", 15, "bold"), bg="white").place(x=400, y=100)
        Label(self.root, text="Select Course", font=("goudy old style", 15, "bold"), bg="white").place(x=400, y=140)
        Label(self.root, text="Admission Date", font=("goudy old style", 15, "bold"), bg="white").place(x=400, y=180)

        Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=350)
        Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=240, y=350)
        Label(self.root, text="Pin Code", font=("goudy old style", 15, "bold"), bg="white").place(x=470, y=350)

        # Entry Fields
        Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=60, width=200)
        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=100, width=200)
        Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=140, width=200)

        self.cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), state="readonly")
        self.cmb_gender.place(x=150, y=180, width=200)
        self.cmb_gender.current(0)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=220, width=500, height=100)

        Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(x=550, y=60, width=200)
        Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=550, y=100, width=200)

        self.cmb_course = ttk.Combobox(self.root, textvariable=self.var_course, state="readonly")
        self.cmb_course.place(x=550, y=140, width=200)

        Entry(self.root, textvariable=self.var_admission, font=("goudy old style", 15), bg="lightyellow").place(x=550, y=180, width=200)

        Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="lightyellow").place(x=80, y=350, width=140)
        Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15), bg="lightyellow").place(x=300, y=350, width=140)
        Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg="lightyellow").place(x=560, y=350, width=140)

        # Buttons
        Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white",
               command=self.add).place(x=150, y=400, width=110, height=40)

        Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",
               command=self.update).place(x=270, y=400, width=110, height=40)

        Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",
               command=self.delete).place(x=390, y=400, width=110, height=40)

        Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
               command=self.clear).place(x=510, y=400, width=110, height=40)
        
        # Search 
        Label(self.root, text="Search Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg="lightyellow").place(x=900, y=60, width=180)
        Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
               command=self.search).place(x=1090, y=60, width=100, height=28)
