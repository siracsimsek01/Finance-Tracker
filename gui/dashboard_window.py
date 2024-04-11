import tkinter as tk
from tkinter import Label, Frame, messagebox, PhotoImage, Toplevel, Button, Entry, messagebox
from tkinter.ttk import Combobox
# from .main_window import MainWindow
from utils.styles import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import datetime, calendar
from .delete_transaction import DeleteTransaction

class Dashboard(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Dashboard")
        self.geometry("1200x600")
        self.configure(bg=COLOR_BG)
        self.parent = parent
        
        self.main_frame = Frame(self, bg=COLOR_BG, width=1200, height=600)
        self.main_frame.pack(side="top", fill="both", expand=True)

        self.transactions_frame = Frame(self.main_frame, bg=COLOR_PRIMARY, width=800, height=600)
        self.transactions_frame.pack(side="bottom", fill="y", expand=True, padx=10, pady=10, anchor="w")
        
        
        self.filter_frame = Frame(self.main_frame, bg=COLOR_BG, width=600, height=10)
        self.filter_frame.pack(side="top", fill="x", expand=False, anchor="w")
        
        self.filter_by_time = Combobox(self.filter_frame, values=["Today","This Week", "This Month", "This Year", "All Time"], state="readonly", width=10)
        self.filter_by_time.set("Time")
        self.filter_by_time.pack(side="left", padx=10, pady=10)
        
        self.filter_by_type = Combobox(self.filter_frame, values=["Income", "Expense"], state="readonly", width=10)
        self.filter_by_type.set("Type")
        self.filter_by_type.pack(side="left", padx=10, pady=10)
        
        self.filter_by_category = Combobox(self.filter_frame, values=["Salary", "Pension", "Interest", "Others", "Food", "Rent", "Clothing", "Car", "Health", "Others"], state="readonly", width=10)
        self.filter_by_category.set("Category")
        self.filter_by_category.pack(side="left", padx=10, pady=10)
        
        self.filter_by_source = Entry(self.filter_frame, width=20)
        self.filter_by_source.insert(0, "Enter Source")
        self.filter_by_source.pack(side="left", padx=10, pady=10)
        
        self.filter_button = Button(self.filter_frame, text="Filter", command=self.filter_transactions)
        self.filter_button.pack(side="left", fill="x", padx=10, pady=10)
        
        self.delete_button = Button(self.filter_frame, text="Delete Transaction", command=self.open_delete_window)
        self.delete_button.pack(side="left", fill="x", padx=10, pady=10)
        self.view_transactions()
        
    
    def view_transactions(self):
        with open("data/transactions.json", "r") as file:
            transactions = json.load(file)
            
        for transaction in transactions:
            date = transaction["date"]
            amount = transaction["amount"]
            category = transaction["category"]
            source = transaction["payee_source"]
            type = transaction["type"]
            
            transaction_label = primary_label(self.transactions_frame, text=f"{date} - {amount} - {category} - {source} - {type}", font=TEXT_LABEL)
            transaction_label.pack(side="top", fill="x", padx=10, pady=10)
            
        return 
        
    def filter_transactions(self):
      try:
        # get the selected filter values
        time = self.filter_by_time.get()
        selected_type = self.filter_by_type.get()
        category = self.filter_by_category.get()
        source = self.filter_by_source.get()

        # Open the transactions file
        with open("data/transactions.json", "r") as file:
            transactions = json.load(file)

    
        for transaction in transactions:
           
            transaction["date"] = datetime.datetime.strptime(transaction["date"], "%Y-%m-%d").date()

        # Filter the transactions based on the selected time
        today = datetime.date.today()
        if time == "Today":
            filtered_transactions = [t for t in transactions if t["date"] == today]
        elif time == "This Week":
            start_of_week = today - datetime.timedelta(days=today.weekday())
            end_of_week = start_of_week + datetime.timedelta(days=6)
            filtered_transactions = [t for t in transactions if start_of_week <= t["date"] <= end_of_week]
        elif time == "This Month":
            start_of_month = today.replace(day=1)
            end_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])
            filtered_transactions = [t for t in transactions if start_of_month <= t["date"] <= end_of_month]
        elif time == "This Year":
            start_of_year = today.replace(month=1, day=1)
            end_of_year = today.replace(month=12, day=31)
            filtered_transactions = [t for t in transactions if start_of_year <= t["date"] <= end_of_year]
        else:  # all Time
            filtered_transactions = transactions

        # filter by type, category, and source if specified
        if selected_type != "Type":
            filtered_transactions = [t for t in filtered_transactions if t["type"] == selected_type]
        if category != "Category":
            filtered_transactions = [t for t in filtered_transactions if t["category"] == category]
        if source != "Enter Source" and source.strip():
            filtered_transactions = [t for t in filtered_transactions if t["payee_source"] == source]

        # clear the transactions frame
        for widget in self.transactions_frame.winfo_children():
            widget.destroy()

        # display the filtered transactions or a message if there are none
        if filtered_transactions:
            for transaction in filtered_transactions:
                date = transaction["date"].strftime("%Y-%m-%d")  # Format date as string for display
                amount = transaction["amount"]
                category = transaction["category"]
                source = transaction["payee_source"]
                transaction_type = transaction["type"]

                transaction_label = primary_label(self.transactions_frame, text=f"{date} - {amount} - {category} - {source} - {transaction_type}", font=TEXT_LABEL)
                transaction_label.pack(side="top", fill="x", padx=10, pady=10)
        else:
            no_transactions_label = primary_label(self.transactions_frame, text="No transactions to display", font=TEXT_LABEL)
            no_transactions_label.pack(side="top", fill="x", padx=10, pady=10)
            
      except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        
        
    def open_delete_window(self):
        delete_window = DeleteTransaction(self)
        delete_window.grab_set() 
    
        
        
        



       



if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()