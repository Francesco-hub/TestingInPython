import unittest
import Website

class SignUpUnitTests(unittest.TestCase):
    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.email1 = 'testingUser@test.com'
        self.email2 = 'testingUser2@test.com'
        self.password = '1234567Test'
