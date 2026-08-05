@regression
Feature: SauceDemo Checkout Process

  Background:
    Given I am logged in as a "standard_user"

  Scenario: Checkout Overview Page
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart 
    And I click checkout button
    And I fill in checkout information with first name "Krishna", last name "Sharma", and postal code "12345"
    Then I click continue button
    When I see the checkout overview page
    Then I should see "Sauce Labs Backpack" in the checkout overview
    And I should see item price in the checkout overview
    And I should see item quantity in the checkout overview
    And I should see the total price in the checkout overview
    And I should see the tax amount in the checkout overview
    And I should see the final total price in the checkout overview
    And I should see Payment Information in the checkout overview
    And I should see Shipping Information in the checkout overview


  Scenario: Cancel checkout overview process
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart
    And I click checkout button
    And I fill in checkout information with first name "Shamli", last name "Das", and postal code "67890"
    When I click continue button
    Then I should see the checkout overview page
    When I click Cancel button on the checkout overview page
    Then I should be redirected back to the inventory page from the checkout overview page

  @smoke
  Scenario: Finish checkout process
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart
    And I click checkout button
    And I fill in checkout information with first name "Krishna", last name "Sharma", and postal code "12345"
    When I click continue button
    Then I should see the checkout overview page
    When I click Finish button
    Then I should be redirected to the checkout complete page
    And I should see a confirmation message "Thank you for your order!"  