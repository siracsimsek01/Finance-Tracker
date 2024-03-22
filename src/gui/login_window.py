import tkinter as tk
from tkinter import ttk



class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Login - PyFinance (Personal Finance Tracker)")
        self.geometry("800x600") 
        self.configure(bg="#0F102B", cursor="hand2")

        # container
        self.box = tk.Frame(self, width=405, height=240, bg="#23243C")
        self.box.place(relx=0.5, rely=0.5, anchor="center")

        logo = tk.PhotoImage(file="img/logo.png")
        logo_label = ttk.Label(self.box, image=logo)
        logo_label.image = logo
        logo_label.pack(pady=20, padx=30, anchor="center")

        welcome_text = ttk.Label(
            self.box,
            text="Welcome to PyFinance!\n",
            font=("Helvetica", 18),
            foreground="white",
            background="#23243C",
        )
        welcome_text.pack(anchor="s")
        sub_text = ttk.Label(
            self.box,
            text="Please enter your name to continue.",
            font=("Helvetica", 14),
            foreground="white",
            background="#23243C",
        )
        sub_text.pack(anchor="s")

        # input field
        self.name_input = ttk.Entry(self.box, font=("Helvetica", 16), width=30)
        self.name_input.pack(pady=10)

        # button
        login_button = ttk.Button(
            self.box, text="Login", command=self.login, style="TButton"
        )
        login_button.pack(pady=10)

        # configuring style of the widgets
        style = ttk.Style()
        style.configure("TLabel", background="#23243C")
        style.configure("TEntry", fieldbackground="#23243C", foreground="white")
        style.configure(
            "TButton", background="#5C6BC0", foreground="white", font=("Helvetica", 14)
        )

    def login(self):
        user_name = self.name_input.get()
        self.destroy()  # Destroy the login window


# Run the window
if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()