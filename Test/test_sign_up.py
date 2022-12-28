import datetime
import unittest
import Website
from datetime import datetime



class SignUpUnitTests(unittest.TestCase):
    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.email1 = 'testingUser@test.com'
        self.email2 = str(datetime.now()) + '@test.com'
        self.email3 = 'testingUseraasssssa@test.com'
        self.password = '1234567Test'
        self.password2 = '1234567Tests'
        self.first_name = 'Test'

    def test_sign_up_email_exists_sign_up_fails(self):
        self.setUp()
        result = self.app.post('/sign-up', data={'email': self.email1, 'firstName': self.first_name, 'password1': self.password,'password2': self.password})
        self.assertIn(b'Email already exists', result.data)

    def test_sign_up_email_too_short_sign_up_fails(self):
        self.setUp()
        result = self.app.post('/sign-up',data={'email': 'a@b', 'firstName': self.first_name, 'password1': self.password, 'password2': self.password})
        self.assertIn(b'Email must be greater than 3 characters', result.data)

    def test_first_name_too_short_sign_up_fails(self):
        self.setUp()
        result = self.app.post('/sign-up', data={'email': self.email3, 'firstName': 'a', 'password1': self.password,'password2': self.password})
        print(result.data)
        self.assertIn(b'First name must be greater than 1 character', result.data)
    def test_password_too_short_sign_up_fails(self):
        self.setUp()
        result = self.app.post('/sign-up', data={'email': self.email3, 'firstName': self.first_name, 'password1': '123', 'password2': '123'})
        print(result.data)
        self.assertIn(b'Password must be at least 7 characters', result.data)
    def test_passwords_dont_match_sign_up_fails(self):
        self.setUp()
        result = self.app.post('/sign-up', data={'email': self.email3, 'firstName': self.first_name, 'password1': self.password, 'password2': self.password2})
        print(result.data)
        self.assertIn(b'Passwords don&#39;t match', result.data)

    def test_sign_up_success(self):
        self.setUp()
        result = self.app.post('/sign-up', data={'email': self.email2, 'firstName': self.first_name, 'password1': self.password, 'password2': self.password})
        self.assertEqual(result.location, '/u')
        login = self.app.post('/login', data={'email': self.email2, 'password': self.password})
        self.assertEqual(login.status_code, 302)
        self.assertEqual(login.location, '/u')




