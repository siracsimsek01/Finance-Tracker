from tkinter import Tk, Frame
from gui.main_window import MainWindow

class LoginWindow(Frame):
    def __init__(self, parent=MainWindow):
        super().__init__(parent)
        self.pack()

def main():
    root = Tk()
    login_app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()