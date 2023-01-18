import unittest

from Test.SeleniumTests.test_sign_up_selenium import SignUpUnitTestsSelenium
from Test.SeleniumTests.test_authentication_selenium import AuthenticationUnitTestsSelenium
from Test.SeleniumTests.test_notes_creation_selenium import NotesUnitTestsSelenium
from Test.SeleniumTests.test_notes_delete_selenium import NotesDeleteUnitTestsSelenium

unittest.TestLoader.sortTestMethodsUsing = None

if __name__ == '__main__':

    suite = unittest.TestSuite()
    
    suite.addTests(SignUpUnitTestsSelenium)
    suite.addTests(AuthenticationUnitTestsSelenium)
    suite.addTests(NotesUnitTestsSelenium)
    suite.addTests(NotesDeleteUnitTestsSelenium)


    unittest.TextTestRunner.run(suite)