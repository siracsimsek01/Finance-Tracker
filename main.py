# main.py
from tkinter import Tk
from src.gui.login_window import LoginWindow  # Adjust the import path as per your project structure

if __name__ == '__main__':
    # Instantiate and show the Login Window
    login = LoginWindow()
    login.mainloop()