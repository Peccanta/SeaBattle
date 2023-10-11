from behave import *

# Импортируем функции и классы из вашей программы
from shipBattle import create_board, place_ship

# Шаги для сценария
@given("создаем игровое поле")
def create_game_board(context):
    context.board = create_board()

@when('размещаем корабль "{ship}" на поле')
def place_ship_on_board(context, ship):
    size = 4  # Здесь укажите желаемый размер корабля
    context.ship = ship
    context.result = place_ship(context.board, ship, size)

@then('корабль "{ship}" размещен на поле')
def verify_ship_placement(context, ship):
    for row in context.board:
        for cell in row:
            if cell == "S":
                return
    assert False, f'Корабль "{ship}" не был размещен на поле'
