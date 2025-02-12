Feature: GitHub Repository CRUD Operations

  Scenario: Full CRUD lifecycle for repository
    Given I have valid GitHub credentials
    When I create a repository named "test-repo-bdd"
    Then the response status code should be 201
    And the repository "test-repo-bdd" should exist
    
    When I update the repository description to "Updated description"
    Then the response status code should be 200
    And the repository description should be "Updated description"
    
    When I delete the repository
    Then the response status code should be 204
    And the repository "test-repo-bdd" should not exist