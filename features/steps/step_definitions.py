from behave import given, when, then
from shipBattle import is_valid_placement, create_board

@given('есть игровое поле')
def step_create_board(context):
    context.board = create_board()

@when('функция is_valid_placement вызывается с параметрами "{board}", "{row}", "{col}", "{orientation}", "{size}"')
def step_validate_ship_placement(context, board, row, col, orientation, size):
    row = int(row)
    col = int(col)
    size = int(size)
    context.result = is_valid_placement(context.board, row, col, orientation, size)

@then('результат должен быть "{expected_result}"')
def step_check_result(context, expected_result):
    expected_result = expected_result.lower() == "true"
    assert context.result == expected_result
