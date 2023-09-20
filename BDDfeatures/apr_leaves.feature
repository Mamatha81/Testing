Feature: login orangehrm
  Scenario Outline: approve/Reject leaves
    Given i Launch the chrome browser
    When i open hrm home page
    And enter username "Admin" and password "admin123"
    And click on login button
    Then click on the section Leave
    And give the <action>
    And close browser
    Examples:
      |action|
      | Approve|
      | Reject|
    