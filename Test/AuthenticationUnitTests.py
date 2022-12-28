import unittest
import Website



class AuthenticationUnitTests(unittest.TestCase):
    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.email = 'testingUser@test.com'
        self.password = '1234567Test'

    def test_login_success(self):
        self.setUp()
        # Send a POST request to the login route with the form data
        result = self.app.post('/login', data={'email': self.email, 'password': self.password})
        self.assertEqual(result.status_code, 302)
        self.assertEqual(result.location, '/u')

    def test_login_incorrect_password(self):
        self.setUp()
        result = self.app.post('/login', data={'email': self.email, 'password': 'wrong_password'}, follow_redirects=True)
        assert b'Incorrect password, try again.' in result.data

    def test_login_email_not_found(self):
        self.setUp()
        result = self.app.post('/login', data={'email': 'wrong@example.com', 'password': self.password})
        assert b'Email does not exist.' in result.data

    def test_logout_after_login(self):
        self.setUp()
        self.app.post('/login', data={'email': self.email, 'password': self.password})
        result = self.app.get('/logout')
        self.assertEqual(result.status_code, 302)
        self.assertEqual(result.location, '/login')
        result2 = self.app.get('/u')
        self.assertEqual(result2.status_code, 302)
        self.assertEqual('/login' in result2.location, True)

    def test_logout_without_login(self):
        self.setUp()
        result = self.app.get('/logout')
        self.assertEqual(result.status_code, 302)
        self.assertEqual('/login' in result.location, True)

    if __name__ == '__main__':
        unittest.main()