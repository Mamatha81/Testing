Feature: Internshala test for Interns
  Scenario: I have toLog into the facegenie page
    Given I have to Launch chrome browser
    When I have to open facegenie home page
    And I have to enter mail "testbams@gmail.com" and pass word "facegenie"
    And I have to click a login button
    Then I have to click a logout button

#  Scenario: I have to log into Dashboard page
#  Scenario: I have to log into manage student page
#  Scenario: I have to log into manage liceince
  
