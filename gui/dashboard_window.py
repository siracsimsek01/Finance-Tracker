import tkinter as tk
from tkinter import Label, Frame, messagebox, PhotoImage, Toplevel, Button, Entry, messagebox
from tkinter.ttk import Combobox
from utils.styles import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.simpledialog import askstring
import json
import datetime, calendar
from .delete_transaction import DeleteTransaction
from utils.graphs import load_transactions, process_data, bar_chart, pie_chart




class Dashboard(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Dashboard")
        self.geometry("1000x600")
        self.configure(bg=COLOR_BG)
        self.parent = parent
        
        
        self.main_frame = Frame(self, bg=COLOR_BG, width=900, height=600)
        self.main_frame.pack(side="top", fill="both", expand=True)
        
       

        self.transactions_frame = Frame(self.main_frame, bg=COLOR_PRIMARY, width=800, height=600)
        self.transactions_frame.pack(side="left", fill="both", expand=False, padx=10, pady=10, anchor="w")
        
        self.transactions_label = Label(self.main_frame, bg=COLOR_BG, text="Filter Transactions", font=TEXT_HEADING)
        self.transactions_label.pack(side="top", fill="x", padx=10, pady=10, anchor="w")
        
        self.filter_frame = Frame(self.main_frame, bg=COLOR_BG, width=600, height=10)
        self.filter_frame.pack(side="top", fill="x", expand=False, anchor="w", pady=10)
        
        
        self.filter_by_time = Combobox(self.filter_frame, values=["Today","This Week", "This Month", "This Year", "All Time"], state="readonly", width=10)
        self.filter_by_time.set("Time")
        self.filter_by_time.pack(side="left", padx=10, pady=10)
        
        self.filter_by_type = Combobox(self.filter_frame, values=["Income", "Expense"], state="readonly", width=10)
        self.filter_by_type.set("Type")
        self.filter_by_type.pack(side="left", padx=10, pady=10)
        
        self.filter_by_category = Combobox(self.filter_frame, values=["Salary", "Pension", "Interest", "Others", "Food", "Rent", "Clothing", "Car", "Health", "Others"], state="readonly", width=10)
        self.filter_by_category.set("Category")
        self.filter_by_category.pack(side="left", padx=10, pady=10)
        
        self.filter_by_source = Entry(self.filter_frame, width=10)
        self.filter_by_source.insert(0, "Enter Source")
        self.filter_by_source.pack(side="left", padx=10, pady=10)
        
        self.filter_button = Button(self.filter_frame, text="Filter", command=self.filter_transactions)
        self.filter_button.pack(side="left", fill="x", padx=10, pady=10)
        
        self.delete_button = Button(self.main_frame, text="Delete Transaction", width=30, height=3, command=self.open_delete_window)
        self.delete_button.place(x=525, y=310)
        self.view_transactions()
        
        self.print_button = Button(self.main_frame, text="Print Transactions", width=30, height=3, command=self.print_transactions)
        self.print_button.place(x=525, y=390)
        
        self.barChart_btn = Button(self.main_frame, text="Statistics in Bar Chart", width=30, height=3, command=self.display_barchart)
        self.barChart_btn.place(x=525, y=150)

        self.pieChart_btn = Button(self.main_frame, text="Statistics in Pie Chart", width=30, height=3, background=COLOR_BG, fg=COLOR_BLACK, command=self.display_piechart)
        self.pieChart_btn.place(x=525, y=230)
        
        
        
    def display_barchart(self):
        transactions = load_transactions()
        income_sums, expense_sums = process_data(transactions)
        fig = bar_chart(income_sums, expense_sums)

        graph = Toplevel(self.main_frame)
        graph.title("Bar Chart")

        canvas = FigureCanvasTkAgg(fig, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)



        
    def display_piechart(self):
        chart_type = askstring("Chart Type", "Enter 'Income' or 'Expense' to display:")
        if chart_type and chart_type.lower() in ['income', 'expense']:
            transactions = load_transactions()
            fig = pie_chart(transactions, chart_type=chart_type.capitalize())

            graph = tk.Toplevel(self.main_frame)
            graph.title(f"{chart_type.capitalize()} Pie Chart")

            canvas = FigureCanvasTkAgg(fig, master=graph)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        else:
            tk.messagebox.showerror("Invalid Input", "Please enter either 'Income' or 'Expense'.")
             
        
    
    def view_transactions(self):
        with open("data/transactions.json", "r") as file:
            transactions = json.load(file)
            
        for transaction in transactions:
            date = transaction["date"]
            amount = transaction["amount"]
            category = transaction["category"]
            source = transaction["payee_source"]
            type = transaction["type"]
            
            transaction_label = primary_label(self.transactions_frame, text=f"{category} from {source} ---  {type} \n {date}                                                                  £{amount}", font=TEXT_TEXT)
            transaction_label.pack(side="top", fill="x", padx=10, pady=10)
            transaction_label.config(height=3)
            
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

                transaction_label = primary_label(self.transactions_frame,text=f"{category} from {source} ---  {type} \n {date}                                                                  £{amount}", font=TEXT_LABEL)
                transaction_label.pack(side="top", fill="x", padx=10, pady=10)
        else:
            no_transactions_label = primary_label(self.transactions_frame, text="No transactions to display", font=TEXT_LABEL)
            no_transactions_label.pack(side="top", fill="x", padx=10, pady=10)
            
      except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        
        
        
        
        
    def open_delete_window(self):
        delete_window = DeleteTransaction(self)
        delete_window.grab_set()
        
    def print_transactions(self):
        try:
            with open("data/transactions.json", "r") as file:
                transactions = json.load(file)
            with open("data/transactions.txt", "w") as file:
                for transaction in transactions:
                    date = transaction["date"]
                    amount = transaction["amount"]
                    category = transaction["category"]
                    source = transaction["payee_source"]
                    type = transaction["type"]
                    file.write(f"{date} - {amount} - {category} - {source} - {type}\n")
            messagebox.showinfo("Success", "Transactions printed to data/transactions.txt")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            

       



if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()