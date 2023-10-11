Feature: Проверка функции place_ship

  Scenario: Размещение корабля на поле
    Given создаем игровое поле
    When размещаем корабль "Submarine" на поле
    Then корабль "Submarine" размещен на поле
