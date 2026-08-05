Feature: SauceDemo Inventory & Cart Management

  Background:
    Given I am logged in as a "standard_user"

  Scenario: Verify Inventory Page Loaded
    Then I should see the page title "Products"
    And there should be 6 products displayed

  Scenario: Add Product to Cart
    When I add "Sauce Labs Backpack" to the cart
    Then the shopping cart badge count should be "1"

  Scenario: Remove Product from Cart
    When I add "Sauce Labs Backpack" to the cart
    And I remove item "Sauce Labs Backpack" from the inventory page
    Then the shopping cart badge count should be "0"

  Scenario: Sort Products by Price (Low to High)
    When I sort products by "Price (low to high)"
    Then the products should be sorted by price in ascending order

  Scenario: Sort Products by Price(High to Low)
    When I sort products by "Price (High to Low)"
    Then the products should be sorted by price in decending order 

  Scenario: Sort Products by Name (A to Z)
    When I sort products by "Name(A to Z)"
    Then the products should be sorted alphabetically from A to Z

  Scenario: Sort Products by Name (Z to A)
    When I sort products by "Name(Z to A)"
    Then the products should be sorted alphabetically from Z to A