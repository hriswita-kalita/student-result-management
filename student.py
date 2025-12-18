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

