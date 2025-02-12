Feature: JSONPlaceholder API Validation

  Scenario Outline: Verify user endpoints
    Given I set API endpoint to "<endpoint>"
    When I send a GET request
    Then the response status code should be 200
    And the response should contain at least <count> items

    Examples:
      | endpoint    | count |
      | users       | 10    |
      | posts       | 100   |
      | comments    | 500   |