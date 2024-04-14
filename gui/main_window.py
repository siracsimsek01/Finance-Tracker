import tkinter as tk
from tkinter import Label, Frame, PhotoImage, Canvas, Scrollbar, Frame, PhotoImage
from .add_transaction_window import AddTransactionWindow
from .dashboard_window import Dashboard
from utils.styles import *
import json
import os


from .delete_transaction import DeleteTransaction


class MainWindow(tk.Tk):

    def __init__(self, user_name):
        tk.Tk.__init__(self)
        self.title("PyFinance - Personal Finance Tracker")
        self.geometry("700x700")
        self.configure(bg="#0F102B")
        self.balance = 0
        self.resizable(False, False)
        self.user_name = user_name

        # Set user name and greeting

        self.left_frame = Frame(self, bg=COLOR_BG, width=300, height=600)
        self.left_frame.pack(side="left", fill="both", expand=False)

        self.user_icon = PhotoImage(file="assets/user_icon.png", width=100, height=100)
        self.user_label = Label(self.left_frame, image=self.user_icon, bg=COLOR_BG)
        self.user_label.place(x=150, y=100, anchor="center")

        self.label = primary_label(
            self.left_frame, text=f"Hello, {self.user_name}!", font=TEXT_TEXT
        )
        self.label.place(x=135, y=150, anchor="center")

        self.add_transaction_button = tk.Button(
            self.left_frame,
            text="Add Transaction",
            font=TEXT_LABEL,
            command=self.add_transaction,
        )
        self.add_transaction_button.place(x=140, y=240, anchor="center")

        self.dashboard_button = tk.Button(
            self.left_frame, text="Dashboard", font=TEXT_LABEL, command=self.dashboard
        )
        self.dashboard_button.place(x=140, y=270, anchor="center")

        self.logout_button = tk.Button(
            self.left_frame,
            text="Logout",
            relief="solid",
            font=TEXT_LABEL,
            command=self.logout,
        )
        self.logout_button.place(x=140, y=400, anchor="center")
        
        self.logo = PhotoImage(file="assets/logo.png", width=200, height=200)
        self.logo_label = Label(self.left_frame, image=self.logo, bg=COLOR_BG)
        self.logo_label.place(x=150, y=650, anchor="center")

        self.right_frame = Frame(self, bg=COLOR_PRIMARY, width=200, height=400)
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.balance_frame = Frame(
            self.right_frame,
            bg=COLOR_FRAME,
            width=350,
            height=150,
            highlightthickness=0,
        )
        self.balance_frame.pack(
            side="top", fill="both", expand=False, padx=20, pady=20, anchor="center"
        )

        self.pound_label = Label(
            self.balance_frame,
            text="£",
            font=TEXT_HEADING,
            bg=COLOR_FRAME,
            fg=COLOR_WHITE,
        )
        self.pound_label.place(x=20, y=100)

        self.header_label = header_label(
            self.balance_frame,
            text="Total Balance",
            font=TEXT_HEADING,
            bg=COLOR_FRAME,
            fg=COLOR_WHITE,
        )
        self.header_label.place(x=40, y=20)

        self.balance_label = balance_label(
            self.balance_frame,
            text=f"{self.balance}",
            font=TEXT_TITLE,
            bg=COLOR_FRAME,
            fg=COLOR_WHITE,
        )
        self.balance_label.place(x=40, y=70)
        self.update_balance()

        self.transactions_label = header_label(
            self.right_frame,
            text="Last Transactions",
            font=TEXT_HEADING,
            bg=COLOR_PRIMARY,
            fg=COLOR_WHITE,
        )
        self.transactions_label.pack(
            side="top", fill="x", expand=False, padx=20, pady=20
        )

        self.refresh_button = tk.Button(
            self.right_frame,
            text="Refresh",
            font=TEXT_LABEL,
            command=self.update_transactions
        )
        self.refresh_button.pack(side="bottom", fill="x", padx=20, pady=20)

        self.canvas = Canvas(
            self.right_frame,
            bg=COLOR_PRIMARY,
            highlightthickness=2,
            highlightbackground="black",
        )
        self.scrollbar = Scrollbar(
            self.right_frame, orient="vertical", command=self.canvas.yview
        )

        self.transactions_frame = Frame(
            self.canvas, bg=COLOR_PRIMARY, width=350, height=250
        )
        self.transactions_frame_id = self.canvas.create_window(
            (0, 0), window=self.transactions_frame, anchor="nw"
        )

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.transactions_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.pack(
            side="left", fill="both", expand=True, padx=20, pady=20, anchor="center"
        )
        self.scrollbar.pack(side="right", fill="y")

        Dashboard.view_transactions(self)

    def add_transaction(self):
        atw = AddTransactionWindow(self)
        atw.grab_set()
        self.update_balance()
        Dashboard.view_transactions(self)

    def load_transactions(self):
        # check if transactions.json file exists
        if os.path.exists("data/transactions.json"):
            with open("data/transactions.json", "r") as file:
                transactions = json.load(file)
            return transactions
        else:
            # Return an empty list if the file does not exist
            return []

    def calculate_balance(self, transactions):
        balance = sum(
            t["amount"] for t in transactions if t["type"].lower() == "income"
        )
        balance -= sum(
            t["amount"] for t in transactions if t["type"].lower() == "expense"
        )
        return balance

    def update_balance(self):
        transactions = self.load_transactions()
        self.balance = self.calculate_balance(transactions)
        self.balance_label.config(text=f"{self.balance}")
        return self.balance
    
    def update_transactions(self):
        transactions = self.load_transactions()
        self.transactions_frame.destroy()
        self.transactions_frame = Frame(
            self.canvas, bg=COLOR_PRIMARY, width=350, height=250
        )
        self.transactions_frame_id = self.canvas.create_window(
            (0, 0), window=self.transactions_frame, anchor="nw"
        )
        Dashboard.view_transactions(self)
        
    # def start_main_window(user_name):
    #     mw = MainWindow(user_name)
    #     mw.mainloop()
    
      

    def dashboard(self):
        dashboard = Dashboard(self)
        dashboard.grab_set()
        self.update_balance()

    def delete_transaction(self):
        dt = DeleteTransaction(self)
        dt.grab_set()
        self.update_balance()
        Dashboard.view_transactions(self)

    def logout(self):
        from .login_window import LoginWindow
        self.destroy()
        lw = LoginWindow(self)
        lw.mainloop()


# if __name__ == "__main__":
#      main_window = MainWindow(user_name)
#     main_window.mainloop()