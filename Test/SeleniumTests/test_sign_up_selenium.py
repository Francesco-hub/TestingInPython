from datetime import datetime
import unittest
import Website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SignUpUnitTestsSelenium(unittest.TestCase):
    driver = webdriver.Chrome()
    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.driver.get("http://127.0.0.1:5000/sign-up")
        self.email1 = 'testingUser@test.com'
        self.email2 = str(hash(str(datetime.now()))) + '@test.com'
        self.email3 = 'testingUseraasssssa@test.com'
        self.password = '1234567Test'
        self.password2 = '1234567Tests'
        self.first_name = 'Test'

    def test_sign_up_email_exists_sign_up_fails(self):
        self.setUp()
        self.driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input").send_keys(self.email1)
        self.driver.find_element(By.XPATH,"/html/body/div/form/div[2]/input").send_keys(self.first_name)
        self.driver.find_element(By.XPATH,"/html/body/div/form/div[3]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH,"/html/body/div/form/div[4]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH,"/html/body/div/form/button").click()
        field = self.driver.find_element(By.XPATH,"/html/body/div[1]").text
        self.assertIn('Email already exists', field)

    def test_sign_up_email_too_short_sign_up_fails(self):
        self.setUp()
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys('a@b')
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys(self.first_name)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/button").click()
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('Email must be greater than 3 characters', field)

    def test_first_name_too_short_sign_up_fails(self):
        self.setUp()
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys(self.email3)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys('a')
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/button").click()
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('First name must be greater than 1 character', field)

    def test_password_too_short_sign_up_fails(self):
        self.setUp()
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys(self.email3)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys(self.first_name)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys('1234')
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys('1234')
        self.driver.find_element(By.XPATH, "/html/body/div/form/button").click()
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('Password must be at least 7 characters', field)

    def test_passwords_dont_match_sign_up_fails(self):
        self.setUp()
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys(self.email3)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys(self.first_name)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys(self.password2)
        self.driver.find_element(By.XPATH, "/html/body/div/form/button").click()
        field = self.driver.find_element(By.XPATH, "/html/body/div[1]").text
        self.assertIn('Passwords don\'t match', field)

    def test_sign_up_success(self):
        self.setUp()
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys(self.email2)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys(self.first_name)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys(self.password)
        self.driver.find_element(By.XPATH, "/html/body/div/form/button").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/h1")))
        field = self.driver.find_element(By.XPATH, "/html/body/div[2]/h1").text
        self.assertIn('Notes', field)


    if __name__ == '__main__':
        unittest.main()

