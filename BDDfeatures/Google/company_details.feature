Feature: Get company details
  Scenario Outline: Extracting Company Details
    Given User is On Google Page
    When she Searched For Company "<company_name>"
    And she Extract Information
    Then Successfully Make Csv file of all data
    Examples:
      | company_name                                           |
      |actualize consulting engineers (india) private limited   |
      | Aimleap                                                |
      | g7 cr technologies india private limited               |
      | No company                                             |
    |Convergytics solutions pvt ltd                                                        |