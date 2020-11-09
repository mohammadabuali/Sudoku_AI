import random

from board import Board


class BacktrackingAgent:

    def __init__(self, board: Board, choosing_variable_heuristics=None, choosing_value_heuristics=None):
        self.board: Board = board
        self.board_size = board.get_board_size()
        if choosing_variable_heuristics is None:
            self.choosing_variable_heuristics = self.choose_variable_randomly
        else:
            self.choosing_variable_heuristics = choosing_variable_heuristics
        if choosing_value_heuristics is None:
            self.choosing_value_heuristics = self.choose_value_randomly
        else:
            self.choosing_value_heuristics = choosing_value_heuristics

        self.empty_coordinates_list = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board.get_assignment_at(row, col) == 0:
                    self.empty_coordinates_list.append((row, col))

    def solve(self):
        return self._mrv_backtracking(self.empty_coordinates_list.copy())
        # random.shuffle(self.empty_coordinates_list)
        # return self._backtracking(0)

    # def _backtracking(self, index):
    #     if index == len(self.empty_coordinates_list):
    #         return True
    #
    #     row, col = self.empty_coordinates_list[index]
    #     a = self.board.valid_values.copy()
    #     random.shuffle(a)
    #     for value in a:
    #         if self.board.check_move_valid(value, row, col):
    #             previous_value = self.board.get_assignment_at(row, col)
    #             self.board.place(value, row, col)
    #             if self._backtracking(index + 1):
    #                 return True
    #             self.board.board[row, col] = previous_value
    #
    #     return False

    def _mrv_backtracking(self, empty_coordinates_list):
        if len(empty_coordinates_list) == 0:
            return True

        assignment = self.choosing_variable_heuristics(empty_coordinates_list)
        if assignment is None:
            return False
        row, col, legal_values = assignment
        empty_coordinates_list.remove((row, col))

        legal_values = self.choosing_value_heuristics(row, col, legal_values, empty_coordinates_list)

        for value in legal_values:
            previous_value = self.board.get_assignment_at(row, col)
            self.board.board[row, col] = value

            if self._mrv_backtracking(empty_coordinates_list):
                return True

            self.board.board[row, col] = previous_value

        empty_coordinates_list.append((row, col))

        return False

    def choose_variable_randomly(self, empty_coordinates_list):
        row, col = random.choice(empty_coordinates_list)
        legal_values = []

        for value in self.board.valid_values:
            if self.board.check_move_valid(value, row, col):
                legal_values.append(value)

        if len(legal_values) == 0:
            return None

        return row, col, legal_values

    @staticmethod
    def choose_value_randomly(row, col, legal_values, empty_coordinates_list):
        random.shuffle(legal_values)
        return legal_values
