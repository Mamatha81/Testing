Feature: mobiles put in cart
  Scenario: i am login to the amzon online shopping page

    Given mamatha Launched chrome browser
    When she opens amazon homes page
    And she search for "iqoo" mobile
    And she filters by rating "4"
    And she add top "3" products to the cart
    Then she verifies the cart value is same