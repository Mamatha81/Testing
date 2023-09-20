Feature: Orange Hrm logo
  Scenario: Log in to the orghrm home page
    Given i Launch the chrome browser
    When i open hrm home page
    And enter username "Admin" and password "admin123"
    And click on login button
    And click on the section Time
    And scroll till find the element
    And take a view screen shot
    Then click the fourth element on view
    And take the inside view screen shot
    And write the comment
    And click on the section Recruitment
    And dropdown the job title
    And search the section names and send the keys

