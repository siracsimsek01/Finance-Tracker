import tkinter as tk
from tkinter import PhotoImage, Label, Entry, Button

class LoginWindow(tk.Tk):
    def __init__(self, parent):
        super().__init__(parent)

        # set window properties
        self.title("Login - PyFinance (Personal Finance Tracker)")
        self.geometry("800x600")
        self.configure(bg="#0F102B")  # set the background color

        # Container frame for the login form
        self.box = tk.Frame(self, width=405, height=240, bg="#333333")
        self.box.place(relx=0.5, rely=0.5, anchor="center")


        # logo
        self.logo = PhotoImage(file="assets/logo.png")
        logo_label = Label(self.box, image=self.logo, bg="#333333") 
        logo_label.pack(pady=20, padx=30, anchor="center")

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
        self.name_input.pack(pady=10)

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
        self.user_name = self.name_input.get()
        # print("User name entered:", user_name)
        self.destroy()

# # Run the window
# if __name__ == "__main__":
#     login_window = LoginWindow()
#     login_window.mainloop()
