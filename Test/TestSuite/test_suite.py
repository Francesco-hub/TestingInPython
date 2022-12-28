import unittest

from Test.test_authentication import AuthenticationUnitTests
from Test.test_notes import NotesUnitTests
from Test.test_note_delete import NotesDeleteUnitTests

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(AuthenticationUnitTests)
    suite.addTests(NotesUnitTests)
    suite.addTests(NotesDeleteUnitTests)

    unittest.TextTestRunner().run(suite)