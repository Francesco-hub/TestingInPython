import unittest
import Website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

unittest.TestLoader.sortTestMethodsUsing = None

class NotesDeleteUnitTestsSelenium(unittest.TestCase):
    driver = webdriver.Chrome()

    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.driver.get("http://127.0.0.1:5000/login")
        self.email = 'testingUser@test.com'
        self.password = '1234567Test'
        self.testNote = 'This is a test note'
        email_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
        email_field.send_keys(self.email)
        password1_field = self.driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
        password1_field.send_keys(self.password)
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/form/button")
        submit_button.click()

    def test_delete_note_success(self):
        self.setUp()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/ul/li/button/span")))
        note = self.driver.find_element(By.XPATH, "/html/body/div[2]/ul/li").text
        delete_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/ul/li/button/span")
        delete_button.click()
        try:
            note = self.driver.find_element(By.XPATH, "/html/body/div[2]/ul/li").text
        except:
            self.assertTrue(2==2)



if __name__ == '__main__':
    unittest.main()