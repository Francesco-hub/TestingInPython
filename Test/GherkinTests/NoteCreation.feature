Feature: Notes Function

    Scenario: I want to create a note with no content

      Given I want to create a note
      When I try to create the note with content ''
      Then the note creation result is 'False' with message: 'Note is too short'

    Scenario: I want to create a note with appropriate content

      Given I want to create a note
      When I try to create the note with content 'AppropriateContent'
      Then the note creation result is 'True' with message: 'Note added!'