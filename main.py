import tkinter as tk
from gui.login_window import LoginWindow
from gui.main_window import MainWindow


def main():

    root = tk.Tk()

    login_app = LoginWindow(master=root)
    root.mainloop()

    if hasattr(login_app, "user_name"):

        new_root = tk.Tk()
        app = MainWindow(
            master=new_root, user_name=login_app.user_name
        ) 
        app.mainloop()


if __name__ == "__main__":
    main()
