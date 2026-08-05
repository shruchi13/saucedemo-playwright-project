@regression
Feature: SauceDemo Checkout Process

  Background:
    Given I am logged in as a "standard_user"
    
  @smoke
  Scenario: Fill in checkout information
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart 
    And I click checkout button
    And I fill in checkout information with first name "Krishna", last name "Sharma", and postal code "12345"
    When I click continue button
    Then I should see the checkout overview page
    
  @smoke
  Scenario: Cancel checkout process
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart
    And I click checkout button
    And I fill in checkout information with first name "Shamli", last name "Das", and postal code "67890"
    When I click Cancel button
    Then I should be redirected back to the shopping cart page

  Scenario: Error message for missing checkout information
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart
    And I click checkout button
    And I fill in checkout information with first name "", last name "Sharma", and postal code "12345"
    And I click continue button
    Then I should see an error message "Error: First Name is required"

  
   