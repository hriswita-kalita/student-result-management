from tkinter import *
from tkinter import messagebox
import sqlite3

class ReportClass:
    def __init__(self, root):
        self.root=root; self.root.title("Result Management System"); self.root.geometry("1200x650+80+80"); self.root.config(bg="white")

