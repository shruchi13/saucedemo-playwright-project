@smoke
Feature: SauceDemo Authentication

 Scenario: Successful Login with Standard User
   Given I navigate to SauceDemo login page
   When I log in with username "standard_user" and password "secret_sauce"
   Then I should be redirected to the inventory page

Scenario: Failed Login with Locked Out User 
   Given I navigate to SauceDemo login page
   When I log in with username "locked_out_user" and password "secret_sauce"
   Then I should see an error message "Epic sadface: Sorry, this user has been locked out."

