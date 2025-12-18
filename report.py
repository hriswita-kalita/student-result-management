from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x700+80+170")
        self.root.config(bg="white")
        self.root.focus_force()


