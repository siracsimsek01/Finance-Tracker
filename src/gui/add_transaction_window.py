import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
# from gui.main_window import MainWindow  


class AddTransactionWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Transaction")
        self.geometry("400x400")
        
        self.style = Style(theme="darkly")
        
        transaction_type_label = ttk.Label(self, text="Transaction Type:")
        transaction_type = ttk.Combobox(self, values=["Income", "Expense"])
        
        # dropdown for category
        
        category_label = ttk.Label(self, text="Category:")
        if transaction_type.get() == "Income":
            category = ttk.Combobox(self, values=["Salary", "Pension", "Interest", "Other"])
        else:
            category = ttk.Combobox(self, values=["Groceries", "Rent", "Utilities", "Transport", "Other"])
        
        # input for amount
        
        amount_label = ttk.Label(self, text="Amount:")
        amount = ttk.Entry(self)
        
        # input for payee or source
        
        payee_source_label = ttk.Label(self, text="Payee/Source:")
        payee_source = ttk.Entry(self)
        
        save_btn = ttk.Button(self, text="Save", style='success.Outline.TButton', command=self.save_transaction)
        
        # layout the widgets
        
        transaction_type_label.pack(fill='x', padx=10, pady=5)
        transaction_type.pack(fill='x', padx=10, pady=5)
        category_label.pack(fill='x', padx=10, pady=5)
        category.pack(fill='x', padx=10, pady=5)
        amount_label.pack(fill='x', padx=10, pady=5)
        amount.pack(fill='x', padx=10, pady=5)
        payee_source_label.pack(fill='x', padx=10, pady=5)
        payee_source.pack(fill='x', padx=10, pady=5)
        save_btn.pack(fill='x', padx=10, pady=10)
        
    def save_transaction(self):
       pass
            
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
