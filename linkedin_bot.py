
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LinkedInBot:
    def __init__(self):
        self.options = uc.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=self.options)
        self.logged_in = False

    def login(self, username, password):
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(3)
        email_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        if "feed" in self.driver.current_url:
            self.logged_in = True

    def connect_or_message(self, profile_url, message=""):
        self.driver.get(profile_url)
        time.sleep(5)
        try:
            message_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Message')]")
            if message:
                message_button.click()
                time.sleep(2)
                textarea = self.driver.find_element(By.TAG_NAME, "textarea")
                textarea.send_keys(message)
                send_btn = self.driver.find_element(By.XPATH, "//button[contains(., 'Send')]")
                send_btn.click()
                return "Message sent"
            return "Already connected, no message sent"
        except:
            pass
        try:
            connect_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Connect')]")
            if connect_button.is_enabled():
                connect_button.click()
                time.sleep(2)
                try:
                    send_button = self.driver.find_element(By.XPATH, "//button[contains(., 'Send')]")
                    send_button.click()
                except:
                    pass
                return "Connection request sent"
            return "Connect button disabled"
        except:
            return "No Connect or Message buttons found"

    def close(self):
        self.driver.quit()
