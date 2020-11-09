import random
from math import exp
from board import Board
from typing import List


class SBS_Agent:

    def __init__(self, board: Board, iterations):
        self.board = board
        self.stochasticSize = 10
        if iterations is not None:
            self.counter = iterations
        else:
            self.counter = 100000
        self.board_list: List[Board] = self.build_boards(board, self.stochasticSize)
        self.board_size = board.get_board_size()
        board.populate()

    def build_boards(self, board:Board, amount):
        lst = []
        for amt in range(amount):
            b1 = Board(board.entries, board.size)
            b1.populate()
            lst.append(b1)
        return lst

    def cost(self, board):
        penalty = 0
        for i in range(1, self.board_size):
            col = board[:, i]
            col_set = set()
            for j in range(len(col)):
                if col[j] in col_set:
                    penalty += 1
                col_set.add(col[j])
        return penalty

    def cost2(self, board):
        penalty = 0
        for i in range(1, self.board_size):
            col = board[:, i]
            row = board[i]
            col_set = set()
            row_set = set()
            for j in range(len(col)):
                if col[j] in col_set:
                    penalty += 1
                if row[j] in row_set:
                    penalty += 1
                col_set.add(col[j])
                row_set.add(row[j])
        return penalty

    def solve1(self):
        for _ in range(self.counter):
            for index, board in enumerate(self.board_list):
                beamLst = []
                for _ in self.board_list:
                    while True:
                        row1 = random.randint(0, board.size)
                        col1 = random.randint(0, board.size)
                        row2 = random.randint(0, board.size)
                        col2 = random.randint(0, board.size)
                        if row1 != row2 and col1 != col2 and \
                            board.check_coordinates(row1, col1) and \
                                board.check_coordinates(row2, col2) and\
                                board.board[row1][col1] != board.board[row2][col2]:
                            board.swap_coordinates((row1, col1), (row2, col2))
                            beamLst.append(board.get_copy_of_board())
                            board.swap_coordinates((row1, col1), (row2, col2))
                            break
                    if board.win():
                        self.board.board = board.board
                        return True
                if random.uniform(0, 1) > 0.8:
                    pick = beamLst[random.randint(0, len(beamLst) - 1)]
                    if self.cost(pick) < self.cost(board.board):
                        board.board = pick
                    else:
                        if random.uniform(0,1) > 0.5:
                            new_board = Board(board.entries, board.size)
                            new_board.populate()
                            self.board_list[index] = new_board
                else:
                    best_b = beamLst[0]
                    penalty = self.cost(best_b)
                    for b in beamLst:
                        p1 = self.cost(b)
                        if p1 < penalty:
                            penalty = p1
                            best_b = b
                    board.board = best_b
        for board in self.board_list:
            if self.cost(board.board) < self.cost(self.board.board):
                self.board.board = board.board
        print(self.cost(self.board.board))
        return False




    def solve(self):
        for _ in range(self.counter):
            for index, board in enumerate(self.board_list):
                beamLst = []
                for _ in self.board_list:
                    while True:
                        row1 = random.randint(0, board.size)
                        col1 = random.randint(0, board.size)
                        row2 = row1
                        col2 = random.randint(0, board.size)
                        if col1 != col2 and \
                            board.check_coordinates(row1, col1) and \
                                board.check_coordinates(row2, col2) and\
                                board.board[row1][col1] != board.board[row2][col2]:
                            board.swap_coordinates((row1, col1), (row2, col2))
                            beamLst.append(board.get_copy_of_board())
                            board.swap_coordinates((row1, col1), (row2, col2))
                            break
                    if board.win():
                        self.board.board = board.board
                        return True
                if random.uniform(0, 1) > 0.8:
                    pick = beamLst[random.randint(0, len(beamLst) - 1)]
                    if self.cost(pick) < self.cost(board.board):
                        board.board = pick
                    else:
                        if random.uniform(0,1) > 0.8:
                            new_board = Board(board.entries, board.size)
                            new_board.populate()
                            self.board_list[index] = new_board
                else:
                    best_b = beamLst[0]
                    penalty = self.cost(best_b)
                    for b in beamLst:
                        p1 = self.cost(b)
                        if p1 < penalty:
                            penalty = p1
                            best_b = b
                    board.board = best_b
        for board in self.board_list:
            if self.cost(board.board) < self.cost(self.board.board):
                self.board.board = board.board
        print(self.cost(self.board.board))
        return False
