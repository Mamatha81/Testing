Feature: Orange Hrm logo
  Scenario: Log in to the orghrm home page
    Given i Launch the chrome browser
    When i open hrm home page
    And enter username "Admin" and password "admin123"
    Then click on login button

