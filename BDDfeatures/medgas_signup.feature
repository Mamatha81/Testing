
Feature: signup in mymedgas
  Scenario: fill the details for signup
    Given login into the mymedgas home page
    When Click a signup Button
    And fill the signup details
    |Field name|input text|
    |First Name| Ruchira       |
    |Last Name|  Iris      |
#    |Email                   |    robot.medgas.uk@gmail.com       |
    |Email                   |    robot.mymedgas.uk_"timestamp"@gmail.com       |
    |Country Code            |     United Kingdom +44     |
    |Phone Number           | 9876543210        |
    |Extension             |    0987654321     |
    |Position                |  NA       |
    |Country                 | United Kingdom        |
    |password                |  MedGas101       |
    |password confirm      |  MedGas101   |
    |Company / Facility Name |   ruchira_iris     |
    |Address                 |    ruchiraadd    |
    |Address 2              |   NA     |
    |City                |   Ruchiracity     |
#    |State|                    Ruchirastate       |
    |Postal Code             |   1234     |
    And again click the signup button
    Then click ok button


  Scenario: continution to signup button
    Given mammu login into the my medgas home page
    When she have to enter email "gmail" and password "password"
    And she clicks on sign in button
    And click on "Admin"
    And click "New User Queue"
    And In search page search "ruchira"
    And click on first element
    Then in the new user page fill some details
    And click "Save & Approve"



