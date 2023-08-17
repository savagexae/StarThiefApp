import tkinter as tk
import os

from IntroScreen import IntroScreen
from MainScreen import MainScreen

class StarThiefApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StarThief")
        
        self.intro_screen = IntroScreen(root, self.show_main_screen)
        self.intro_screen.pack(expand=True, fill='both')

    def show_main_screen(self):
        self.intro_screen.pack_forget()
        main_screen = MainScreen(self.root)
        main_screen.pack(expand=True, fill='both')

def main():
    # Set the DISPLAY environment variable for X11 forwarding if not set
    display_num = os.environ.get("DISPLAY")
    if display_num is None:
        os.environ["DISPLAY"] = "localhost:0.0"

    root = tk.Tk()
    app = StarThiefApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
