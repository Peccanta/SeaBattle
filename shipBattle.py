import random


# Создаем игровое поле размером 10x10
def create_board():
    board = []
    for _ in range(10):
        row = ["O"] * 10  # "O" обозначает пустое место
        board.append(row)
    return board

# Выводим игровое поле
def print_board(board, hide_computer_ships=False):
    header = "  A B C D E F G H I J"
    print(header)
    for i, row in enumerate(board):
        print_row = []
        for cell in row:
            if hide_computer_ships and cell == "S":
                print_row.append("O")  # Если корабль компьютера должен быть скрыт, заменяем "S" на "O"
            else:
                print_row.append(cell)
        print(f"{i + 1} {' '.join(print_row)}")


# Размещаем корабли на поле
def place_ships(board):
    def place_ships(board):
        ships = {
            "Aircraft Carrier": 4,
            "Battleship": 3,
            "Submarine": 2,
            "Destroyer": 2,
            "Patrol Boat": 1,
        }
        for ship, size in ships.items():
            place_ship(board, ship, size)


# Размещаем один корабль на поле
def place_ship(board, ship, size):
    while True:
        orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            row = random.randint(0, 9)
            col = random.randint(0, 10 - size)
        else:
            row = random.randint(0, 10 - size)
            col = random.randint(0, 9)
        if is_valid_placement(board, row, col, orientation, size):
            if orientation == "horizontal":
                for i in range(size):
                    board[row][col + i] = "S"  # "S" обозначает корабль
            else:
                for i in range(size):
                    board[row + i][col] = "S"  # "S" обозначает корабль
            break


# Проверяем, можно ли разместить корабль в данной позиции
def is_valid_placement(board, row, col, orientation, size):
    def is_neighboring(row, col):
        # Проверяет, есть ли соседние клетки (верх, вниз, влево, вправо, диагональ)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < 10 and 0 <= c < 10 and board[r][c] != "O":
                return True
        return False

    if orientation == "horizontal":
        for i in range(size):
            if board[row][col + i] != "O" or is_neighboring(row, col + i):
                return False
    else:
        for i in range(size):
            if board[row + i][col] != "O" or is_neighboring(row + i, col):
                return False
    return True


# Получение координат хода от игрока
def get_player_move():
    while True:
        try:
            print("\nВаш ход:")
            guess = input("Введите координаты (например, A3): ").upper()
            col = ord(guess[0]) - ord("A")
            row = int(guess[1:]) - 1
            if 0 <= row < 10 and 0 <= col < 10:
                return row, col
            else:
                print("Неверные координаты. Пожалуйста, введите снова.")
        except (ValueError, IndexError):
            print("Неверный формат ввода. Пожалуйста, введите снова.")


# Ход игрока
def player_turn(board):
    player_row, player_col = get_player_move()
    if board[player_row][player_col] == "S":
        print("Попадание!")
        board[player_row][player_col] = "X"
    else:
        print("Промах.")
        board[player_row][player_col] = "*"


# Ход компьютера
def computer_turn(board):
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if board[row][col] != "X" and board[row][col] != "*":
            return row, col


# Обработка попадания или промаха
def process_shot(board, row, col):
    if board[row][col] == "S":
        result = "Попадание!"
        board[row][col] = "X"
    else:
        result = "Промах."
        board[row][col] = "*"
    print(f"Result: {result}")  # Add this line for debugging
    return result


# Проверка завершения игры
def check_game_over(board):
    # Подсчитываем количество оставшихся кораблей
    remaining_ships = sum(board.count("S") for board in board)
    # Если не осталось кораблей, игра завершена
    return remaining_ships == 0


# Основная функция игры
def main():
    player_board = create_board()
    computer_board = create_board()

    print("Добро пожаловать в игру 'Морской бой'!")
    print("Ваше поле:")
    print_board(player_board)

    place_ships(player_board)
    place_ships(computer_board)

    while True:
        player_turn(computer_board)

        print("\nПоле компьютера:")
        print_board(computer_board, hide_computer_ships=True)

        if check_game_over(computer_board):
            print("Вы выиграли! Поздравляем!")
            break

        computer_row, computer_col = computer_turn(player_board)
        process_shot(player_board, computer_row, computer_col)

        print("\nВаше поле:")
        print_board(player_board)

        if check_game_over(player_board):
            print("Компьютер выиграл. Попробуйте еще раз.")
            break


if __name__ == "__main__":
    main()
