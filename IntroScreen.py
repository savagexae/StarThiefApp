import tkinter as tk
import time
from MainScreen import MainScreen

class IntroScreen(tk.Frame):
    def __init__(self, master, on_intro_complete):
        super().__init__(master)
        self.on_intro_complete = on_intro_complete
        self.pack_propagate(0)

        self.title_label = tk.Label(self, text="StarThief", font=("Helvetica", 36, "bold"))
        self.title_label.pack(pady=20)

        self.secret_label = tk.Label(self, text="Welcome home, StarThief", font=("Helvetica", 18))
        self.secret_label.pack(pady=20)

        self.after(2000, self.on_intro_complete)

if __name__ == "__main__":
    root = tk.Tk()
    intro_screen = IntroScreen(root, lambda: print("Intro Complete"))
    intro_screen.pack(expand=True, fill='both')
    root.mainloop()
