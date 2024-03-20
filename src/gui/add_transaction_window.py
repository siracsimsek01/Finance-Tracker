import tkinter as tk
from tkinter import ttk


class add_transaction(tk.Tk):
    def __init__(self, income, expenses):
        super().__init__()
        self.income = income
        self.expenses = expenses
        
        # Set window properties
        self.title('Add Transaction - PyFinance (Personal Finance Tracker)')
        self.geometry('800x600') 
        self.configure(bg='#0F102B')
        
        
        
        