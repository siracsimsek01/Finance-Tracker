import tkinter as tk
from tkinter import messagebox, Label, Entry, Button
import json


class DeleteTransaction(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Delete Transaction")
        self.geometry("600x600")
        
          # input field for transaction ID
        self.id_label = Label(self, text="Transaction ID:")
        self.id_label.pack(pady=(0,5))
        self.id_entry = Entry(self)
        self.id_entry.pack(pady=(0,10))
        
        # transaction list
        self.trans_list = tk.Listbox(self, height=15, width=50)
        self.trans_list.pack(pady=20, padx=20)

      
        # button to delete the transaction
        delete_button = Button(self, text="Delete Transaction", command=self.delete_transaction)
        delete_button.pack(pady=(0,10))

        self.load_transactions()

    def load_transactions(self):
        self.trans_list.delete(0, tk.END) 
        try:
            with open("data/transactions.json", "r") as file:
                self.transactions = json.load(file)
            for transaction in self.transactions:
                display_text = f"ID: {transaction['id']} - {transaction['amount']} - {transaction['category']}"
                self.trans_list.insert(tk.END, display_text)
        except FileNotFoundError:
            messagebox.showerror("Error", "Transaction file not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error reading transaction data.")

    def delete_transaction(self):
        transaction_id = self.id_entry.get()
        if not transaction_id:
            messagebox.showwarning("Warning", "Please enter a transaction ID.")
            return

        transaction_found = False
        for i, transaction in enumerate(self.transactions):
            if str(transaction['id']) == transaction_id:
                transaction_found = True
                confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete transaction ID {transaction_id}?")
                if confirm:
                    del self.transactions[i]
                    self.update_transactions_json()
                    self.load_transactions()
                    self.id_entry.delete(0, tk.END)
                    break

        if not transaction_found:
            messagebox.showinfo("Not Found", "Transaction ID not found. Please try again.")

    def update_transactions_json(self):
        try:
            with open("data/transactions.json", "w") as file:
                json.dump(self.transactions, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update transactions: {e}")
