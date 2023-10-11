import unittest
from io import StringIO
from unittest.mock import patch
import random

# Импортируем функции, которые нужно протестировать
from shipBattle import create_board, \
    print_board, get_player_move, player_turn, computer_turn


class TestBattleshipGame(unittest.TestCase):

    def setUp(self):
        self.player_board = create_board()
        self.computer_board = create_board()


if __name__ == '__main__':
    unittest.main()
