from behave import *

from shipBattle import create_board, place_ships, print_board

# Replace 'your_module_name' with the actual name of the module where your code is located.

@given("I have a game board")
def step_impl(context):
    context.board = create_board()
    context.ships = {
        "Aircraft Carrier": 4,
        "Battleship": 3,
        "Submarine": 2,
        "Destroyer": 2,
        "Patrol Boat": 1,
    }

@when("I place ships on the board")
def step_impl(context):
    place_ships(context.board)

@then("the ships should be placed correctly")
def step_impl(context):
    for ship, size in context.ships.items():
        ship_found = False
        for row in context.board:
            for cell in row:
                if cell == "S":
                    ship_found = True
                    size -= 1
                    if size == 0:
                        break
            if size == 0:
                break
        assert ship_found, f"Ship '{ship}' not placed correctly."
