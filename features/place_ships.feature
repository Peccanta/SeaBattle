Feature: Testing the place_ships function

  Scenario: Placing ships on the board
    Given I have a game board
    When I place ships on the board
    Then the ships should be placed correctly
