Feature: login to the facebook
  Scenario: i am login to the facebook page
    Given mamatha Launch chrome browser
    When I open facebook home page
    And I enter mail "name@gmail.com" and password "xyz123"
    And I click a login button
    Then I click a saved button
    And I take screenshot
    And I click home button
    And I click logout button
