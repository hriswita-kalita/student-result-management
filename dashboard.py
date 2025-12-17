from tkinter import *
from PIL import Image , ImageTk # pip install pillow

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0" )
        self.root.config(bg="white")
 
        # Icons 
        self.logo_dash = ImageTk.PhotoImage(file = "images/logo_p.png")

        # Title
        title = Label(self.root, text = "Student Result Management System", padx = 10, compound = LEFT, image = self.logo_dash, font = ("goudy old style", 20, "bold"), bg = "#033054", fg = "white").place(x=0, y=0, relwidth=1, height=50)

        # Menu
        M_Frame = LabelFrame(self.root, text = "Menu", font = ("times new roman", 15), bg = "white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        btn_course = Button(M_Frame, text = "Course", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x=20, y=5, width = 200, height = 40) 
        btn_student = Button(M_Frame, text = "Student", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x=240, y=5, width = 200, height = 40)
        btn_result = Button(M_Frame, text = "Result", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x=460, y=5, width = 200, height = 40)
        btn_view = Button(M_Frame, text = "View Student Result", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x=680, y=5, width = 200, height = 40)
        btn_logout = Button(M_Frame, text = "Logout", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x=900, y=5, width = 200, height = 40)
        btn_exit = Button(M_Frame, text = "Exit", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x=1120, y=5, width = 200, height = 40)   

        # Footer
        footer = Label(self.root, text = "SRMS -Student Result Management System\nContact Us for any Technical Issues: 987xxxx01 ", font = ("goudy old style", 12), bg = "#026262", fg = "white").pack(side = BOTTOM, fill = X)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root);
    root.mainloop()
