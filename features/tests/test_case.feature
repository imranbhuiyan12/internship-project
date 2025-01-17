
Feature: internship project


  Scenario: User can filter by sale status Out of Stocks
    Given Open the main page
    Then  Log in to the page email and password
    When  Click on “off plan” at the left side menu
    Then  Verify the right page opens
    When  Click on Filters and Filter by sale status of “Out of Stocks”
    Then  Verify each product contains the Out of Stocks tag




