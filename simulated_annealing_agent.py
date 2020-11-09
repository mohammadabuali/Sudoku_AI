import random
from math import exp
from board import Board
from matplotlib import pyplot as plt


class SA_Agent:

    def __init__(self, board: Board, temp, decay):
        self.board: Board = board
        self.board_size = board.get_board_size()
        if temp is not None:
            self.temp = temp
        else:
            self.temp = 10000
        if decay is not None and decay < 1:
            self.decay = decay
        else:
            self.decay = 0.99
        board.populate()
        x = 5


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

    def cost1(self, board):

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

    def solve(self):
        tempLst = []
        costLst = []
        T = self.temp
        T1 = self.temp
        decay = self.decay
        while T > 1:
            tempLst.append(T1 - T+1)
            costLst.append(self.cost(self.board.board))
            board = self.board
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
                    b = board.get_copy_of_board()
                    board.swap_coordinates((row1, col1), (row2, col2))
                    break
            if self.board.win():
                return True
            penalty = self.cost(self.board.get_copy_of_board()) - self.cost(b)
            if penalty > 0:
                self.board.board = b
            else:
                if (exp(penalty/T) - random.uniform(0, 1)) > 0:
                    self.board.board = b

            T *= decay
        fig = plt.figure()
        plt.xlabel('Temperature')
        plt.xlim(tempLst[-1], tempLst[0])
        plt.ylabel('Number of collisions')

        plt.plot(tempLst, costLst)
        plt.show()
        return False

    def solve1(self):
        tempLst = []
        costLst = []
        T = 1000000
        alpha = 0.9999
        while T > 1:
            tempLst.append(T)
            costLst.append(self.cost(board.board))
            board = self.board
            while True:
                row1 = random.randint(0, board.size)
                col1 = random.randint(0, board.size)
                row2 = random.randint(0, board.size)
                col2 = random.randint(0, board.size)
                if row1 != row2 and col1 != col2 and \
                        board.check_coordinates(row1, col1) and \
                        board.check_coordinates(row2, col2) and \
                        board.board[row1][col1] != board.board[row2][col2]:
                    board.swap_coordinates((row1, col1), (row2, col2))
                    b = board.get_copy_of_board()
                    board.swap_coordinates((row1, col1), (row2, col2))
                    break
            if self.board.win():
                return True
            penalty = self.cost(self.board.get_copy_of_board()) - self.cost(b)
            if penalty > 0:
                self.board.board = b
            else:
                if (exp(penalty / T) - random.uniform(0, 1)) > 0:
                    self.board.board = b

            T *= alpha
        fig = plt.figure()
        plt.plot(tempLst, costLst)
        plt.xlabel('Temperature')
        plt.ylabel('Number Of Collisions')
        plt.show()

        return False