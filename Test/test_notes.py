import unittest
import Website



class NoteUnitTests(unittest.TestCase):
    def setUp(self):
        app = Website.create_app('testing')
        self.app = app.test_client()
        self.email = 'testingUser@test.com'
        self.password = '1234567Test'