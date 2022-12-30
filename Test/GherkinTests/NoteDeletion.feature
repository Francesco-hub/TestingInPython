Feature: Delete Notes Function

    Scenario: I want to delete a note with a given id that exists

      Given I want to delete a note
      When I try to delete the note with id '4'
      Then the note deletion result is 'False'

    Scenario: I want to create a note with a given id that does not exist

      Given I want to delete a note
      When I try to delete the note with id '1'
      Then the note deletion result is 'True'