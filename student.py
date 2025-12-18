from tkinter import *
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
        Label(
            self.root,
            text="Manage Course Details",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=10, y=15, relwidth=1180, height=35)

        # Variables
        self.var_roll = StringVar()
        self.var_courseName = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        # Labels
        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        Label(self.root, text="E-mail", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        # Entry Fields 
        self.txt_roll = Entry(self.root, textvariable=self.var_courseName,
                                    font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        Entry(self.root, textvariable=self.var_name,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)

        Entry(self.root, textvariable=self.var_email,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)

        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=220, width=500, height=100)

        # Buttons 
        Button(self.root, text="Save", font=("goudy old style", 15, "bold"),
               bg="#2196f3", fg="white", cursor="hand2", command=self.add)\
            .place(x=150, y=400, width=110, height=40)

        Button(self.root, text="Update", font=("goudy old style", 15, "bold"),
               bg="#4caf50", fg="white", cursor="hand2", command=self.update)\
            .place(x=270, y=400, width=110, height=40)

        Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),
               bg="#f44336", fg="white", cursor="hand2", command=self.delete)\
            .place(x=390, y=400, width=110, height=40)

        Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),
               bg="#607d8b", fg="white", cursor="hand2", command=self.clear)\
            .place(x=510, y=400, width=110, height=40)

        # Search Panel 
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"),
              bg="white").place(x=720, y=60)

        Entry(self.root, textvariable=self.var_search,
              font=("goudy old style", 15, "bold"), bg="lightyellow")\
            .place(x=870, y=60, width=180)

        Button(self.root, text="Search", font=("goudy old style", 15, "bold"),
               bg="#03a9f4", fg="white", cursor="hand2", command=self.search)\
            .place(x=1070, y=60, width=120, height=28)

        # Content Frame
        self.course_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.course_Frame.place(x=720, y=100, width=470, height=340)

        scrollx = Scrollbar(self.course_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.course_Frame, orient=VERTICAL)

        self.CourseTable = ttk.Treeview(
            self.course_Frame,
            columns=("cid", "name", "duration", "charges", "description"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        self.CourseTable["show"] = "headings"
        self.CourseTable.column("cid", width=50)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=150)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.create_table()
        self.show_all()

    # Database
    def create_table(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course(
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)
        con.commit()
        con.close()

    # Functions
    def clear(self):
        self.show_all()
        self.var_roll.set("")
        self.var_courseName.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)

    def get_data(self, ev):
        row = self.CourseTable.item(self.CourseTable.focus())["values"]
        if row:
            self.var_roll.set(row[0])
            self.var_courseName.set(row[1])
            self.var_duration.set(row[2])
            self.var_charges.set(row[3])
            self.txt_description.delete("1.0", END)
            self.txt_description.insert(END, row[4])
            self.txt_roll.config(state="readonly")

    def add(self):
        if self.var_courseName.get() == "":
            messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            return
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO course(name,duration,charges,description) VALUES(?,?,?,?)",
                (
                    self.var_courseName.get(),
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0", END)
                )
            )
            con.commit()
            messagebox.showinfo("Success", "Course added successfully", parent=self.root)
            self.show_all()
            self.clear()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Course Name already present", parent=self.root)
        con.close()

    def update(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Select course from list", parent=self.root)
            return
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute(
            "UPDATE course SET duration=?, charges=?, description=? WHERE cid=?",
            (
                self.var_duration.get(),
                self.var_charges.get(),
                self.txt_description.get("1.0", END),
                self.var_roll.get()
            )
        )
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
        self.show_all()

    def delete(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Select course from list", parent=self.root)
            return
        if not messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root):
            return
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("DELETE FROM course WHERE cid=?", (self.var_roll.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
        self.clear()

    def show_all(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM course")
        rows = cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert("", END, values=row)
        con.close()

    def search(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM course WHERE name LIKE ?",
            ('%' + self.var_search.get() + '%',)
        )
        rows = cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert("", END, values=row)
        con.close()


if __name__ == "__main__":
    root = Tk()
    studentClass(root)
    root.mainloop()
