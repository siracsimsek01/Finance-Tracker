import tkinter as tk
from tkinter import PhotoImage, Label, Entry, Button, messagebox, Frame
from .main_window import MainWindow


class LoginWindow(tk.Tk):
    def __init__(self, user_name):
        super().__init__()

        # set window properties
        self.title("Login - PyFinance (Personal Finance Tracker)")
        self.geometry("800x600")
        self.configure(bg="#0F102B")  # set the background color

        # Container frame for the login form
        self.box = Frame(self, width=405, height=400, bg="#333333")
        self.box.place(relx=0.5, rely=0.5, anchor="center")
        self.user_name = user_name

        # logo
        self.logo = PhotoImage(file="assets/logo.png")
        logo_label = Label(self.box, image=self.logo, bg="#333333")
        logo_label.pack(padx=20, pady=20, anchor="center", side="top", fill="x")

        # Welcome text
        welcome_text = Label(
            self.box,
            text="Welcome to PyFinance!\n",
            font=("Helvetica", 18),
            fg="white",
            bg="#333333",
        )
        welcome_text.pack(anchor="s")

        # sub text
        sub_text = Label(
            self.box,
            text="Please enter your name to continue.",
            font=("Helvetica", 14),
            fg="white",
            bg="#333333",
        )
        sub_text.pack(anchor="s")

        # Input field
        self.name_input = Entry(self.box, font=("Helvetica", 16), width=30)
        self.name_input.pack(pady=5)

        # button
        login_button = Button(
            self.box,
            text="Login",
            command=self.login,
            fg="black",
            bg="#5C6BC0",
            font=("Helvetica", 14),
        )
        login_button.pack(pady=10)

    def login(self):
        self.user_name = self.name_input.get() # get the user name
        if self.user_name: # check if the user name is not empty
            self.destroy()
            mw = MainWindow(user_name=self.user_name) # create the main window with the user name entered
            mw.mainloop()
        else:
            messagebox.showerror("Error", "Please enter your name to continue.")


# Run the window
if __name__ == "__main__":
    lw = LoginWindow()
    lw.mainloop()
