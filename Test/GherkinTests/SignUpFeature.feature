Feature: SignUp Function
    Scenario: I give an existing email, an appropriate name, a first password equal to a second password

      Given I want to sign up
      When I try to sign up using 'testingUser@test.com' as email and 'AppropriateName' as name and 'Password' as  first password and 'Password' as second password
      Then the sign up result is 'False' with message: 'Email already exists'

    Scenario: I give a non existing, inappropriate email, an appropriate name, a first password equal to a second password

      Given I want to sign up
      When I try to sign up using 'a@b' as email and 'AppropriateName' as name and 'Password' as  first password and 'Password' as second password
      Then the sign up result is 'False' with message: 'Email must be greater than 3 characters'

    Scenario: I give a non existing email, an inappropriate name, a first password equal to a second password

      Given I want to sign up
      When I try to sign up using 'notExistingEmail@test.com' as email and 'a' as name and 'Password' as  first password and 'Password' as second password
      Then the sign up result is 'False' with message: 'First name must be greater than 1 character'

    Scenario: I give a non existing email, an appropriate name, a first inappropriate password equal to a second password

      Given I want to sign up
      When I try to sign up using 'nonExistingEmail@test.com' as email and 'AppropriateName' as name and 'pass' as  first password and 'pass' as second password
      Then the sign up result is 'False' with message: 'Password must be at least 7 characters'

    Scenario: I give a non existing email, an appropriate name, a first password not equal to a second password

      Given I want to sign up
      When I try to sign up using 'nonExistingEmail@test.com' as email and 'AppropriateName' as name and 'Password' as  first password and 'DifferentPassword' as second password
      Then the sign up result is 'False' with message: 'Passwords don\'t match'

      Scenario: I give a non existing email, an appropriate name, a first password equal to a second password

      Given I want to sign up
      When I try to sign up using 'nonExistingEmail@test.com' as email and 'AppropriateName' as name and 'Password' as  first password and 'Password' as second password
      Then the sign up result is 'True' with message: 'Account created!'