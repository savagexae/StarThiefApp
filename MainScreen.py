import tkinter as tk
from CountMyStars import CountMyStars
from SneakIntoTheGalaxy import SneakIntoTheGalaxy

class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(0)

        self.title_label = tk.Label(self, text="StarThief", font=("Helvetica", 36, "bold"))
        self.title_label.pack(pady=20)

        self.count_stars_button = tk.Button(self, text="Count My Stars", command=self.show_count_stars)
        self.count_stars_button.pack(pady=10)

        self.sneak_button = tk.Button(self, text="Sneak Into The Galaxy", command=self.show_sneak_into_galaxy)
        self.sneak_button.pack(pady=10)

    def show_count_stars(self):
        self.destroy()
        count_my_stars = CountMyStars(self.master)
        count_my_stars.pack(expand=True, fill='both')

    def show_sneak_into_galaxy(self):
        self.destroy()
        sneak_into_galaxy = SneakIntoTheGalaxy(self.master)
        sneak_into_galaxy.pack(expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    main_screen = MainScreen(root)
    main_screen.pack(expand=True, fill='both')
    root.mainloop()
