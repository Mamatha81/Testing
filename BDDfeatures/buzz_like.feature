Feature: login orangehrm
  Scenario: comments/likes
    Given i Launch the chrome browser
    When i open hrm home page
    And enter username "Admin" and password "admin123"
    And click on login button
    Then i click on the Buzz
    And click on Most Liked Posts
    And i click on the Admin
    And delete top 5 actions





