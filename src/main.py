import tkinter as tk
from gui.login_window import LoginWindow
from gui.main_window import MainWindow


def main():

    login_window = LoginWindow()
    login_window.mainloop()

    if hasattr(login_window, "user_name"):
        user_name = login_window.user_name
        main_window = MainWindow(user_name)
        main_window.mainloop()


if __name__ == "__main__":
    main()
