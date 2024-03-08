import tkinter as tk


root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("500x500")


name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()


def open_dashboard():

    name = name_entry.get()

    root.withdraw()

    dashboard = tk.Toplevel(root)
    dashboard.title("Finance Tracker Dashboard")
    dashboard.geometry("500x500")

    dashboard.protocol("WM_DELETE_WINDOW", on_close_dashboard)

    greeting_label = tk.Label(dashboard, text=f"Welcome, {name}!")
    greeting_label.pack()

    balance = 0
    balance_label = tk.Label(dashboard, text=f"Current Balance: ${balance}")
    balance_label.pack()


button = tk.Button(root, text="Log In", command=open_dashboard)
button.pack()


def on_close_dashboard():
    root.destroy()


root.mainloop()
