import tkinter as tk
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

if __name__ == "__main__":
    root = tk.Tk()
    app = StarThiefApp(root)
    root.mainloop()
