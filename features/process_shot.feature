Feature: Testing the process_shot function

  Scenario: Testing a hit
    Given a game board
    When the process_shot function is called with row 2 and col 2
    Then it should print Попадание!

Scenario: Testing a miss
  Given a game board
  When the process_shot function is called with row 4 and col 5
  Then it should print Промах.

