Feature: Restaurants logo
  Scenario: search restaurants in google maps
    Given i Launch the chrome browser
    When i have open restaurants on google page
    Then I save the nearby restaurants
