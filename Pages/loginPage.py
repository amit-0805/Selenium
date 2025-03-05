# from selenium.webdriver.common.by import By

# from Locators.locators import Locators


# class LoginPage():

#     def __init__(self, driver):
#         self.driver = driver

#         self.username_textbox_xpath = Locators.username_textbox_xpath
#         self.password_textbox_xpath = Locators.password_textbox_xpath
#         self.login_button_xpath = Locators.login_button_xpath

#     def enter_username(self, username):
#         self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
#         self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

#     def enter_password(self, password):
#         self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
#         self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

#     def click_login(self):
#         self.driver.find_element(By.XPATH, self.login_button_xpath).click()



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Modify these to match your HTML page's selectors
        self.username_textbox_xpath = "//input[@id='username']"
        self.password_textbox_xpath = "//input[@id='password']"
        self.login_button_xpath = "//button[@type='submit']"

    def enter_username(self, username):
        # Use more robust element location
        username_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'username'))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        # Use more robust element location
        password_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        # Use more robust element location
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.TAG_NAME, 'button'))
        )
        login_button.click()