import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from add_transaction_window import AddTransactionWindow




class MainWindow(tk.Tk):
    def __init__(self, user_name):
        super().__init__()
        self.style = Style(theme='darkly')
        self.title("PyFinance - Personal Finance Tracker")
        self.geometry("800x600")
        self.configure(bg="#0F102B")


        # personalized greeting
        self.greeting = tk.Label(self, text=f"Welcome {user_name}!", style='Inverse.TLabel')
        self.greeting.pack()

        # user's current account balance
        self.balance_label = tk.Label(self, text="Current Balance: $0.00", style='Inverse.TLabel')
        self.balance_label.pack()

      
        self.last_transaction_summary = tk.Label(self, text="Last Transaction: None", style='Inverse.TLabel')
        self.last_transaction_summary.pack()

    
        self.setup_menu()
        
    def setup_menu(self):
        self.menu_bar = tk.Menu(self, style='TMenu')
        self.config(menu=self.menu_bar)

      
        self.transactions_menu = tk.Menu(self.menu_bar, tearoff=0, style='TMenu')
        self.menu_bar.add_cascade(label='Transactions Management', menu=self.transactions_menu)
        self.transactions_menu.add_command(label='Add Transaction', command=self.open_add_transaction)
        self.transactions_menu.add_command(label='View Summary', command=self.view_summary)
        self.transactions_menu.add_command(label='Delete Transaction', command=self.delete_transaction)
    
    def open_add_transaction(self):
     add_transaction_window = AddTransactionWindow(self)
     add_transaction_window.grab_set() 

        
if __name__ == '__main__':
    root = MainWindow()  
    root.mainloop()