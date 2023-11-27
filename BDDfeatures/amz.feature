Feature: mobiles put in cart
  Scenario: Open Amazon and add devices to the cart and verify the cart price

    Given mamatha Launched chrome browser
    When she opens amazon homes page
    And she search for "iqoo" mobile
    And she filters by rating "4"
    And she add top "3" products to the cart
    And she naviagtes to cart
    Then she verifies the cart value is same