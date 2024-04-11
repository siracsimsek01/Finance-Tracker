import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox
from tkinter.ttk import Combobox
# from main_window import MainWindow
import json
from datetime import datetime
import random
import os

class AddTransactionWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Transaction")
        self.geometry("400x300")
        self.configure(bg="#0F102B")
        self.parent = parent  

        # Transaction Type Selection
        Label(self, text="Transaction Type:", bg="#0F102B", fg="white").pack()
        self.transaction_type = Combobox(self, values=["Income", "Expense"], state="readonly")
        self.transaction_type.pack()
        self.transaction_type.bind("<<ComboboxSelected>>", self.update_categories)

        # Category Dropdown
        Label(self, text="Category:", bg="#0F102B", fg="white").pack()
        self.category = Combobox(self, state="readonly")
        self.category.pack()

        # Amount Entry
        Label(self, text="Amount:", bg="#0F102B", fg="white").pack()
        self.amount = Entry(self)
        self.amount.pack()

        # Date Entry
        Label(self, text="Date (YYYY-MM-DD):", bg="#0F102B", fg="white").pack()
        self.date = Entry(self)
        self.date.pack()

        # Payee/Source Entry
        Label(self, text="Payee/Source:", bg="#0F102B", fg="white").pack()
        self.payee_source = Entry(self)
        self.payee_source.pack()

        # Save Button
        self.save_button = Button(self, text="Save", command=self.save_transaction)
        self.save_button.pack()

    def update_categories(self, event=None):
        if self.transaction_type.get() == "Income":
            self.category['values'] = ["Salary", "Pension", "Interest", "Others"]
        else:
            self.category['values'] = ["Food", "Rent", "Clothing", "Car", "Health", "Others"]
        self.category.set('')  
        
    

    def save_transaction(self):
        transaction_type = self.transaction_type.get()
        category = self.category.get()
        amount = self.amount.get()
        date = self.date.get()
        payee_source = self.payee_source.get()

    
        try:
            amount = float(amount)  

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return
        
        # Build the transaction dictionary
        transaction = {
            'id': random.randint(1000, 9999), 
            'type': transaction_type,
            'category': category,
            'amount': amount,
            'date': date,
            'payee_source': payee_source
        }

        # Define the file path and ensure the directory exists
        transactions_file_path = os.path.join('data', 'transactions.json')
        os.makedirs(os.path.dirname(transactions_file_path), exist_ok=True)

        # Load existing transactions from file or initialize as an empty list
        if os.path.exists(transactions_file_path):
            with open(transactions_file_path, 'r') as file:
                transactions = json.load(file)
        else:
            transactions = []

       
        transactions.append(transaction)


        with open(transactions_file_path, 'w') as file:
            json.dump(transactions, file, indent=4)


        messagebox.showinfo("Success", "Transaction saved successfully!")
        
        if transaction["type"] == "Income":
            self.parent.balance += transaction["amount"]
        else:
            self.parent.balance -= transaction["amount"]
            
        with open('data/balance.json', 'w') as file:
            json.dump(self.parent.balance, file)

        # If this window has a reference to a parent window, update balance
        if hasattr(self, 'parent') and hasattr(self.parent, 'update_balance'):
            self.parent.update_balance()

        self.destroy()  # Close the AddTransactionWindow
        
        
    # def get_average_income(self):
    #     income = [t["amount"] for t in self.transactions if t["type"] == "Income"]
    #     return sum(income) / len(income) if income else 0.0
    
    def get_average_income(self):
        with open('data/transactions.json', 'r') as file:
            transactions = json.load(file)
            
        income_transactions = [t for t in transactions if t["type"] == "Income"]
        income_amounts = [t["amount"] for t in income_transactions]
        return income_amounts
    
        
    
    def get_average_expense(self):
        with open('data/transactions.json', 'r') as file:
            transactions = json.load(file)
            
        expense_transactions = [t for t in transactions if t["type"] == "Expense"]
        expense_amounts = [t["amount"] for t in expense_transactions]
        return expense_amounts



if __name__ == '__main__':
    # This section is for testing purposes
    root = tk.Tk()
    root.withdraw()
    atw = AddTransactionWindow(root)
    atw.mainloop()
