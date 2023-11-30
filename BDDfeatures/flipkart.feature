Feature: mobiles put in cart
  Scenario: Open the flipkart and add mobile into cart

    Given Mamatha opens flipkart home
    When she search "dell laptop"
    And she filters by stars "4"
    And she add top "4" products
    And she click on cart
    Then she calculate the cart value