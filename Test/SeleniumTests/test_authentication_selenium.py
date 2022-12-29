import unittest
import Website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthenticationUnitTestsSelenium(unittest.TestCase):
    driver = webdriver.Chrome()
    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.driver.get("http://127.0.0.1:5000/login")
        self.email = 'testingUser@test.com'
        self.password = '1234567Test'

    def test_login_success(self):
        self.setUp()
        email_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
        email_field.send_keys(self.email)
        password1_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
        password1_field.send_keys(self.password)
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/form/button")
        submit_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]")))
        field = self.driver.find_element(By.XPATH,"/html/body/div[1]").text
        self.assertIn('Logged in successfully', field)

    def test_login_incorrect_password(self):
        self.setUp()
        email_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
        email_field.send_keys(self.email)
        password1_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
        password1_field.send_keys('IncPassword')
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/form/button")
        submit_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]")))
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('Incorrect password, try again', field)

    def test_login_email_not_found(self):
        self.setUp()
        email_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
        email_field.send_keys('incorrect@email')
        password1_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
        password1_field.send_keys(self.password)
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/form/button")
        submit_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]")))
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('Email does not exist', field)

    def test_logout_after_login(self):
        self.setUp()
        email_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
        email_field.send_keys(self.email)
        password1_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
        password1_field.send_keys(self.password)
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/form/button")
        submit_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]")))
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('Logged in successfully', field)

        log_out_button_drawer =self.driver.find_element(By.XPATH, "/html/body/nav/button/span")
        log_out_button_drawer.click()
        self.driver.implicitly_wait(10)
        log_out_button = self.driver.find_element(By.ID, "logout")
        log_out_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form/h3")))
        field2 = self.driver.find_element(By.XPATH, "/html/body/div/form/h3").text
        self.assertIn('Login', field2)

    if __name__ == '__main__':
        unittest.main(verbosity=2)