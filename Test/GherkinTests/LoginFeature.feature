
  Feature: Login Function
    Scenario: I give an existing email and password and the login is successful

      Given I want to login
      When I try to login using 'testingUser@test.com' as email and '1234567Test' as password
      Then the login should be 'True'

      Scenario: I give a non existing email and password and the login is unsuccessful

      Given I want to login
      When I try to login using 'notExisting@test.com' as email and '1234567Test' as password
      Then the login should be 'False'

      Scenario: I give an existing email and a wrong password and the login is un successful

      Given I want to login
      When I try to login using 'testingUser@test.com' as email and 'WrongPassword' as password
      Then the login should be 'False'







