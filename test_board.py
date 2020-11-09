import pytest
import numpy as np

import file_parser
from board import Board


def test_4_by_4_board_initialization():
    games = file_parser.read_games("sudoku_4x4_test")
    b = Board(games[0], 4)
    # integers = [int(character) for character in games[0]]
    assert np.array_equal(b.board, [[0, 3, 4, 0], [4, 0, 0, 2], [1, 0, 0, 3], [0, 2, 1, 0]]), \
        'problem with initializing 4 by 4 board'


def test_4_by_4_board_illegal_moves():
    games = file_parser.read_games("sudoku_4x4_test")
    board = Board(games[0], 4)

    assert not board.check_move_valid(2, 0, 3), 'this is an unchangeable coordinate'
    assert not board.check_move_valid(3, 3, 1), 'this is an unchangeable coordinate'
    assert not board.check_move_valid(3, 3, 2), 'this is an unchangeable coordinate'

    assert not board.check_move_valid(1, 0, 0), 'there is already a one in the column'
    assert not board.check_move_valid(2, 0, 1), 'there is already a two in the column'
    assert not board.check_move_valid(4, 0, 1), 'there is already a four in the column'

    assert not board.check_move_valid(3, 1, 1), 'there is already a three in the row'

    assert board.check_move_valid(3, 1, 2), 'there is already a three in the subgrid'
    assert not board.check_move_valid(4, 1, 1), 'there is already a four in the subgrid'


def test_4_by_4_get_rows():
    games = file_parser.read_games("sudoku_4x4_test")
    board = Board(games[0], 4)

    assert np.array_equal(board.get_row(0), [0, 3, 4, 0])
    assert np.array_equal(board.get_row(1), [4, 0, 0, 2])
    assert np.array_equal(board.get_row(2), [1, 0, 0, 3])
    assert np.array_equal(board.get_row(3), [0, 2, 1, 0])


def test_4_by_4_get_columns():
    games = file_parser.read_games("sudoku_4x4_test")
    board = Board(games[0], 4)

    assert np.array_equal(board.get_column(0), [0, 4, 1, 0])
    assert np.array_equal(board.get_column(1), [3, 0, 0, 2])
    assert np.array_equal(board.get_column(2), [4, 0, 0, 1])
    assert np.array_equal(board.get_column(3), [0, 2, 3, 0])


def test_4_by_4_sub_grid_coordinates():
    games = file_parser.read_games("sudoku_4x4_test")
    board = Board(games[0], 4)

    # upper left subgrid
    assert board.get_sub_grid_coordinates(0, 0) == (0, 0), 'problem in the upper left subgrid'
    assert board.get_sub_grid_coordinates(0, 1) == (0, 0), 'problem in the bottom left subgrid'
    assert board.get_sub_grid_coordinates(1, 0) == (0, 0), 'problem in the bottom left subgrid'
    assert board.get_sub_grid_coordinates(1, 1) == (0, 0), 'problem in the bottom left subgrid'

    # bottom left subgrid
    assert board.get_sub_grid_coordinates(2, 0) == (2, 0), 'problem in the bottom left subgrid'
    assert board.get_sub_grid_coordinates(2, 1) == (2, 0), 'problem in the bottom left subgrid'
    assert board.get_sub_grid_coordinates(3, 0) == (2, 0), 'problem in the bottom left subgrid'
    assert board.get_sub_grid_coordinates(3, 1) == (2, 0), 'problem in the bottom left subgrid'

    # upper right subgrid
    assert board.get_sub_grid_coordinates(0, 2) == (0, 2), 'problem in the upper right subgrid'
    assert board.get_sub_grid_coordinates(0, 3) == (0, 2), 'problem in the upper right subgrid'
    assert board.get_sub_grid_coordinates(1, 2) == (0, 2), 'problem in the upper right subgrid'
    assert board.get_sub_grid_coordinates(1, 3) == (0, 2), 'problem in the upper right subgrid'

    # bottom right subgrid
    assert board.get_sub_grid_coordinates(2, 2) == (2, 2), 'problem in the bottom right corner'
    assert board.get_sub_grid_coordinates(2, 3) == (2, 2), 'problem in the bottom right corner'
    assert board.get_sub_grid_coordinates(3, 2) == (2, 2), 'problem in the bottom right corner'
    assert board.get_sub_grid_coordinates(3, 3) == (2, 2), 'problem in the bottom right corner'


def test_4_by_4_check_value_in_sub_grid():
    games = file_parser.read_games("sudoku_4x4_test")
    board = Board(games[0], 4)

    assert not board.check_val_in_sub_grids(3, 0, 0)
    assert not board.check_val_in_sub_grids(4, 0, 0)

    assert not board.check_val_in_sub_grids(3, 3, 3)
    assert not board.check_val_in_sub_grids(2, 1, 2)


def test_4_by_4_place():
    games = file_parser.read_games("sudoku_4x4_test")
    board = Board(games[0], 4)
    board.place(2, 0, 0)
    board.place(1, 0, 3)
    board.place(3, 3, 0)

    assert board.board[0, 0] == 2
    assert board.board[0, 3] == 1
    assert board.board[3, 0] == 3
