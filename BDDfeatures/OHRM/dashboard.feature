Feature: Orange Hrm logo
  Scenario: Log in to the orghrm home page
    Given i Launch the chrome browser
    When i open hrm home page
    And enter username "Admin" and password "admin123"
    And click on login button
#    And login to the dash board
    And scroll the till find element
    And take a screen shot
    #full page screen shot
    Then login to the PIM
    And click the add button
    And take the screen shot
    # particular element screenshot

