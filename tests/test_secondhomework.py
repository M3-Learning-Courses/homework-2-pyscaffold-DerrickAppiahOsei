# test_tic_tac_toe.py
import pytest
import my_second_homework.secondhomework
#from unittest.mock import patch
#from my_second_homework import TicTacToe  # Import your Tic-Tac-Toe game class

# Test to check the initial state of the game board
def test_initial_board():
    """
    Test that the board is empty when a new game instance is created.
    """
    game = my_second_homework.secondhomework.myClass()  # Create a new game instance
    assert game.board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # Assert that the board is empty

# Test to check a player's move on the board
def test_player_move():
    """
    Test the make_move method of the myClass class to ensure that it correctly updates the game board.
    """
    game = my_second_homework.secondhomework.myClass()  # Create a new game instance
    game.make_move(0, 0)  # Make a move for the current player ('X')
    assert game.board == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # Assert that the board reflects the move

# Test to check the detection of a game winner
def test_winner_detection():
    """
    Test the check_winner method of the myClass class to ensure that it correctly detects the winner of a game.
    """
    game = my_second_homework.secondhomework.myClass()  # Create a new game instance
    game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]  # Set up a winning scenario for 'X'
    assert game.check_winner() == 'X'  # Assert that 'X' is detected as the winner

# Test to check the detection of a draw
def test_draw_detection():
    """
    Test that the check_draw method correctly detects a draw scenario on the game board.
    """
    game = my_second_homework.secondhomework.myClass()  # Create a new game instance
    game.board = [['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'X', 'O']]  # Set up a draw scenario
    assert game.check_draw()  # Assert that a draw is detected

if __name__ == "__main__":
    pytest.main