*** Settings ***
Resource          ..${/}resource${/}resource.robot

Documentation    Suite description
Test Setup  Init Driver


*** Test Cases ***
Verify current date
    When navigate to calendar
    Then verify current date is correct

Create a note
    When navigate to home screen
    When create note    @test_data.note.text
    Then assert note title is correct    @test_data.note.text
    Then assert note body is correct    @test_data.note.text

