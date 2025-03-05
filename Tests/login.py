# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import unittest

# from Locators.locators import Locators
# from Pages.loginPage import LoginPage
# from Pages.homePage import HomePage
# import HtmlTestRunner


# class LoginTet(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#         cls.driver.get(r"C:\Users\Amit\Downloads\login-test-automation-main\login-test-automation-main\login_test.html")
#         cls.driver.implicitly_wait(10)
#         cls.driver.maximize_window()

#     def test_login_not_valid(self):
#         driver = self.driver
#         login = LoginPage(driver)
#         login.enter_username('Admin')
#         login.enter_password('wrongPassword')
#         login.click_login()
#         actual_text = WebDriverWait(self.driver, 100).until(
#             EC.presence_of_element_located((By.XPATH, Locators.alert_message_xpath))
#         ).text
#         self.assertIn('Invalid credentials', actual_text)

#     def test_login_valid(self):
#         login = LoginPage(self.driver)
#         login.enter_username('Admin')
#         login.enter_password('admin123')
#         login.click_login()

#         expected_url = r'C:\Users\Amit\Downloads\login-test-automation-main\login-test-automation-main\login_test.html'
#         WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

#         self.assertEqual(self.driver.current_url, expected_url)

#         homePage = HomePage(self.driver)
#         homePage.click_dropdown()
#         homePage.logout()
#         time.sleep(2)

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         cls.driver.quit()
#         print("Test Completed")


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
#         output=r'C:\Users\Amit\Downloads\login-test-automation-main\login-test-automation-main\reports'))



from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

from Locators.locators import Locators
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
import HtmlTestRunner

class LoginTet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        # Use the local HTML file path
        cls.driver.get("file:///" + r"C:\Users\Amit\Downloads\login-test-automation-main\login-test-automation-main\login_test.html".replace('\\', '/'))
        
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_not_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        
        # Modify to match your HTML page's selectors
        login.enter_username('admin')  # Lowercase 'admin'
        login.enter_password('wrongpassword')
        login.click_login()
        
        # Modify to match your HTML page's error message selector
        actual_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'message'))
        ).text
        self.assertIn('Invalid Credentials', actual_text)

    def test_login_valid(self):
        login = LoginPage(self.driver)
        
        # Modify to match your HTML page's credentials
        login.enter_username('admin')
        login.enter_password('password123')
        login.click_login()

        # Wait for home section to be visible
        home_section = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'homeSection'))
        )
        self.assertTrue(home_section.is_displayed(), "Home section should be visible after login")

        # Optional: Add logout if needed
        # logout_button = self.driver.find_element(By.ID, 'logoutBtn')
        # logout_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r'C:\Users\Amit\Downloads\login-test-automation-main\login-test-automation-main\reports'))