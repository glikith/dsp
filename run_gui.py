from tkinter import Tk
from ui.gui import DeadlockGUI

def main():
    root = Tk()
    app = DeadlockGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
