@medgas
Feature: work on the mymedgas
  Background: common steps in mymedgs
    Given mammu login into the my medgas home page
    When she have to enter email "gamil" and password "password"
    And she clicks on sign in button

  @facilities
  Scenario: open mymedgas website and login
    When she click on the "Facilities"
    And she click on the add facility
    And she fill the the some needed details
    And she click on the save button
    Then she search "iris_4" in facility searchbar


  @assets
  Scenario: Add new asset in creating facility
    When she have to click on the assets
    And In the assets page in facility search bar search for "iris_3
    And she have to click on the new asset
    And In that pagesearch section search the "Gem10"
    And add new asset section
    Then she have to click Save button























