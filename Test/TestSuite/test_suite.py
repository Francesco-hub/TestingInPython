import unittest

from Test.UnitTests.test_authentication import AuthenticationUnitTests
from Test.UnitTests.test_notes import NotesUnitTests
from Test.UnitTests.test_notes_delete import NotesDeleteUnitTests
from Test.UnitTests.test_sign_up import SignUpUnitTests
from Test.SeleniumTests.test_sign_up_selenium import SignUpUnitTestsSelenium
from Test.SeleniumTests.test_authentication_selenium import AuthenticationUnitTestsSelenium
from Test.SeleniumTests.test_notes_creation_selenium import NotesUnitTestsSelenium
from Test.SeleniumTests.test_notes_delete_selenium import NotesDeleteUnitTestsSelenium

unittest.TestLoader.sortTestMethodsUsing = None

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(AuthenticationUnitTests)
    suite.addTests(NotesUnitTests)
    suite.addTests(NotesDeleteUnitTests)
    suite.addTests(SignUpUnitTests)
    suite.addTests(SignUpUnitTestsSelenium)
    suite.addTests(AuthenticationUnitTestsSelenium)
    suite.addTests(NotesUnitTestsSelenium)
    suite.addTests(NotesDeleteUnitTestsSelenium)


    unittest.TextTestRunner.run(suite)