Feature: If the user search for a movie or tv show, proper results must be returned according to the search criteria and filters
  @T1
  Scenario: Verify that when the user searches for a keyword, the search returns results according to that keyword
    Given I am on TMDB home page
    When I click on the search input and I enter "King Kong" text
    When I click "ENTER"
    Then I should have at least "1" results returned
    Then The search results must have "king kong" in the movie/tv show title