import tkinter as tk
from tkinter import Label, Frame, messagebox, PhotoImage
from .add_transaction_window import AddTransactionWindow
from .login_window import LoginWindow
from .dashboard_window import Dashboard
from utils.styles import *
import json
import os
import numpy as np






class MainWindow(tk.Tk):
    def __init__(self, user_name=""):
        super().__init__()
        self.title("PyFinance - Personal Finance Tracker")
        self.geometry("700x400")
        self.configure(bg="#0F102B")
        self.balance = 0
        self.resizable(False, False)  
  

        # Set user name and greeting
        
        self.left_frame = Frame(self, bg=COLOR_BG, width=300, height=600)
        self.left_frame.pack(side="left", fill="both", expand=False)
        
        self.user_icon = PhotoImage(file="assets/user_icon.png", width=100, height=100)
        self.user_label = Label(self.left_frame, image=self.user_icon, bg=COLOR_BG)
        self.user_label.place(x=150, y=100, anchor="center")      
        
        self.label = primary_label(self.left_frame, text=f"Hello, {user_name}!", font=TEXT_TEXT)
        self.label.place(x=135, y=150, anchor="center")
        
        self.add_transaction_button = tk.Button(self.left_frame, text="Add Transaction", font=TEXT_LABEL, command=self.add_transaction)
        self.add_transaction_button.place(x=140, y=240, anchor="center")
        
        self.dashboard_button = tk.Button(self.left_frame, text="Dashboard", font=TEXT_LABEL, command=self.dashboard)
        self.dashboard_button.place(x=140, y=270, anchor="center")
        
        self.logout_button = tk.Button(self.left_frame, text="Logout", relief="solid", font=TEXT_LABEL, command=self.logout)
        self.logout_button.place(x=140, y=300, anchor="center")
        
        self.right_frame = Frame(self, bg=COLOR_PRIMARY, width=200, height=400)
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        self.balance_frame = Frame(self.right_frame, bg=COLOR_FRAME, width=350, height=150, highlightthickness=0)
        self.balance_frame.pack(side="top", fill="both", expand=False, padx=20, pady=20, anchor='center')
        
        self.pound_label = Label(self.balance_frame, text="£", font=TEXT_HEADING, bg=COLOR_FRAME, fg=COLOR_WHITE)
        self.pound_label.place(x=20, y=100)
        
        self.balance_label = balance_label(self.balance_frame, text="Total Balance", font=TEXT_HEADING, bg=COLOR_FRAME, fg=COLOR_WHITE)
        self.balance_label.place(x=40, y=20)
        
        self.balance_label = header_label(self.balance_frame, text=f"{self.balance}", font=TEXT_TITLE, bg=COLOR_FRAME, fg=COLOR_WHITE) 
        self.balance_label.place(x=40, y=70)
        
        
        # self.summary_frame = Frame(self.right_frame, bg=COLOR_FRAME, width=350, height=500, highlightthickness=0)
        # self.summary_frame.pack(side="left", fill="none", expand=True, padx=20, pady=20, anchor='sw')
        
        
        # self.summary_div = Frame(self.summary_frame, bg=COLOR_WHITE, width=280, height=200)
        # self.summary_div.pack(side="top", fill="y", expand=False, padx=10, pady=10, anchor='center')
         
        # self.summary_label = primary_label(self.summary_frame, text="Summary", font=TEXT_TEXT, bg=COLOR_FRAME, fg=COLOR_WHITE)
        # self.summary_label.place(x=20, y=25)
        
        # self.income_button = secondary_button(self.summary_frame, text="Incomes", font=TEXT_TEXT, command=self.view_incomes)
        # self.income_button.place(x=110, y=20)
        
        # self.expense_button = secondary_button(self.summary_frame, text="Expenses", font=TEXT_TEXT, command=self.view_expenses)
        # self.expense_button.place(x=220, y=20)   
            
        # self.summary_block = Frame(self.summary_frame, bg=COLOR_PRIMARY, width=280, height=50, highlightthickness=0)
        # self.summary_block.place(x=50, y=80)
            
        

    # def view_incomes(self):
    #     # for widget in self.summary_frame.winfo_children():
    #     #     widget.destroy()
    #     with open('data/transactions.json', 'r') as file:
    #         transactions = json.load(file)
    #     incomes = [t for t in transactions if t["type"] == "Income"]
    #     for i, income in enumerate(incomes):
    #         income_block = Frame(self.summary_frame, bg=COLOR_PRIMARY, width=280, height=50)
    #         income_block.place(x=50, y=80 + i*60)
    #         income_label = Label(
    #             income_block,
    #             text=f"Income {i+1}: £{income['amount']}({income['category']})",
    #             bg=COLOR_PRIMARY,
    #             fg="white",
    #         )
    #         income_label.pack()

    # def view_expenses(self):
            
    #     with open('data/transactions.json', 'r') as file:
    #         transactions = json.load(file)
    #     expenses = [t for t in transactions if t["type"] == "Expense"]
    #     for i, expense in enumerate(expenses):
    #         expense_block = Frame(self.summary_frame, bg=COLOR_PRIMARY, width=280, height=50)
    #         expense_block.place(x=50, y=80 + i*60)
    #         expense_label = Label(
    #             expense_block,
    #             text=f"Expense {i+1}: £{expense['amount']}({expense['category']})",
    #             bg=COLOR_PRIMARY,
    #             fg="white",
    #         )
    #         expense_label.pack()


    def add_transaction(self):
      
        atw = AddTransactionWindow(self)
        atw.grab_set()  

        
    def load_transactions(self):
        # Check if transactions.json file exists
        if os.path.exists('data/transactions.json'):
            with open('data/transactions.json', 'r') as file:
                transactions = json.load(file)
            return transactions
        else:
            # Return an empty list if the file does not exist
            return []
        
    def calculate_balance(self, transactions):
        balance = sum(t['amount'] for t in transactions if t['type'].lower() == 'income')
        balance -= sum(t['amount'] for t in transactions if t['type'].lower() == 'expense')
        return balance
    
 

    def dashboard(self):
        dashboard = Dashboard(self)
        dashboard.grab_set()
    
    def logout(self):
        self.destroy()
        lw = LoginWindow()
        lw.mainloop()
        


if __name__ == "__main__":
    mw = MainWindow("Test User")
    mw.mainloop()
