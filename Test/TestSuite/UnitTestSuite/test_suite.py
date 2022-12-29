import unittest

from Test.UnitTests.test_authentication import AuthenticationUnitTests
from Test.UnitTests.test_notes import NotesUnitTests
from Test.UnitTests.test_notes_delete import NotesDeleteUnitTests
from Test.UnitTests.test_sign_up import SignUpUnitTests


unittest.TestLoader.sortTestMethodsUsing = None

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(AuthenticationUnitTests)
    suite.addTests(NotesUnitTests)
    suite.addTests(NotesDeleteUnitTests)
    suite.addTests(SignUpUnitTests)


    unittest.TextTestRunner.run(suite)