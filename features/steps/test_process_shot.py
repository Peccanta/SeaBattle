from behave import given, when, then
from shipBattle import process_shot


# Замените 'your_module_name' на имя вашего модуля, где находится функция process_shot

@given("a game board")
def step_given_game_board(context):
    context.board = [
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "S", "S", "0", "0", "0", "0", "0", "0", "0"]
    ]

@when("the process_shot function is called with row {row:d} and col {col:d}")
def step_when_process_shot_called(context, row, col):
    context.result = process_shot(context.board, row, col)


@then("it should print {expected_message}")
def step_then_check_message(context, expected_message):
    print(f"Expected message: {expected_message}")
    print(f"Actual result: {context.result}")
    assert context.result == expected_message