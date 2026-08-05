@regression
Feature: SauceDemo Cart Management

Background:
    Given I am logged in as a "standard_user"

Scenario: See Cart Page
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart 
    Then cart Page should load 
    And I should see "Sauce Labs Backpack" in the cart
    And I should see item price in the cart 
    And I should see item quantity in the cart 
@smoke
Scenario: Proceed to checkout page
    When I go to shopping cart
    And I click checkout button
    Then I navigate to checkout page 
@smoke
Scenario: Remove Item from cart 
    When I add "Sauce Labs Backpack" to the cart
    And I go to shopping cart
    And I remove "Sauce Labs Backpack" from the cart page
    Then "Sauce Labs Backpack" should not be in the cart

    
Scenario: Proceed to continue shopping 
    when I go to shopping cart
    And I click continue shopping button
    Then I navigate back to inventory page
   


 

