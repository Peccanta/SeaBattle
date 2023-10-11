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

    def test_print_board(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_board(self.player_board)
            output = mock_stdout.getvalue()
            self.assertTrue("  A B C D E F G H I J" in output)
            self.assertTrue("1 O O O O O O O O O O" in output)
    
    def test_get_player_move(self):
        with patch('builtins.input', side_effect=["A3"]):
            row, col = get_player_move()
            self.assertEqual(row, 2)
            self.assertEqual(col, 0)

if __name__ == '__main__':
    unittest.main()
