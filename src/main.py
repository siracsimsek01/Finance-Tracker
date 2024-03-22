import tkinter as tk
from ttkbootstrap import Style
from gui.login_window import LoginWindow
from gui.main_window import MainWindow


# Start the Tkinter event loop for the login window


def main():
    login_window = LoginWindow()
    user_name = login_window.name_input.get()
    login_window.destroy()

    main_window = MainWindow(user_name)
    main_window.mainloop()


if __name__ == "__main__":
    main()
