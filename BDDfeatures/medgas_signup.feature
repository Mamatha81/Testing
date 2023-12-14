Feature: signup in mymedgas
  Scenario: fill the details for signup
    Given login into the mymedgas home page
    When Click a signup Button
    And fill the signup details
    |Field name|input text|
    |First Name| Ruchira       |
    |Last Name|  Iris      |
    |Email                   |    xxxxxxx       |
    |Country Code            |    Australia +61     |
    |Phone Number           | 9876543210        |
    |Extension             |    0987654321     |
    |Position                |  NA       |
    |Country                 | Australia        |
    |password                |  xxxx       |
    |password confirm      |  xxxx   |
    |Company / Facility Name |   ruchira_iris     |
    |Address                 |    ruchiraadd    |
    |Address 2              |   NA     |
    |City                |   Ruchiracity     |
#    |STATE|                   | Ruchirastate       |
    |Postal Code             |   1234     |
    And again click the signup button
    Then click ok button
