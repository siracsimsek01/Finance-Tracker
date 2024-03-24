import tkinter as tk
from tkinter import Menu, Label

class MainWindow(tk.Tk):
    def __init__(self, user_name):
        super().__init__()
        self.title("PyFinance - Personal Finance Tracker")
        self.geometry("800x600")
        self.configure(bg="#0F102B")  # background color

        # personalized greeting
        self.greeting = Label(self, text=f"Welcome {user_name}!", fg="white", bg="#0F102B", font=("Helvetica", 18))
        self.greeting.pack()

        # users current account balance
        self.balance_label = Label(self, text="Current Balance: $0.00", fg="white", bg="#0F102B", font=("Helvetica", 18))
        self.balance_label.pack()

        # last transaction summary
        self.last_transaction_summary = Label(self, text="Last Transaction: None", fg="white", bg="#0F102B", font=("Helvetica", 18))
        self.last_transaction_summary.pack()

        # set up the menu bar
        self.setup_menu()

    def setup_menu(self):
        self.menu_bar = Menu(self, bg="#333333", fg="white") 
        self.config(menu=self.menu_bar)

        # transactions management menu
        self.transactions_menu = Menu(self.menu_bar, tearoff=0, bg="#333333", fg="white")
        self.menu_bar.add_cascade(label='Transactions Management', menu=self.transactions_menu)
        self.transactions_menu.add_command(label='Add Transaction', command=self.open_add_transaction)
        self.transactions_menu.add_command(label='View Summary', command=self.view_summary)
        self.transactions_menu.add_command(label='Delete Transaction', command=self.delete_transaction)

    def open_add_transaction(self):
        print("Add Transaction")

    def view_summary(self):
        print("View Summary")

    def delete_transaction(self):
        print("Delete Transaction")

