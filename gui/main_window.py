import tkinter as tk
from tkinter import Label, Frame, messagebox, PhotoImage, Canvas
from .add_transaction_window import AddTransactionWindow
from .login_window import LoginWindow
from utils.styles import *
# from  utils.styles import primary_label, TEXT_TEXT, COLOR_BG
import json
import os


class MainWindow(tk.Tk):
    def __init__(self, user_name=""):
        super().__init__()
        self.title("PyFinance - Personal Finance Tracker")
        self.geometry("1000x600")
        self.configure(bg="#0F102B")
        self.balance = 0
        
        border_radius = int(0.3 * 20)

        # Set user name and greeting
        
        self.left_frame = Frame(self, bg=COLOR_BG, width=300, height=600)
        self.left_frame.pack(side="left", fill="both", expand=False)
        
                
        self.user_icon = PhotoImage(file="assets/user_icon.png", width=100, height=100)
        self.user_label = Label(self.left_frame, image=self.user_icon, bg=COLOR_BG)
        self.user_label.place(x=150, y=100, anchor="center")      
        
        self.label = primary_label(self.left_frame, text=f"Hello, {user_name}!", font=TEXT_TEXT)
        self.label.place(x=135, y=150, anchor="center")
        
        self.add_transaction_button = tk.Button(self.left_frame, text="Add Transaction", font=TEXT_LABEL, command=self.add_transaction)
        self.add_transaction_button.place(x=140, y=300, anchor="center")
        
        self.dashboard_button = tk.Button(self.left_frame, text="Dashboard", font=TEXT_LABEL, command=self.dashboard)
        self.dashboard_button.place(x=140, y=340, anchor="center")
        
        self.logout_button = tk.Button(self.left_frame, text="Logout", relief="solid", font=TEXT_LABEL, command=self.logout)
        self.logout_button.place(x=140, y=500, anchor="center")
        
        
        self.right_frame = Frame(self, bg=COLOR_PRIMARY, width=700, height=600)
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        self.balance_frame = Frame(self.right_frame, bg=COLOR_FRAME, width=350, height=150, highlightthickness=0)
        self.balance_frame.pack(side="top", fill="none", expand=True, padx=20, pady=20, anchor='nw')
        
        pound_label = Label(self.balance_frame, text="£", font=TEXT_LABEL, bg=COLOR_FRAME, fg=COLOR_WHITE)
        
        self.balance_label = balance_label(self.balance_frame, text="Total Balance", font=TEXT_HEADING, bg=COLOR_FRAME, fg=COLOR_WHITE)
        self.balance_label.place(x=20, y=20)
        
        self.balance_label = header_label(self.balance_frame, text=f"{pound_label}{self.balance}", font=TEXT_HEADING)
        self.balance_label.place(x=330, y=100)
        

        
        # greeting = Label(
        #     self,
        #     text=f"Welcome {user_name}!",
        #     fg="white",
        #     bg="#0F102B",
        #     font=("Helvetica", 18),
        # )
        # greeting.pack()

        # # Setup initial balance
        # self.balance = 0
        # self.balance_label = Label(
        #     self,
        #     text=f"Your current balance is: £{self.balance}",
        #     fg="white",
        #     bg="#0F102B",
        #     font=("Helvetica", 18),
        # )
        # self.balance_label.pack()

        
        # buttons_frame = tk.Frame(self, bg="#0F102B")
        # buttons_frame.pack(pady=10)
        

        # self.add_transaction_button = tk.Button(
        #     self,
        #     text="Add Transaction",
        #     command=self.add_transaction,
        #     bg="#333333",
        #     relief="solid",
        #     width=20,
        # )
        # self.add_transaction_button.pack(in_=buttons_frame, side="left", padx=10)

        # # Button to view summary
        # self.summary_button = tk.Button(
        #     self,
        #     text="View Summary",
        #     command=self.view_summary,
        #     bg="#333333",
        #     relief="solid",
        #     width=20,
        # )
        # self.summary_button.pack(in_=buttons_frame, side="left", padx=10)

        # # Button to delete transaction
        # self.delete_transaction_button = tk.Button(
        #     self,
        #     text="Delete Transaction",
        #     command=self.delete_transaction,
        #     bg="#333333",
        #     relief="solid",
        #     width=20,
        # )
        # self.delete_transaction_button.pack(in_=buttons_frame, side="left", padx=10)

        # # Frame for showing summary of transactions
        # self.summary_frame = Frame(self, bg="#0F102B")
        # self.summary_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Load transactions and update balance
        self.load_transactions()
        # self.update_balance()

    def load_transactions(self):
      try:
        
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.json'))
        
        # check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Transactions file does not exist at path: {file_path}")
        
        with open(file_path, "r") as file:
            self.transactions = json.load(file)
      except FileNotFoundError as e:
            self.transactions = []
            messagebox.showerror("Error", str(e))
      except json.JSONDecodeError as e:
        self.transactions = []
        messagebox.showerror("Error", f"Invalid JSON format in transactions file: {file_path}")



    # def update_balance(self):
    #     balance = sum(t["amount"] if t["type"] == "Income" else -t["amount"] for t in self.transactions)
    #     self.balance = balance
    #     self.balance_label.configure(text=f"Current balance: £{self.balance:.2f}")

    def view_summary(self):
        # Clear the current frame
        for widget in self.summary_frame.winfo_children():
            widget.destroy()

            if not self.transactions:
                messagebox.showinfo("Summary", "No transactions to display.")
            return

        # Adjust how transactions are displayed based on their type
        for i, transaction in enumerate(self.transactions):
            if transaction["type"] == "Income":
                detail = transaction.get(
                    "source", "N/A"
                )  # Use .get() to avoid KeyError
            else:  # For Expense transactions
                detail = transaction.get("payee", "N/A")

            transaction_label = Label(
                self.summary_frame,
                text=f"Transaction {i+1}: {transaction['type']} - £{transaction['amount']} from {detail} ({transaction['category']})",
                bg="#0F102B",
                fg="white",
            )
            transaction_label.pack()

    def add_transaction(self):
        # This will open a new AddTransactionWindow and handle the transaction
        atw = AddTransactionWindow(self)
        atw.grab_set()  # Make the new window modal

    def delete_transaction(self):
        # Placeholder for delete transaction functionality
        messagebox.showinfo(
            "Delete Transaction",
            "Delete transaction functionality not implemented yet.",
        )

    def dashboard(self):
        # Placeholder for dashboard functionality
        pass
    
    def logout(self):
        self.destroy()
        lw = LoginWindow()
        lw.mainloop()
        
    # Main menu is now redundant since buttons are added directly to the window


if __name__ == "__main__":
    mw = MainWindow("Test User")
    mw.mainloop()
